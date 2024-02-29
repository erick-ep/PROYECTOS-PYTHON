from flask import Flask, render_template

app = Flask(__name__) 

@app.route('/')
def base():
       return render_template('base.html') 

@app.route('/login')
def login():
   
    return render_template('login.html') 

@app.route('/signin')
def signin():
    return render_template('signin.html')

@app.route('/index')
def index():
    return render_template('index.html')

app.run(debug=True)