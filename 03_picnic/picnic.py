#!/usr/bin/env python3
"""
Author : Austinito
Date   : 2022-08-06
Purpose: Correcly format the items we're taking on our picnic.
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Picnic game',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('items',
                        metavar='str',
                        nargs='+',
                        help='Item(s) to bring')

    parser.add_argument('-s',
                        '--sorted',
                        help='Sort the items',
                        action='store_true',
                        )

    return parser.parse_args()


# --------------------------------------------------
def mk_string_with_oxford_comma(items: list[str]):
    """Combines a list of strings with oxford comma rules"""
    if len(items) > 1:
        last = items.pop()
        if len(items) > 1:
            return ', '.join(items) + ', and ' + last
        return ''.join(items) + ' and ' + last
    return ''.join(items)


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    items = args.items

    if args.sorted:
        items.sort()

    pretty_items = mk_string_with_oxford_comma(items)

    print(f'You are bringing {pretty_items}.')


# --------------------------------------------------
if __name__ == '__main__':
    main()
