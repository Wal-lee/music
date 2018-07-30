from . import main
from flask import render_template

@main.route('/')
def main_page():
    return render_template('main.html', weather='晴天')