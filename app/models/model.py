from datetime import datetime

from app import db


class Order(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    order_date = db.Column(db.DateTime, nullable=False, default=datetime.now)
    status = db.Column(db.Boolean, nullable=False, default=False)
    total_value = db.Column(db.Float, nullable=False)
    notes = db.Column(db.String(255), nullable=True)
    fk_client_id = db.Column(db.ForeignKey('clients.id'))
    fk_employer_id = db.Column(db.ForeignKey('employers.id'))

    client = db.relationship('Client', foreign_keys=fk_client_id)
    fk_employer_id = db.relationship('Employer', foreign_keys=fk_employer_id)

    def __init__(self, order_date, status, total_value):
        self.order_date = order_date
        self.status = status
        self.total_value = total_value

    def __repr__(self):
        return "Order ID: " + self.id


class Client(db.Model):
    __tablename__ = 'clients'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    cpf = db.Column(db.String(11), nullable=False)
    birth_date = db.Column(db.Date, nullable=False)

    def __init__(self, name, cpf, birth_date):
        self.name = name
        self.cpf = cpf
        self.birth_date = birth_date

    def __repr__(self):
        return "Client Name: " + self.name


class Employer(db.Model):
    __tablename__ = 'employers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    cpf = db.Column(db.String(11), nullable=False)
    birth_date = db.Column(db.Date, nullable=False)
    entry_date = db.Column(db.Date, nullable=False, default=datetime.utcnow())
    is_active = db.Column(db.Boolean, nullable=False, default=1)
    is_admin = db.Column(db.Boolean, nullable=False, default=0)
    is_super = db.Column(db.Boolean, nullable=False, default=0)

    def __init__(self, name, cpf, birth_date):
        self.name = name
        self.cpf = cpf
        self.birth_date = birth_date

    def __repr__(self):
        return "Employer Name: " + self.name


class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100), nullable=False)
    product_value = db.Column(db.Float, nullable=False)
    available_quantity = db.Column(db.Integer, nullable=False)
    add_by = db.Column(db.ForeignKey('employers.id'))
    add_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())

    client = db.relationship('Employer', foreign_keys=add_by)

    def __init__(self, product_name, product_value, available_quantity, add_by):
        self.product_name = product_name
        self.product_value = product_value
        self.available_quantity = available_quantity
        self.add_by = add_by

    def __repr__(self):
        return "Product id: " + self.id
