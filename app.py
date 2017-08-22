from flask import Flask
from spreadsheet import get_walker

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>' + get_walker() + ' should walk Gator next.</h1>'

if __name__ == '__main__':
    app.run(debug=True)
