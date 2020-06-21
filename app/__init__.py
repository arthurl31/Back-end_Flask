from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

app = Flask(__name__)
app.static_folder = 'static'
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

app.config.from_object('config')

db = SQLAlchemy(app=app)

from app.models import *

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

from app.controllers import controller
