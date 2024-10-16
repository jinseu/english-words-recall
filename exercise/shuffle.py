#!/usr/bin/env python

import random


def shuffle_words(words):
    size = len(words)
    i = 0
    while i < size:
        n = random.randint(0, size-1)
        words[n], words[i] = words[i], words[n]
        i += 1
