from sqlalchemy.dialects.postgresql.psycopg2 import logger
from sqlalchemy.exc import SQLAlchemyError
from app import db
from app.models.model import Product


def getAll():
    try:
        return Product.query.all()
    except SQLAlchemyError as e:
        logger.error(e.args)
        return False


def insert_product(name_product, value, quantity, add_by, add_at=False):
    try:
        db.session.add(
            Product(product_name=str(name_product), product_value=float(value), available_quantity=int(quantity),
                    add_by=int(add_by)))
        db.session.commit()
        return db.session.query(db.func.max(Product.id)).first()
    except SQLAlchemyError as e:
        logger.error(e.args)
        return False


def getById(id_product):
    try:
        return Product.query.get(int(id_product))
    except SQLAlchemyError as e:
        logger.error(e.args)
        return False


def update_product(id_product, name_product, value, quantity, add_by):
    try:
        data = Product.query.get(int(id_product))
        data.product_name = str(name_product)
        data.product_value = float(value)
        data.available_quantity = int(quantity)
        data.add_by = int(add_by)
        db.session.add(data)
        db.session.commit()
        return True
    except SQLAlchemyError as e:
        logger.error(e.args)
        return False


def delete_product(id_product):
    try:
        data = Product.query.get(int(id_product))
        db.session.delete(data)
        db.session.commit()
        return True
    except SQLAlchemyError as e:
        logger.error(e.args)
        return False


def alter_active_state(id, state):
    try:
        data = Product.query.get(int(id))
        data.is_active = state
        db.session.add(data)
        db.session.commit()
        return True
    except SQLAlchemyError as e:
        logger.error(e.args)
        return False
