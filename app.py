from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cakes')
def cakes():
    return render_template('cakes.html')

@app.route('/sarah')
def sarah():
    return render_template('sarah.html')

@app.route('/daniel')
def daniel():
    return render_template('daniel.html')

@app.route('/juliette')
def juliette():
    return render_template('juli.html')



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
