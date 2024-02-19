from flask import Flask, render_template

app = Flask(__name__) 

@app.route('/')

def plantilla():
    data={
        'titulo':'Página plantilla',
        'mensaje':'hola chavales',
        'nombre':'Erick Antonio de Jesus Espinosa Piste'        
    }
    return render_template('pagina1.html',data=data) 
app.run(debug=True)