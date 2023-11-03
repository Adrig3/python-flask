from flask import Flask, request
app = Flask(__name__)
@app.route('/saludo/')
def saludo():
    nombre = request.args.get('nombre')
    cadena = "Hola, {}!".format(nombre)
    return cadena
if __name__ == '__main__':
    app.run(port=5000)