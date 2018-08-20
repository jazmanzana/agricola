from flask import Flask
import text_parser as tp
from flask import render_template


app = Flask(__name__)

@app.route('/cartas')
def parse_all_cards():
    return tp.parse_cards()

@app.route('/carta/<card_nr>')
def get_card(card_nr):
    card=tp.get_card(card_nr)
    return render_template('card.html', **locals())

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=8888)