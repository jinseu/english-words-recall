#!/usr/bin/env python

import argparse
import word
from exercise import word_ch_select


def parse():
    parser = argparse.ArgumentParser()
    parser.parse_args()
    parser.add_argument(
        "-m", "--mode", default="en2ch-select",
        choices=['en2ch'], help="recall mode")
    parser.add_argument(
        "-f", "--file", default="./data/data.csv", help="data file path")
    parser.add_argument(
        "-c", "--count", default=10, type=int, help="recall count")
    return parser.parse_args()


def main():
    args = parse()
    words = word.load_words(args.file)
    if args.mode == "en2ch-select":
        word_ch_select(words, args.count)
    else:
        raise Exception("not support mode {}".format(args.mode))


if __name__ == '__main__':
    main()
