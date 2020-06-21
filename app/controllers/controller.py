from werkzeug.security import check_password_hash

from app import app
from app.dao import *
from app.dao import Adress, Employer
from app import db
from flask import render_template, redirect, request, flash, url_for
from validate_docbr import CPF
from datetime import datetime
import bcrypt
import time


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        cpf = request.form.get('cpf')
        password = request.form.get('password')

        user = Employer.get_employer_by_username(cpf)

        if not user or not check_password_hash(user.password, password):
            flash('Please check your login details and try again.')
            return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    elif request.method == 'POST':
        name = request.form.get('name')
        cep = request.form.get('cep')
        adress = request.form.get('adress')
        cpf = request.form.get('cpf')
        bdate = request.form.get('bdate')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        cpf_validator = CPF()

        if cpf_validator.validate(cpf):
            bdate = datetime.strptime(bdate, '%Y-%m-%d')
            adress_id = Adress.insert_adress(name=adress, cep=cep)

            if password1 != password2:
                flash('Senhas digitadas invalidas!')
                return redirect('/register')
            else:
                hashed_pwd = bcrypt.hashpw(password=password1.encode('utf-8'), salt=bcrypt.gensalt())
                Employer.insert_employer(name=name, cpf=cpf, birth_date=bdate, adress=adress_id, password=hashed_pwd)
                flash('Funcionario cadastrado com sucesso!')
                return redirect('/login')
        else:
            flash('CPF Digitado invalido')
            return redirect('/register')
