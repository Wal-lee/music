from flask import Blueprint

main = Blueprint('main', __name__)

from music.main.views import view_main