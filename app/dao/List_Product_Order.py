from app.models.model import Product_Order as l
from app import db


def getAll():
    try:
        return l.query.all()
    except:
        return False


def insert_order(product_id, order_id):
    pass


def getById(order_id):
    pass


def delete_order(order_id):
    pass
