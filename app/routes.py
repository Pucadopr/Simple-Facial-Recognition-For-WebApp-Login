from app import app
from flask import request, render_template
from flask_wtf import FlaskForm
from wtforms import StringField
from app.api_logic import execute_request, check_confidence
import json

from PIL import Image

class LoginForm(FlaskForm):
    username = StringField('Username')

@app.route('/', methods=['GET', 'POST'])
def index():
    login_form = LoginForm()
    if request.method == 'POST':
        username = request.form['username']
        file = request.files['file']
        image = Image.open(file)
        image.save('photo.jpg')

        json_obj = execute_request()
        flag = check_confidence(json_obj)

        if flag:
            return render_template('admin_panel.html', user=username)
        else:
            message = "Your photo was not recognized as a Thumming User. Please, try again."
            login_form = LoginForm()
            return render_template('login_form.html', title='Login', form=login_form, message=message)

    return render_template('base.html', title='Login', form=login_form, message="")

@app.route('/login_form/', methods=['GET'])
def login_form():
    login_form = LoginForm()
    return render_template('login_form.html', title='Login', form=login_form, message="")