from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

import os

#Dirección de la Bd en nuestra carpeta de la app
dbdir = "sqlite:///" + os.path.abspath(os.getcwd()) + "database/users.db"

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = dbdir
db = SQLAlchemy(app)

#Primera ruta 'index.html'
@app.route("/")
def index():
    return render_template("index.html")

#Ruta para ver el listado de usuarios
@app.route("/users/list")
def listado():
	return render_template("listado.html")