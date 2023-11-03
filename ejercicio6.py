from flask import Flask, request
app = Flask(__name__)
@app.route('/temperatura/')
def iva():
    celsius = float(request.args.get('celsius', -999))

    if celsius == -999:
        error = f'<h2>Se debe introducir un valor en Celsius.</h2>'
        return error
    else:

        resultado = celsius + 32
        cadena = f'<h2>En grados Farenheit es: {resultado}</h2>'
        return cadena
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)