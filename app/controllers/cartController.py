from flask import render_template, redirect, request, flash, url_for, session
from flask_login import current_user
from flask_login import login_required

from app import app
from app.dao import Order, Product


@app.route('/addtocard/<id>', methods=['GET', 'POST'])
@login_required
def addtocard(id):
    product = Product.getById(id)

    if 'cart' in session:
        if not any(product.product_name in d for d in session['cart']):
            session['cart'].append({str(product.name): 1})
    elif any(product.name in d for d in session['cart']):
        for d in session['cart']:
            d.update((k, request.form.get('quantity')) for k, v in d.items() if k == product.product_name)
    else:
        session['cart'] = [{product.name: 1}]

    return redirect(url_for('addorder'))


@app.route('/myccart', methods=['GET', 'POST'])
@login_required
def myccart():
    if 'cart' in session:
        return render_template('mycart.html', cart={'products': session['cart']})
    else:
        session['cart'] = {}
        return render_template('mycart.html', cart={'products': session['cart']})
