import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///product.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



db = SQLAlchemy(app)

class Shoes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    size = db.Column(db.Integer)
    price = db.Column(db.Integer)

@app.route('/')
def index():
    query = Shoes.query.all()
    return render_template('index.html', shoes=query)
@app.route('/contact')
def contact():
    var = "CONTACT | PAGE"
    render_template('contact.html', title=var)
@app.route('/')
def signup():
    var = "SIGN-UP | PAGE"
    render_template('signup.html', title=var)
@app.route('/')
def login():
    var = "LOGIN | PAGE"
    render_template('.html', title=var)
@app.route('/')
def error404():
    var = "Error 404!"
    render_template('404.html', title=var)
@app.route('/')
def error500():
    var = "Error 500!"
    render_template('500.html', title=var)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
