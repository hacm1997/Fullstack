from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

import os

#Dirección de la Bd - Aún no configurada correctamente
dbdir = "sqlite:///" + os.path.abspath(os.getcwd()) + "database/users.sql"

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = dbdir
db = SQLAlchemy(app)

#Primera ruta 'index.html'
@app.route("/")
def index():
    return render_template("index.html")

#Ruta para ver el listado de usuarios
@app.route("/listado.html")