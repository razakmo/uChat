from flask import Flask, render_template

from app.main import bp


@bp.route("/", methods=["GET", "POST"])
def home():
    return render_template("main/home.html", title="Home")
