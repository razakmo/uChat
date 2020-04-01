from app.main import bp
from flask import Flask, render_template


@bp.route('/', methods=['GET', 'POST'])
def home():
    return render_template('main/home.html', title="Home")
