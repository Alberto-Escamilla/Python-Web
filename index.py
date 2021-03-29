#Se importa la librería de Flask
from flask import Flask, render_template #Render indica que se agregará una ruta en returun
#Se crea una variable APP para inicializar la libreria
app = Flask(__name__)
#Se crea la ruta home e inicia el servidor
@app.route('/')
def home():
    #Return devuelve el valor de la página
    return render_template('home.html')
     #Puedes agregar diferentes rutas
@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)#Permite actualizar la aplicación cada que se realiza un cambio