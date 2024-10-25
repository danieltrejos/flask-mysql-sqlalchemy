from . import db
from sqlalchemy.sql import func


class Usuario(db.Model):
    __tablename__ = 'Usuarios'
    idUsuario = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombreCompleto = db.Column(db.String(100), nullable=False)
    direccion = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.String(12), nullable=False)
    correo = db.Column(db.String(45), nullable=False)
    fechaRegistro = db.Column(db.DateTime, nullable=False, default=func.now())

    prestamos = db.relationship('Prestamo', backref='usuario', lazy=True)

    def __repr__(self):
        return f'<Usuario {self.nombreCompleto}>'

class Libro(db.Model):
    __tablename__ = 'Libros'
    codigo = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.String(45), nullable=False)
    titulo = db.Column(db.String(45), nullable=False)
    autor = db.Column(db.String(45), nullable=False)
    anoPublicacion = db.Column(db.Date, nullable=False)
    editorial = db.Column(db.String(45), nullable=False)
    categoria = db.Column(db.String(45), nullable=False)
    estado = db.Column(db.Enum('Devuelto', 'Prestado'), nullable=False)

    prestamos = db.relationship('Prestamo', backref='libro', lazy=True)

    def __repr__(self):
        return f'<Libro {self.titulo}>'

class Prestamo(db.Model):
    __tablename__ = 'Prestamos'
    idPrestamo = db.Column(db.Integer, primary_key=True)
    fechaPrestamo = db.Column(db.Date, nullable=False)
    fechaDevolucion = db.Column(db.Date, nullable=False)
    idUsuario = db.Column(db.Integer, db.ForeignKey('Usuarios.idUsuario'), nullable=False)
    codigo = db.Column(db.Integer, db.ForeignKey('Libros.codigo'), nullable=False)

    def __repr__(self):
        return f'<Prestamo {self.idPrestamo}>'
