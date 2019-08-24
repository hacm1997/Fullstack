from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

import os

dbdir = "sqlite:///" + os.path.abspath(os.getcwd()) + "database/users.sql"

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = dbdir
db = SQLAlchemy(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/listado.html")