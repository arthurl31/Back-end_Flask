from flask import render_template, redirect, request, flash, url_for
from flask_login import current_user
from flask_login import login_required
from app import app
from app.dao import Client, Adress
from validate_docbr import CPF
from datetime import datetime


@app.route("/addclient", methods=['GET', 'POST'])
@login_required
def addclient():
    if request.method == 'GET':
        return render_template('add_client.html')
    else:
        name = request.form.get('ncliente')
        cep = request.form.get('cep')
        adress = request.form.get('adress')
        cpf = request.form.get('cpf')
        bdate = request.form.get('bdate')
        cpf_validator = CPF()

        if cpf_validator.validate(cpf):
            if Client.getByCPF(cpf) is None:
                bdate = datetime.strptime(bdate, '%Y-%m-%d')
                adress_id = Adress.insert_adress(name=adress, cep=cep)

                Client.insert_client(name=name, cpf=str(cpf), birth_date=bdate, adress=adress_id)
                flash('Cliente adicionado com sucesso!')
                return redirect(url_for('home'))
            else:
                flash('Cliente já existe')
                return redirect(url_for('home'))
        else:
            flash('CPF Digitado invalido')
            return redirect(url_for('addclient'))


@app.route("/allclientes", methods=['GET', 'POST'])
@login_required
def allclientes():
    return render_template('all_clientes.html', context={'clients': Client.getAll()})


@app.route('/deleteclient/<int:id>', methods=['GET'])
@login_required
def deleteclient(id):
    Client.delete_client(int(id))
    flash('Cliente ' + str(id) + ' Deletado com Sucesso')
    return redirect(url_for('allclientes'))
