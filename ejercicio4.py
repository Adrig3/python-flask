from flask import Flask, request
app = Flask(__name__)
@app.route('/convierte/')
def convierte():
    dolares = float(request.args.get('dolares', 1))
    resultado = dolares * 1.2
    cadena = f'<h2>En euros son: {resultado}</h2>'
    return cadena
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)