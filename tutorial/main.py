from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    name = 'Codi'
    course = 'Python Web'
    isPremium = False
    courses = ['Python', 'Ruby', 'Java', 'Elixir']

    return render_template('index.html', username=name, courseName=course, premium=isPremium, courses=courses)


if __name__ == '__main__':
    app.run(debug=True)

