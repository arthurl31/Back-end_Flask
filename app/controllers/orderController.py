from flask import render_template, redirect, request, flash, url_for, session
from flask_login import current_user
from flask_login import login_required
from app import app
from app.dao import Order, Product, Client
from validate_docbr import CPF


@app.route('/addorder', methods=['GET', 'POST'])
@login_required
def addorder():
    if request.method == 'GET':
        return render_template('generate_order.html', context={'products': Product.getAll()})
    else:
        return redirect(url_for('allproducts'))


@app.route('/endorder', methods=['POST'])
@login_required
def endorder():
    if 'cart' in session:
        cpf_validator = CPF()
        client_cpf = request.form.get('cpf')
        notes = request.form.get('notes')
        if not cpf_validator.validate(client_cpf):
            flash('CPF Invalido!')
            return redirect(url_for('mycart'))

        if Client.getByCPF(client_cpf):
            for i in session['cart']:
                for product_id, quantity in i.items():
                    current_product = Product.getById(int(product_id))
                    money_spend = (current_product.product_value * quantity)
                    return 'oi'
            # create relationship
        else:
            flash('CPF do Cliente não encontrado!')
            return redirect(url_for('mycart'))
    else:
        return redirect(url_for('home'))
