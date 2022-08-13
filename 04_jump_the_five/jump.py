#!/usr/bin/env python3
"""
Author : Austinito
Date   : 2022-08-13
Purpose: Obfuscate numbers
"""

import argparse


JUMPER = {
        '1': '9',
        '2': '8',
        '3': '7',
        '4': '6',
        '5': '0',
        '6': '4',
        '7': '3',
        '8': '2',
        '9': '1',
        '0': '5'
        }


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
            description='Jump the Five',
            formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('positional', metavar='str', help='Input text')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    pos_arg: str = args.positional

    res = ''
    for char in pos_arg:
        res += JUMPER[char] if char.isdigit() else char

    print(res)


# --------------------------------------------------
if __name__ == '__main__':
    main()
