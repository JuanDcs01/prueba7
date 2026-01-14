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

@others.route('/eliminar/<int:id>')
def eliminar(id):
    celular = Celular.query.get_or_404(id)
    db.session.delete(celular)
    db.session.commit()
    return redirect(url_for('inicio.index'))

@others.route('/editar/<int:id>', methods=['POST', 'GET'])
def editar(id):

    celular = Celular.query.get_or_404(id)

    if request.method == 'POST':
        celular.marca = request.form['marca']
        celular.modelo = request.form['modelo']
        celular.anio = request.form['anio']

        db.session.commit()
        return redirect(url_for('inicio.index'))


    return render_template('editar.html', celular=celular)