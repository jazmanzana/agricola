#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json

def parse_cards():
    return json.dumps(get_all_cards())

def get_all_cards():
    text = copy_text()
    text_without_escapes = eliminate_scapes(text)
    return cards_to_dict(text_without_escapes)

def copy_text():
    path = "{}/karten.txt".format(os.getcwd())
    f = open(path,'r')
    text = f.readlines()
    f.close()
    return text

def eliminate_scapes(text):
    text_without_escapes = []
    for line in text:
        line = line[:-1]
        text_without_escapes.append(line)
    return text_without_escapes

def cards_to_dict(text):
    all_cards = {}
    new_card = 0
    for line in text:
        if line == "%%%":
            continue
        key_and_value = line.split("=")
        key = key_and_value[0]
        value = key_and_value[1]
        if key == "ID":
            new_card = value
            all_cards[new_card] = {}
            all_cards[new_card]["Deutsch"] = {}
            all_cards[new_card]["Español"] = {}
        else:
            if key in ["Name", "Art", "Spieler", "Komplexität", "Text", "Gewinn", "Anforderung", "Kosten"]:
                all_cards[new_card]["Deutsch"][key] = value
            else:
                all_cards[new_card]["Espanol"][key] = value
    return all_cards

def get_card(card):
    return json.dumps(get_all_cards().get(card))