from flask import render_template, redirect, request, flash, url_for
from flask_login import current_user
from flask_login import login_required

from app import app
from app.dao import Order, Product


@app.route('/addorder', methods=['GET', 'POST'])
@login_required
def addorder():
    if request.method == 'GET':
        return render_template('generate_order.html', context={'products': Product.getAll()})
    else:
        return redirect(url_for('allproducts'))
