from flask import request
from app.forms.LoginForm import LoginForm
from app import app
from flask import render_template
from flask import redirect


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        form = LoginForm()
        return render_template('login.html', context={'form': form})
    else:
        form = LoginForm(request.form)
        if form.validate():
            pass
        else:
            return 'not valid'
