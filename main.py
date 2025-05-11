from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def start():
    return render_template('category.html')

@app.route('/alat')
def index():
    return render_template('alat.html')

app.run(debug=True)