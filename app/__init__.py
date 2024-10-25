from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

load_dotenv()
db = SQLAlchemy()

def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)

    # Imprimir la URI de la base de datos para verificar
    print('Base de datos:', app.config['SQLALCHEMY_DATABASE_URI'])

    # Inicializar la base de datos con la aplicación
    db.init_app(app)

    # Importar modelos dentro de la función para evitar circularidad
    with app.app_context():
        from . import models

    # Registrar blueprints
    from .usuarios.routes import usuarios_bp
    app.register_blueprint(usuarios_bp)

    # Importar rutas mediante blueprint
    from .routes import main
    app.register_blueprint(main, url_prefix='/')

    return app
