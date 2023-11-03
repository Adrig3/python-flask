from flask import Flask, request
app = Flask(__name__)
@app.route('/iva/')
def iva():
    euros = float(request.args.get('euros', 1))
    resultado = euros * ( 21 / 100)
    cadena = f'<h2>El IVA es: {resultado}</h2>'
    return cadena
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)