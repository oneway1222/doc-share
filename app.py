from flask import Flask, render_template, request, url_for, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, validators
from DatabaseController import DatabaseController
import mysql.connector

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
config = {
    'user': "root",
    'password': "root",
    'host': "127.0.0.1",
    'port': "3306",
    'database': "docshare"
}
dbcontroller = DatabaseController(config)

@app.route('/', methods=['GET', 'POST'])
def sign_in():
    return render_template('sign_in.html')


class RegForm(FlaskForm):
    username = StringField("Please enter your username", validators=[validators.Length(min=1, max=10)])
    password = PasswordField("password", validators=[validators.Length(min=1, max=10)])
    submit = SubmitField("Submit")


@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    username = False
    password = ""
    form = RegForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        
        try:
            dbcontroller.sign_up(username, password)
        except mysql.connector.errors.IntegrityError as e:
            return render_template('sign_up.html', form=form, username="", password="", e=e)

    return render_template('sign_up.html', form=form, username=username, password=password)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)