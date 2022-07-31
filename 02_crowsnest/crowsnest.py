#!/usr/bin/env python3
"""
Author : Austinito <austinherrera@localhost>
Date   : 2022-07-31
Purpose: Shout whatever you see
"""

import argparse


VOWELS = ['a', 'e', 'i', 'o', 'u']


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Crow's Nest -- choose the correct article",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word', metavar='str', help='A word')

    return parser.parse_args()


# --------------------------------------------------
def get_correct_article(word: str):
    """Get correct article for given str"""
    return 'an' if word[0].lower() in VOWELS else 'a'


# --------------------------------------------------
def main():
    """Where it begins..."""

    args = get_args()
    word = args.word
    article = get_correct_article(word)
    print(f'Ahoy, Captain, {article} {word} off the larboard bow!')


# --------------------------------------------------
if __name__ == '__main__':
    main()
