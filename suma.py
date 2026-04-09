from flask import Flask, request
app = Flask(_name_)
@app.route('/suma')
def suma():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    if a is None or b is None:
        return "Parámetros faltantes: 'a' o 'b'", 400
    return str(a + b)
