from flask import Flask
from spreadsheet import get_walker

app = Flask(__name__)


@app.route('/')
def index():
    walker = get_walker()
    return '<h1>%s should walk Gator next</h1>' % walker

if __name__ == '__main__':
    app.run(debug=True)
