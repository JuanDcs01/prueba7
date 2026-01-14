from flask import Blueprint, render_template
from app.models import Celular

inicio = Blueprint('inicio', __name__)

@inicio.route('/')
def index():
    celulares = Celular.query.all()
    return render_template('index.html', celulares=celulares)