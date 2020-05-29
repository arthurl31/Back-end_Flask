from app.models.model import Product
from app import db


def getAll():
    try:
        return Product.query.all()
    except:
        return False

def insert_product(name_product, value, quantity, add_by, add_at=False):
    try:
        db.session.add(Product(product_name=str(name_product), product_value=float(value), available_quantity=int(quantity), add_by=int(add_by)))
        db.session.commit()
    except:
        return False

def getById(id_product):
    try:
        return Product.query.get(int(id_product))
    except:
        return False

def update_product(id_product, name_product, value, quantity, add_by, add_at=False):
    try:
        data = Product.query.get(int(id_product))
        data.product_name = str(name_product)
        data.product_value = float(value)
        data.available_quantity = int(quantity)
        data.add_by = int(add_by)
        data.add_at = str(add_at)
        db.session.add(data)
        db.session.commit()
        return True
    except:
        return False

def delete_product(id_product):
    try:
        data = Product.query.get(int(id_product))
        db.session.delete(data)
        db.session.commit()
        return True
    except:
        return False