from flask import Blueprint, render_template

bp = Blueprint("pages", __name__, template_folder = 'templates')

@bp.route("/")
def home():
    return render_template("home.html")

@bp.route("/projects")
def projects():
    return render_template("projects.html")

@bp.route("/contacts")
def contacts():
    return render_template("contacts.html")