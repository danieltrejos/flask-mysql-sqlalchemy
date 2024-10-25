from app import create_app, db

app = create_app('config.DevelopmentConfig')

with app.app_context():
    db.create_all()

# Verificar la URI de la base de datos
#print("Base de datos:", app.config['SQLALCHEMY_DATABASE_URI'])


if __name__ == '__main__':
    app.run(debug=True)