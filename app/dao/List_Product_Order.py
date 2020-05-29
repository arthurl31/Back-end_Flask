from app.models.model import Product_Order as l
from app import db


def getAll():
    try:
        return l.query.all()
    except:
        return False


def insert_order(product_id, order_id):
    try:
        db.session.add(Product_Order(fk_product_id=int(product_id), fk_order_id=int(order_id)))
        db.session.commit()
        return db.session.query(db.func.max(Product_Order.id)).first()
    except:
        return False


def getById(order_id):
    try:
        return Product_Order.query.get(int(order_id))
    except:
        return False


def delete_order(order_id):
    try:
        data = Product_Order.query.get(int(order_id))
        db.session.delete(data)
        db.session.commit()
        return True
    except:
        return False