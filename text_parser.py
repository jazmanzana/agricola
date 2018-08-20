#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

def parse_cards():
    return get_all_cards()

def get_all_cards():
    return cards_to_dict(copy_text())

def copy_text():
    path = "{}/karten.txt".format(os.getcwd())
    f = open(path,'r', encoding="utf-8")
    text = f.read()
    f.close()
    return text

def cards_to_dict(text):
    all_cards = {}
    new_card = 0
    cards = text.split("%%%")
    for card in cards:
        lines = card.split("\n")
        for line in lines:
            if not line:
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
                    all_cards[new_card]["Español"][key] = value
    return all_cards

def get_card(card):
    return get_all_cards().get(card)