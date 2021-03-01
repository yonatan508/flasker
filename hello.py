from flask import Flask, render_template


# create a flask app
app = Flask(__name__)

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