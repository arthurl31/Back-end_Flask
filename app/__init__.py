from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
import os

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app=app)
app.config['SECRET_KEY'] = os.urandom(32)

from app.models import *

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

from app import controllers
