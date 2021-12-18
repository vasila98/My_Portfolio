from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app=Flask(__name__)


UPLOAD_FOLDER = 'static/uploads'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

db=SQLAlchemy(app)
migrate = Migrate(app, db)

from models import *

from admin.routes import *
from app.routes import *


if __name__=='__main__':
    # db.create_all()
    app.run(debug=True)    



