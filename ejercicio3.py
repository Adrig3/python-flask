from flask import Flask, request
app = Flask(__name__)
@app.route('/inicio/')
def inicio():
    valor = request.args.get('valor', 'Valor por defecto')
    cadena = f'El valor inicial es {valor}'
    return cadena

@app.route('/', methods=['GET', 'POST'])
def root():
    return """
    <p>Copia y pega:
    <br>localhost:5000/inicio/?valor=300
"""
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)