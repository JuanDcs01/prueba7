from flask import Blueprint, render_template,request, redirect, url_for
from app.models import Celular
from app import db

others = Blueprint('others', __name__)

@others.route('/agregar')
def agregar():
    return render_template('agregar.html')

@others.route('/guardar', methods=['POST'])
def guardar():
    marca = request.form['marca']
    modelo = request.form['modelo']
    anio = request.form['anio']

    celular = Celular(marca, modelo, anio)

    db.session.add(celular)
    db.session.commit()

    return redirect(url_for('inicio.index'))

# @others.route()
# def ():
#     return