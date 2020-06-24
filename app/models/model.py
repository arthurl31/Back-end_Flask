from datetime import datetime

from app import db


class Order(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    order_date = db.Column(db.DateTime, nullable=False, default=datetime.now)
    status = db.Column(db.Boolean, nullable=False, default=True)
    total_value = db.Column(db.Float, nullable=False)
    notes = db.Column(db.String(255), nullable=True)
    fk_client_id = db.Column(db.ForeignKey('clients.id'))
    fk_employer_id = db.Column(db.ForeignKey('employers.id'))

    client = db.relationship('Client', foreign_keys=fk_client_id)
    employer = db.relationship('Employer', foreign_keys=fk_employer_id)

    def __init__(self, total_value, notes, client_id, employer_id):
        self.fk_client_id = client_id
        self.fk_employer_id = employer_id
        self.notes = notes
        self.total_value = total_value

    def __repr__(self):
        return "Order ID: " + self.id


class Client(db.Model):
    __tablename__ = 'clients'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    cpf = db.Column(db.String(20), nullable=False, unique=True)
    birth_date = db.Column(db.Date, nullable=False)
    fk_adress_id = db.Column(db.ForeignKey('adress.id', ondelete='CASCADE'))

    adress = db.relationship('Adress', foreign_keys=fk_adress_id)

    def __init__(self, name, cpf, birth_date, adress_id):
        self.name = name
        self.cpf = cpf
        self.birth_date = birth_date
        self.fk_adress_id = adress_id

    def __repr__(self):
        return "Client Name: " + self.name


class Employer(db.Model):
    __tablename__ = 'employers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    cpf = db.Column(db.String(20), nullable=False, unique=True)
    birth_date = db.Column(db.Date, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    entry_date = db.Column(db.Date, nullable=False, default=datetime.utcnow())
    is_active = db.Column(db.Boolean, nullable=False, default=1)
    is_admin = db.Column(db.Boolean, nullable=False, default=0)
    is_super = db.Column(db.Boolean, nullable=False, default=0)
    fk_adress_id = db.Column(db.ForeignKey('adress.id'))

    adress = db.relationship('Adress', foreign_keys=fk_adress_id)

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def __init__(self, name, cpf, birth_date, password, adress_id):
        self.name = name
        self.cpf = cpf
        self.birth_date = birth_date
        self.password = password
        self.fk_adress_id = adress_id

    def __repr__(self):
        return "Employer Name: " + self.name


class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100), nullable=False)
    product_value = db.Column(db.Float, nullable=False)
    available_quantity = db.Column(db.Integer, nullable=False)
    is_active = db.Column(db.Boolean, nullable=False, default=1)
    add_by = db.Column(db.ForeignKey('employers.id'))
    add_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())

    client = db.relationship('Employer', foreign_keys=add_by)

    def __init__(self, product_name, product_value, available_quantity, add_by):
        self.product_name = product_name
        self.product_value = product_value
        self.available_quantity = available_quantity
        self.add_by = add_by

    def __repr__(self):
        return "Product id: " + str(self.id)


class Adress(db.Model):
    __tablename__ = 'adress'
    id = db.Column(db.Integer, primary_key=True)
    nome_endereco = db.Column(db.String(80), nullable=False)
    cep = db.Column(db.String(80), nullable=False)

    def __init__(self, id, nome_endereco, cep):
        self.id = id
        self.nome_endereco = nome_endereco
        self.cep = cep


class Product_Order(db.Model):
    __tablename__ = 'list_product_order'
    id = db.Column(db.Integer, primary_key=True)
    fk_order_id = db.Column(db.ForeignKey('orders.id'))
    fk_product_id = db.Column(db.ForeignKey('products.id'))

    order = db.relationship('Order', foreign_keys=fk_order_id)
    product = db.relationship('Product', foreign_keys=fk_product_id)

    def __init__(self, order_id, product_id):
        self.fk_order_id = order_id
        self.fk_product_id = product_id
