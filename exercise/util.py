#!/usr/bin/env python

import random


def str_select_input():
    while True:
        w = input('answer:')
        res = w.strip().lower()
        if len(res) > 1:
            print('input not correct')
        elif len(res) == 1:
            return ord(res[0]) - ord('a')


def single_select(correct_pair, in_corrects):
    print("%s" % (correct_pair[0]))
    i = 0
    k = random.randint(0, len(in_corrects)-1)
    for incorrect in in_corrects:
        no = chr(ord('a') + i)
        if i == k:
            print('%s: %s' % (no, correct_pair[1]))
        else:
            print('%s: %s' % (no, incorrect))
        i += 1
    answer = str_select_input()
    return answer == k

