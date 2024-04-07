from flask import Flask, render_template, request 
import joblib

# create an instance of flask
app = Flask(__name__)

# @app.route('/')
# def base():
#      return 'Hello World'

@app.route('/') #decorator 
def homepage(): 
     return render_template('homepage.html') 
     #return('Hello World')

# @app.route('/predict', methods=['post'])
# def predict():
#      exp = request.form.get('experience')
#      phone = request.form.get('phone')
#      mail = request.form.get('email')

#      print(exp)
#      print(phone)
#      print(mail)

#      return "got the values...Thankyou"


@app.route('/predict', methods =['post']) #decorator 
def predict(): 
    #load the model
    model = joblib.load('dib_78.pkl')

    preg = int(request.form.get('preg'))
    plas = int(request.form.get('plas'))
    pres = int(request.form.get('pres'))
    skin = int(request.form.get('skin'))
    test = int(request.form.get('test'))
    mass = int(request.form.get('mass'))
    pedi = int(request.form.get('pedi'))
    age  = int(request.form.get('age'))

    #print(preg , plas , pres , skin , test , mass , pedi ,age)
    
    output = model.predict([[int(preg) , int(plas) , int(pres) , int(skin) , int(test) , int(mass) , int(pedi) , int(age)pip]])
   
    if output[0] == 0:
        value = "not diabetic"
    else :
        value = "diabetic"
      
    return render_template('predict.html', value = value)


if __name__ == "__main__":
    app.run(debug=True)

