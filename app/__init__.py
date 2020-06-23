from flask import Flask, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_login import LoginManager
import os

app = Flask(__name__)
app._static_folder = os.path.abspath("static/")
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

app.config.from_object('config')

db = SQLAlchemy(app=app)

from app.models import *

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

login_manager = LoginManager()
login_manager.init_app(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    return redirect('login')


from app.controllers import employerController, productController, orderController, cartController
