from flask import Blueprint, render_template, request, url_for, redirect
from app.models import Usuario

usuarios_bp = Blueprint('usuarios', __name__)

# Ruta para listar todos los usuarios
@usuarios_bp.route('/usuarios')
def lista_usuarios():
    usuarios = Usuario.query.all()
    return render_template('usuarios/usuarios_list.html', usuarios=usuarios)

# Ruta para crear un nuevo usuario
@usuarios_bp.route('/usuarios/nuevo', methods=['GET', 'POST'])
@usuarios_bp.route('/usuarios/nuevo', methods=['GET', 'POST'])
def nuevo_usuario():
    if request.method == 'POST':
        nombre = request.form['nombreCompleto']
        direccion = request.form['direccion']
        telefono = request.form['telefono']
        correo = request.form['correo']
        fecha_registro = request.form['fechaRegistro']

        # Crear el nuevo usuario
        nuevo_usuario = Usuario(nombreCompleto=nombre,direccion=direccion,telefono=telefono,correo=correo,fechaRegistro=fecha_registro)
        
        # Agregarlo a la base de datos
        from app import db
        db.session.add(nuevo_usuario)
        db.session.commit()

        # Redireccionar a la lista de usuarios
        return redirect(url_for('usuarios.lista_usuarios'))
    
    # Mostrar el formulario si es una solicitud GET
    return render_template('usuarios/usuario_form.html')

# Ruta para editar un usuario
@usuarios_bp.route('/usuarios/<int:id>/editar', methods=['GET', 'POST'])
def editar_usuario(id):
    usuario = Usuario.query.get_or_404(id)
    if request.method == 'POST':
        usuario.nombreCompleto = request.form['nombreCompleto']
        usuario.direccion = request.form['direccion']
        usuario.telefono = request.form['telefono']
        usuario.correo = request.form['correo']
        from app import db  # Importar db dentro de la función
        db.session.commit()
        return redirect(url_for('usuarios.lista_usuarios'))
    
    return render_template('usuarios/usuario_form.html', usuario=usuario)

# Ruta para eliminar un usuario
@usuarios_bp.route('/usuarios/<int:id>/eliminar', methods=['POST'])
def eliminar_usuario(id):
    usuario = Usuario.query.get_or_404(id)
    from app import db  # Importar db dentro de la función
    db.session.delete(usuario)
    db.session.commit()
    return redirect(url_for('usuarios.lista_usuarios'))
