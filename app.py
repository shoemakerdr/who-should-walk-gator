import os
from flask import Flask, render_template
from spreadsheet import get_data

app = Flask(__name__)


@app.route('/')
def index():
    data = get_data()
    return render_template('index.html', name=data["walker"], day=data["day"], time=data["time"])

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
