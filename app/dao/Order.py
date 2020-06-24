from app.models.model import Order
from app import db
from sqlalchemy.dialects.postgresql.psycopg2 import logger
from sqlalchemy.exc import SQLAlchemyError


def getAll():
    try:
        return Order.query.all()
    except:
        return False


def insert_order(total_value, notes, client, employer):
    try:
        db.session.add(
            Order(total_value=float(total_value), notes=str(notes), employer_id=int(employer), client_id=int(client)))
        db.session.commit()
        return db.session.query(db.func.max(Order.id)).first()
    except SQLAlchemyError as e:
        logger.error(e.args)
        return False


def getById(order_id):
    try:
        return Order.query.get(int(order_id))
    except:
        return False


def update_order(order_id, status, total_value, notes):
    try:
        data = Order.query.get(int(order_id))
        data.status = bool(status)
        data.total_value = float(total_value)
        data.notes = str(notes)
        db.session.add(data)
        db.session.commit()
        return True
    except:
        return False


def delete_order(order_id):
    try:
        data = Order.query.get(int(order_id))
        db.session.delete(data)
        db.session.commit()
        return True
    except:
        return False


def alter_active_state(id, state):
    try:
        data = Order.query.get(int(id))
        data.status = state
        db.session.add(data)
        db.session.commit()
        return True
    except SQLAlchemyError as e:
        logger.error(e.args)
        return False
