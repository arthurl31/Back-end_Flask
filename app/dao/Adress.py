from sqlalchemy.dialects.postgresql.psycopg2 import logger
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import func

from app.models.model import Adress
from app import db


def getAll():
    try:
        return Adress.query.all()
    except:
        return False


def insert_adress(name, cep):
    try:
        db.session.add(Adress(id=None, nome_endereco=str(name), cep=str(cep)))
        db.session.commit()
        return db.session.query(db.func.max(Adress.id)).first()
    except:
        return False


def getById(adress_id):
    try:
        return Adress.query.get(int(adress_id))
    except:
        return False


def update_adress(adress_id, name, cep):
    try:
        data = Adress.query.get(int(adress_id))
        data.nome_endereco = str(name)
        data.cep = str(cep)
        db.session.add(data)
        db.session.commit()
        return True
    except:
        return False


def delete_adress(adress_id):
    try:
        data = Adress.query.get(int(adress_id))
        db.session.delete(data)
        db.session.commit()
        return True
    except SQLAlchemyError as e:
        logger.error(e.args)
        return False
