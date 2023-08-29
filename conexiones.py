# importamos librerias
from flask import Flask
from modelo import db

# creamos una instancia de la aplicacion Flask
app = Flask(__name__)

# conectamos base de datos con el programa configurando el URL de la base de datos
# el .db = database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///personas_registradas.db"

# inicia la extension SQLALCHEMY en la app Flask
db.init_app(app)

# aseguramos que las operaciones se hagan de manera correcta bajo el contexto de Flask
with app.app_context():
    db.create_all()