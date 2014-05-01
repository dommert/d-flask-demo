# Dommert's Flask Foundation
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world(title='Hello World'):
    return render_template('foundation/default.html', title=title)

@app.route('/about')
def about(title='About Page'):
    return render_template('foundation/onecol.html', title=title)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
