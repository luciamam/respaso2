from flask_wtf import FlaskForm
from wtforms import  StringField,SubmitField,EmailField,PasswordField
from wtforms.validators import DataRequired ,Email, Length,EqualTo,ValidationError


class RegisterFrom(FlaskForm):
    name=StringField("introude un nombre de usuario",validators=[DataRequired(),Length(min=4,max=12)])
    email=EmailField("introduce un correo electronico",validators=[DataRequired(),Length(min=20,max=30),Email()])
    password=PasswordField("escribe una contraseña",validators=[DataRequired(),Length(min=4,max=12),EqualTo("confirm")])
    confirm=PasswordField("repite la contrseña",validators=[DataRequired(),Length(min=4,max=12)])
    submit=SubmitField("Registrarse")



class LoginFrom(FlaskForm):

    email=EmailField("introduce un correo electronico",validators=[DataRequired(),Length(min=20,max=30),Email()])
    password=PasswordField("escribe una contraseña",validators=[DataRequired(),Length(min=4,max=12)])
    
    submit=SubmitField("Inicia Sesion")
