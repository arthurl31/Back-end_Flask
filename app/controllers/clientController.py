from app import app
from flask import render_template


@app.route("/addclient")
def addclient():
    return render_template('login.html')


@app.route("/deleteclient/<id>")
def deleteclient():
    return "delete"


@app.route("/updateclient/<id>")
def updateclient():
    return "update"


@app.route("/seeclient/<id>")
def seeclient():
    return "seeclient"


@app.route("/seeallclient")
def seeallclient():
    return "seeallclient"
