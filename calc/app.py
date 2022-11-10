from flask import Flask, request
from operations import add, sub, mult, div
app = Flask(__name__)

@app.route('/add')
def add_params():
    """return params a + b """
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(add(a,b))

@app.route('/sub')
def sub_params():
    """return params a -b """
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(sub(a,b,))

@app.route('/mult')
def mult_params():
    """ return product of a * b """
    a = int(request.args.get("a"))
    b = int(request.args.get('b'))
    return str(mult(a,b))

@app.route('/div')
def div_params():
    """Return quotient of a / b """
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return str(div(a,b))
