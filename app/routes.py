from flask import render_template, Blueprint, url_for, redirect

main = Blueprint('main', __name__)

# Ruta principal
@main.route('/')
def home():
    
    return render_template('home.html')

# Ruta about
@main.route('/about')
def about():
    return render_template('about.html')

# Ruta contacto
@main.route("/contacto")
def contacto():
    return render_template('contacto.html')