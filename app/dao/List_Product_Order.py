from app.models.model import Product_Order
from app import db
from sqlalchemy.dialects.postgresql.psycopg2 import logger
from sqlalchemy.exc import SQLAlchemyError


def getAll():
    try:
        return Product_Order.query.all()
    except:
        return False


def insert_order(product_id, order_id):
    try:
        db.session.add(Product_Order(order_id=int(order_id), product_id=int(product_id)))
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
        data = Product_Order.query.filter(Product_Order.fk_order_id == int(order_id)).first()
        db.session.delete(data)
        db.session.commit()
        return True
    except SQLAlchemyError as e:
        logger.error(e.args)
        return False


def get_order_by_product(product_id):
    try:
        data = Product_Order.query.filter(Product_Order.fk_product_id == int(product_id)).all()
        return data
    except SQLAlchemyError as e:
        logger.error(e.args)
        return False
