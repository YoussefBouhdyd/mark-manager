from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

basedir = os.path.abspath(os.path.dirname(__file__))

db = SQLAlchemy()
def create_app():
    app = Flask(__name__,static_url_path="/")
    app.secret_key = "1234"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'database/marks.db')
    db.init_app(app)
    from routes import register_routes
    register_routes(app,db)
    migrate = Migrate(app,db) 
    return app