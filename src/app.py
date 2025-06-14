from flask import Flask ,render_template,request,redirect,url_for
from  flask_bootstrap import Bootstrap4
from forms.forms import RegisterFrom
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
    documento_usuario=usuarios.insert_one(dict_usuario)
    return redirect(url_for('perfil'))



@app.route('/login')
def mostrar_login():
    return "soy la ruta login"



@app.route('/perfil')
def perfil():
    return "bienvenido a tu perfil"


@app.errorhandler(404)
def not_faound(mensaje):
    return render_template ('NotFound.html'),404







if __name__=="__main__":
    app.run(debug=True,host='0.0.0.0')