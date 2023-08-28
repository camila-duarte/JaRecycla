from flask_sqlalchemy import SQLAlchemy

# inicializamos la extension SQLAlchemy = todo lo que esta en mi clase pertenece a SQLAlchemy
db = SQLAlchemy()


# definimos la clase en nuestra base de datos
class Personas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cedula = db.Column(db.Integer, nullable=False)
    punto = db.Column(db.Integer, nullable=False)

    def __init__(self, cedula, punto):
        self.cedula = cedula
        self.punto = punto

