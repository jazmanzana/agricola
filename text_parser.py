#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

def parse_cards():
    text = copy_text()
    text_without_escapes = eliminate_scapes(text)
    separate_cards = cards_to_dict(text_without_escapes)
    return bytes(separate_cards)

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
        else:
            all_cards[new_card][key] = value
    return all_cards


