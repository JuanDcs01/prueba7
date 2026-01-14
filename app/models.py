from app import db

class Celular(db.Model):
    __tablename__ = 'celulares'

    id = db.Column(db.Integer, primary_key=True)
    marca= db.Column(db.String, nullable=False)
    modelo = db.Column(db.String, nullable=False)
    anio = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<datos {self.id} {self.marca} {self.modelo} {self.anio}>'
    
    def __init__(self, marca, modelo, anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio