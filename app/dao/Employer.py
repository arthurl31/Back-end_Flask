from app.models.model import Employer
from app import db


def getAll():
    try:
        return Employer.query.all()
    except:
        return False


def insert_employer(name, cpf, birth_date, adress):
    try:
        db.session.add(Employer(name=str(name), cpf=str(cpf), birth_date=birth_date, adress_id=int(adress)))
        db.session.commit()
    except:
        return False


def getById(employer_id):
    try:
        return Employer.query.get(int(employer_id))
    except:
        return False


# provavelmente criar novos metodos pra troccar apenas os valores boolean :)
def update_employer(employer_id, name, cpf, birth_date, fk_adress_id, is_active=True, is_admin=False,
                    is_super=False):
    try:
        data = Employer.query.get(int(employer_id))
        data.name = str(name)
        data.cpf = str(cpf)
        data.birth_date = str(birth_date)
        data.fk_adress_id = int(fk_adress_id)
        data.is_active = bool(is_active)
        data.is_admin = bool(is_admin)
        data.is_super = bool(is_super)
        db.session.add(data)
        db.session.commit()
        return True
    except:
        return False


def delete_employer(employer_id):
    try:
        data = Employer.query.get(int(employer_id))
        db.session.delete(data)
        db.session.commit()
        return True
    except:
        return False
