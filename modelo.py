from flask_sqlalchemy import SQLAlchemy

# inicializamos la extension SQLAlchemy = todo lo que esta en mi clase pertenece a SQLAlchemy
db = SQLAlchemy()


# definimos la clase en nuestra base de datos
class Personas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cedula = db.Column(db.Integer, nullable=False)
    punto = db.Column(db.Integer)

    def __init__(self, cedula):
        self.cedula = cedula
        self.punto = 0
        
    def sumar_pts(self, punto):
        self.punto += punto
        
    def restar_pts(self, punto):
        self.punto -= punto

