from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, TextAreaField, ValidationError
from wtforms.validators import EqualTo, DataRequired

from miappflask.models import User


class RegisterForm(FlaskForm):
    username = StringField('Usuario', validators=[DataRequired()])
    password = PasswordField('Contraseña', validators=[DataRequired(),
                                                     EqualTo('password2',
                                                             message='Las contraseñas deben coincidir.')])
    password2 = PasswordField('Confirmar Contraseña', validators=[DataRequired()])
    submit = SubmitField('Registrarse')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Nombre de usuario ya está en uso.')



class LoginForm(FlaskForm):
    username = StringField('Usuario', validators=[DataRequired()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    submit = SubmitField('Iniciar Sesión')



class AddArticuloForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired()])
    description = TextAreaField('Descripción', validators=[DataRequired()])
    submit = SubmitField('Guardar')



class UpdateArticuloForm(FlaskForm):
    name = StringField('Nuevo Nombre', validators=[DataRequired()])
    description = TextAreaField('Nueva Descripción', validators=[DataRequired()])
    submit = SubmitField('Modificar')