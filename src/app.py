from flask import Flask ,render_template,request,redirect,url_for,flash
from  flask_bootstrap import Bootstrap4
from forms.forms import RegisterFrom,LoginFrom
from dotenv import load_dotenv
from pymongo import MongoClient
from werkzeug.security import generate_password_hash,check_password_hash

import os

load_dotenv()








app=Flask(__name__)
Bootstrap4(app)
app.config['SECRET_KEY']=os.getenv("SECRET_KEY")
client = MongoClient("mongodb://localhost:27017/")
db=client["RepasoJunio2025"]
usuarios=db["usuarios"]



@app.route('/')
def home():
    return "soy la ruta raiz"

@app.route('/register')
def mostrar_register():
    form=RegisterFrom()
    return render_template('Register.html',form=form)


@app.route('/register',methods=['POST'])
def registrarse():
    datos=request.form
    name=datos['name']
    email=datos['email']
    password=datos['password']
    #vamos a registrar al usuario en la basse de datos 
    dict_usuario={
        "name":name,
        "email":email,
        "password":generate_password_hash(password)
    }
    if  not db.usuarios.find_one({"email":email}):
    
        documento_usuario=usuarios.insert_one(dict_usuario)
        return redirect(url_for('perfil'))
    else:
        flash ("este usuario ya existe","info")
        return redirect(url_for("mostrar_register"))

@app.route('/login')
def mostrar_login():
    form=LoginFrom()
    return render_template('Login.html',form=form)

@app.route('/login', methods=['POST'])
def login():
    datos=request.form
    email_request=datos["email"]
    usuario=db['usuarios'].find_one({"email":email_request})
    if usuario:
        if check_password_hash(usuario["password"],datos["password"]):
            return redirect(url_for("perfil"))
        else:
            flash("contraseña incorrecta","warning")
            return redirect(url_for('mostrar_login'))
    else:
        
        flash("el usuario no existe","error")
        
        return redirect(url_for('mostrar_register'))


@app.route('/perfil')
def perfil():
    return "bienvenido a tu perfil"


@app.errorhandler(404)
def not_faound(mensaje):
    return render_template ('NotFound.html'),404







if __name__=="__main__":
    app.run(debug=True,host='0.0.0.0')