from flask import Flask
import os

def create_app(config_name):
    app = Flask(__name__)  
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY']='frase-secreta'
    app.config['PROPAGATE_EXCEPTIONS'] = True
    return app