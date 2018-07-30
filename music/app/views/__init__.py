from flask import Blueprint


web = Blueprint('music', __name__)

from music.app.views import view_music