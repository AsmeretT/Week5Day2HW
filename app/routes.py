from app import app
from flask import render_template

@app.route('/')
def home():
    
    return render_template('index.html')

@app.route('/favefive')
def faveFivepage():
    names = ['Brandy', 'Kaytranada', 'NAO', 'Wizkid', 'Burna Boy']
    return render_template('favefive.html', my_list=names)

