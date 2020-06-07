from app import app
from app.dao import Adress as a
from app import db


@app.route("/")
def index():
    print(a.insert_adress('a', 'b'))
    print('')
    return "Hello World"
