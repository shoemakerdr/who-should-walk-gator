from flask import Flask, render_template
from spreadsheet import get_walker

app = Flask(__name__)


@app.route('/')
def index():
    walker = get_walker()
    return render_template('index.html', name=walker)

if __name__ == '__main__':
    app.run(debug=True)
