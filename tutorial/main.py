from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    name = 'Codi'
    course = 'Python Web'
    return render_template('index.html', username=name, courseName=course)


if __name__ == '__main__':
    app.run(debug=True)

