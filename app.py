from flask import Flask, render_template
from spreadsheet import get_data

app = Flask(__name__)


@app.route('/')
def index():
    data = get_data()
    return render_template('index.html', name=data["walker"], day=data["day"], time=data["time"])

if __name__ == '__main__':
    app.run(debug=True)
