from flask import Flask, send_from_directory, render_template, jsonify
import text_parser as tp
import os

app = Flask(__name__, static_url_path='')

@app.route('/cartas')
def parse_all_cards():
    return jsonify(tp.parse_cards())

@app.route('/reglas')
def agricola_rules():
    return send_from_directory(os.getcwd(), 'agricola_rules.pdf')

@app.route('/carta/<card_nr>')
def get_card(card_nr):
    #card=tp.get_card(card_nr)
    #return render_template('card.html', **locals())
    return jsonify(tp.get_card(card_nr))

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=8888)