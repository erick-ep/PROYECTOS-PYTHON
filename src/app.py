from flask import Flask, redirect, render_template, request, url_for
import json

app = Flask(__name__)

# Cargar usuarios desde el archivo JSON o inicializar como un diccionario vacío si no existe
try:
    with open('usuarios.json', 'r') as file:
        usuarios = json.load(file)
except FileNotFoundError:
    usuarios = {}

@app.route('/')
def base():
    return render_template('base.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in usuarios and usuarios[username] == password:
            # Redirigir al usuario a una página de saludo si el inicio de sesión es exitoso
            return redirect(url_for('saludo', user=username))
        else:
            error_message = "Usuario o contraseña incorrecta"
            return render_template('login.html', error_message=error_message)

    return render_template('login.html')

@app.route('/signin')
def signin():
    return render_template('signin.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/saludo/<user>')
def saludo(user):
    return render_template('saludo.html', user=user)

if __name__ == '__main__':
    app.run(debug=True)
