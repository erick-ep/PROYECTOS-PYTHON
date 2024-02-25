from flask import Flask, render_template, request, redirect,url_for

app = Flask(__name__) 
user = ""
@app.route('/')

def plantilla():
    data={
        'titulo':'Página plantilla',
        'mensaje':'Hola chavales sean bienvenidos a mi sitio web:)',
        'nombre':'Erick Antonio de Jesus Espinosa Piste'        
    }
    return render_template('pagina1.html',data=data) 
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if (username == 'u' and password == '1'):
            user = username
            error_message = "todo correcto"
            return redirect ("/page1/" + user)

        else:
            error_message = "Usuario o contraseña incorrecta"
            print (error_message)
    return render_template('login.html') 

@app.route('/page1/<user>')
def saludo(user):
    return '<h2>hola '+ user +'</h2>'

app.run(debug=True)