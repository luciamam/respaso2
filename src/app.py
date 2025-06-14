from flask import Flask ,render_template
from  flask_bootstrap import Bootstrap4
from forms.forms import RegisterFrom
from dotenv import load_dotenv

import os

load_dotenv()








app=Flask(__name__)
Bootstrap4(app)
app.config['SECRET_KEY']=os.getenv("SECRET_KEY")



@app.route('/')
def home():
    return "soy la ruta raiz"



@app.route('/register')
def mostrar_register():
    form=RegisterFrom()
    return render_template('Register.html',form=form)



@app.route('/login')
def mostrar_login():
    return "soy la ruta login"




@app.errorhandler(404)
def not_faound(mensaje):
    return render_template ('NotFound.html'),404







if __name__=="__main__":
    app.run(debug=True,host='0.0.0.0')