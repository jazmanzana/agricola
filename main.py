from flask import Flask
import text_parser as tp

app = Flask(__name__)

@app.route('/cartas')
def parse_all_cards():
    return tp.parse_cards()

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=80)