from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/quemsomos')
def quemsomos():
    return render_template('quemsomos.html')

@app.route('/contato')
def cotato():
    return render_template('contato.html')

if __name__ == '__main__':
    app.run(debug=True)
