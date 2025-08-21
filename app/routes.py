from flask import Blueprint, render_template

main = Blueprint("main", __name__)

@main.route("/")
def home():
    # this will render index.html inside templates/
    return render_template("index.html", title="Home Page")

@main.route("/about")
def about():
    # pass a variable to the template
    return render_template("about.html", title="About Us")
