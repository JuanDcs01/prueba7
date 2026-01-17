from app import db
from flask_sqlalchemy import SQLAlchemy
import enum
from sqlalchemy import Enum

# Tabla intermedia para la relación Muchos a Muchos
compatibilidades = db.Table('celulares_accesorios',
    db.Column('idcelular', db.Integer, db.ForeignKey('celulares.idcelular'), primary_key=True),
    db.Column('idaccesorio', db.Integer, db.ForeignKey('accesorios.idaccesorio'), primary_key=True)
)

class Marca(db.Model):
    __tablename__ = 'marcas'
    idmarca = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    pais_origen = db.Column(db.String(50), nullable=False)
    celulares = db.relationship('Celular', backref='marca_rel', lazy=True)

class Celular(db.Model):
    __tablename__ = 'celulares'
    idcelular = db.Column(db.Integer, primary_key=True)
    modelo = db.Column(db.String(50), nullable=False)
    año = db.Column(db.Integer)
    idmarca = db.Column(db.Integer, db.ForeignKey('marcas.idmarca'), nullable=False)
    
    # Relaciones
    imei = db.relationship('Imei', backref='celular_rel', uselist=False)
    accesorios = db.relationship('Accesorio', secondary=compatibilidades, backref='celulares_compatibles')

class Imei(db.Model):
    __tablename__ = 'imei' # Cambiado de 'especificaciones' para mayor claridad
    idimei = db.Column(db.Integer, primary_key=True)
    numero_imei = db.Column(db.BigInteger, nullable=False, unique=True) # BigInteger es vital aquí
    idcelular = db.Column(db.Integer, db.ForeignKey('celulares.idcelular'), unique=True)

class TipoAccesorio(enum.Enum): # Clase en mayúscula por convención
    sonido = "sonido"
    bateria = "bateria"
    proteccion = "proteccion"

class Accesorio(db.Model):
    __tablename__ = 'accesorios'
    idaccesorio = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    tipo = db.Column(db.Enum(TipoAccesorio), nullable=False)
    