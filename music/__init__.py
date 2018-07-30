from flask import Flask
from music.app.views import web 
from music.main.views import main


def create_app():
    app=Flask(__name__)
    app.config.from_object('config')
    app.register_blueprint(main)
    app.register_blueprint(web)
    return app