from sqlalchemy.dialects.postgresql.psycopg2 import logger
from sqlalchemy.exc import SQLAlchemyError

from app.models.model import Client
from app import db


def getAll():
    try:
        return Client.query.all()
    except SQLAlchemyError as e:
        logger.error(e.args)
        return False


def getByCPF(cpf):
    try:
        return Client.query.filter(Client.cpf == str(cpf)).first()
    except SQLAlchemyError as e:
        logger.error(e.args)
        return False


def insert_client(name, cpf, birth_date, adress):
    try:
        db.session.add(Client(name=str(name), cpf=str(cpf), birth_date=birth_date, adress_id=str(adress[0])))
        db.session.commit()
    except SQLAlchemyError as e:
        logger.error(e.args)
        return False


def getById(client_id):
    try:
        return Client.query.get(int(client_id))
    except SQLAlchemyError as e:
        logger.error(e.args)
        return False


def update_client(client_id, name, cpf, birth_date, adress_id):
    try:
        data = Client.query.get(int(client_id))
        data.name = str(name)
        data.cpf = str(cpf)
        data.birth_date = str(birth_date)
        data.fk_adress_id = int(adress_id)
        db.session.add(data)
        db.session.commit()
        return True
    except SQLAlchemyError as e:
        logger.error(e.args)
        return False


def delete_client(client_id):
    try:
        data = Client.query.get(int(client_id))
        db.session.delete(data)
        db.session.commit()
        return True
    except SQLAlchemyError as e:
        logger.error(e.args)
        return False
