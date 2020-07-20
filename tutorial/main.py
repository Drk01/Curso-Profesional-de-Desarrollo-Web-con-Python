from flask import Flask
from flask import render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    name = 'Codi'
    course = 'Python Web'
    isPremium = False
    courses = ['Python', 'Ruby', 'Java', 'Elixir']

    return render_template('index.html', username=name, courseName=course, premium=isPremium, courses=courses)

@app.route('/usuario/<username>/<int:age>') #string #integer
def usuario(username, age):
    return 'Hola '+username+' '+'tienes ' + str(age) + ' años'

@app.route('/datos')
def datos():
    nombre = request.args.get('name', '') #Diccionario
    return 'Listado de datos: ' + str(nombre)

if __name__ == '__main__':
    app.run(debug=True)

