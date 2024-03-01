from flask import Flask, render_template

app = Flask(__name__) 

@app.route('/')
def index():
       return render_template('index.html') 

@app.route('/habilidades')
def habilidades():
   
    return render_template('habilidades.html') 

@app.route('/redes_sociales')
def redes_sociales():
    return render_template('redes_sociales.html')

@app.route('/sobre_mi')
def sobre_mi():
    return render_template('sobre_mi.html')

@app.route('/base')
def base():
    return render_template('base.html')

app.run(debug=True)