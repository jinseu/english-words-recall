#!/usr/bin/env python

import word
from exercise import word_ch_select


def main():
    words = word.load_words('./data/data.csv')
    word_ch_select(words, 10)


if __name__ == '__main__':
    main()
