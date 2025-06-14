from flask import Flask ,render_template






app=Flask(__name__)



@app.route('/')
def home():
    return "soy la ruta raiz"



@app.route('/register')
def mostrar_register():
    return "soy la ruta register"



@app.route('/login')
def mostrar_login():
    return "soy la ruta login"




@app.errorhandler(404)
def not_faound(mensaje):
    return render_template ('NotFound.html'),404







if __name__=="__main__":
    app.run(debug=True,host='0.0.0.0')