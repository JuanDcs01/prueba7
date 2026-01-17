from flask import Blueprint, render_template, request, redirect, url_for, flash
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
    año = request.form['año']

    celular = Celular(marca=marca, modelo=modelo, año=año)

    db.session.add(celular)
    db.session.commit()

    flash("nuevo dispositivo añadido")

    return redirect(url_for('inicio.index'))

@others.route('/eliminar/<int:id>')
def eliminar(id):
    celular = Celular.query.get_or_404(id)
    db.session.delete(celular)
    db.session.commit()

    flash("dispositivo eliminado")
    return redirect(url_for('inicio.index'))

@others.route('/editar/<int:id>', methods=['POST', 'GET'])
def editar(id):

    celular = Celular.query.get_or_404(id)

    if request.method == 'POST':
        celular.marca = request.form['marca']
        celular.modelo = request.form['modelo']
        celular.año = request.form['año']

        db.session.commit()
        flash("dispositivo editado")
        return redirect(url_for('inicio.index'))


    return render_template('editar.html', celular=celular)

@others.route('/info/<int:id>')
def info(id):

    celular = Celular.query.get_or_404(id)
    return render_template('info.html', celular=celular)