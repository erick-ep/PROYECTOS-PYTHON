from flask import Flask, render_template

app = Flask(__name__) 

@app.route('/')

def plantilla():
    data={
        'titulo':'Página plantilla',
        'mensaje':'Hola chavales sean bienvenidos a mi sitio web:)',
        'nombre':'Erick Antonio de Jesus Espinosa Piste'        
    }
    return render_template('pagina.html',data=data) 

@app.route('/login')
def login():
   
    return render_template('login.html') 

app.run(debug=True)