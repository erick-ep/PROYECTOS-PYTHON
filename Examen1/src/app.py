from flask import Flask, redirect, render_template,request, url_for

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

@app.route('/buscar', methods=['GET'])
def buscar():
    query = request.args.get('query')  
    if query == 'contenido':
        return redirect(url_for('contenido')) 
    elif query == 'redes_sociales':
        return redirect(url_for('sobre_mi')) 
    elif query == 'habilidades':
        return redirect(url_for('habilidades'))
    else:
        return render_template('404.html', query=query) 


app.run(debug=True)