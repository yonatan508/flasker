from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired


# create a flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = "My game is not good"

#create a form class
class NamerForm(FlaskForm):
    user_name = StringField("Enter User Name", validators=[DataRequired()])
    user_password = PasswordField("Enter Password", validators=[DataRequired()])
    submit = SubmitField("Submit")


# create a route decorator
@app.route("/")

#def index():
#    return "<h1>hello world</h1>"

def index():
    favorite_food = ["pizza","hamborger","pasta","meet",50]
    name = "yonatan kazaz"
    return render_template("index.html",
    name = name,
    favorite_food = favorite_food)


#localhost:5000/user/yonatan
@app.route("/user/<name>")

def user(name):
    return render_template("user.html",name=name)

# Invaild URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500

@app.route("/name", methods=['GET','POST'])
def name():
    name = None
    password = None
    form_user = NamerForm()
    form_password = NamerForm()
    #validate form
    if form_user.validate_on_submit():
        name = form_user.user_name.data
        form_user.user_name.data = ''
        password = form_password.user_password.data
        form_password.user_password.data = ''
    return render_template("name.html",
        name = name,
        password = password,
        form_user = form_user,
        form_password = form_password)