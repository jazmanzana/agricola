from flask import Flask
app = Flask(__name__)

@app.route('/franco')
def hello_world():
    return 'Hola, Franco!'

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=80)