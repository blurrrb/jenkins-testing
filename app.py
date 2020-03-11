from flask import Flask, request
app = Flask(__name__)

from lib import power, mod_inverse

@app.route('/')
def hello_world():
   return 'Hello World'

@app.route('/pow')
def pow():
    x = int(request.args.get('x'))
    y = int(request.args.get('y'))
    m = int(request.args.get('m'))
    return str(power(x, y, m))

@app.route('/modinv')
def modinv():
    a = int(request.args.get('a'))
    m = int(request.args.get('m'))
    return str(mod_inverse(a, m))


if __name__ == '__main__':
   app.run()