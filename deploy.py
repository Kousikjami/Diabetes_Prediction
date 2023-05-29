from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
# Load the model
model=pickle.load(open('diabetes.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST', 'GET'])
def predict():
    a=request.form['a']
    b=request.form['b']
    c=request.form['c']
    d=request.form['d']
    e=request.form['e']
    f=request.form['f']
    g=request.form['g']
    h=request.form['h']
    #i=request['i']
    result=model.predict([[a,b,c,d,e,f,g,h]])[0]
    return render_template('index.html', prediction=result)


if __name__ == '__main__':
    app.run(debug=True)