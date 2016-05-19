from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from blueprint import blueprint


DB = SQLAlchemy()
app = Flask(__name__)
app.config.from_object('app.config')
DB.init_app(app)
app.register_blueprint(blueprint)
