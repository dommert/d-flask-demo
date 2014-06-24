# Dommert's Flask Foundation
from flask import Flask, render_template
app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def hello_world(title='Hello World'):
    return render_template('foundation/default.html', title=title)

@app.route('/about')
def about(title='About Page'):
    return render_template('foundation/onecol.html', title=title)


@app.route('/example')
def example(title='Example Page'):
    return render_template('foundation/example.html', title=title)

@app.route('/test/')
def test(title='Test Page'):
    return render_template('theme/about.html', title=title)

@app.route('/<path:path>')
def catch_all(path, title='Catch All'):
	return render_template('theme/about.html', title=title, path=path)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
