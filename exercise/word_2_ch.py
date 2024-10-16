#!/usr/bin/env python

import random

from .shuffle import shuffle_words
from .util import single_select


def word_ch_select(words, count):
    shuffle_words(words)
    w_size = len(words)
    if count > w_size:
        count = w_size
    used = words[0:count]
    correct = 0
    mis = 0
    for item in used:
        r = random.randint(0, w_size-5)
        res = single_select([item.word, item.ch_meaning],
                            [w.ch_meaning for w in words[r:r+4]])
        if res:
            print("right")
            correct += 1
        else:
            print("mistake")
            mis += 1
        print('total: %d correct: %d not correct: %d' % (count, correct, mis))

