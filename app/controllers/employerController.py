from flask_login import login_user, login_required, logout_user
from flask_login import current_user
from app.dao import Adress, Employer
from app import app, db, login_manager
from flask import render_template, redirect, request, flash, url_for
from validate_docbr import CPF
from datetime import datetime
import bcrypt


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        if not current_user.is_authenticated:
            return render_template('login.html')
        else:
            return redirect(url_for('home'))
    elif request.method == 'POST':
        if not current_user.is_authenticated:
            cpf = request.form.get('cpf')
            password = request.form.get('password')

            user = Employer.get_employer_by_username(cpf)

            if not user or not bcrypt.checkpw(password=password.encode('utf-8'),
                                              hashed_password=str(user.password).encode('utf-8')):
                flash('Please check your login details and try again.')
                return redirect(url_for('login'))
            else:
                login_user(user)
                return redirect('home')
        else:
            return redirect('home')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        if not current_user.is_authenticated:
            return render_template('register.html')
        else:
            return redirect(url_for('home'))
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


@app.route('/home', methods=['GET'])
@login_required
def home():
    return render_template('home.html')


@app.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    redirect(url_for('login'))