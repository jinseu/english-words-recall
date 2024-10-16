#!/usr/bin/env python

import csv

from .word import Word


def load_words(filename):
    res = []
    with open(filename, newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            label = row.get('标签', '')
            labels = label.split(';')
            comment = row.get('备注', '')
            comments = comment.split(';')
            if len(row['含义']) == 0:
                raise Exception('word is not correct', row)
            res.append(Word(row['单词'], row['含义'], labels, comments))
    return res
