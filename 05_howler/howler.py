#!/usr/bin/env python3
"""
Author : austinherrera <austinherrera@localhost>
Date   : 2022-08-13
Purpose: Transform text into UPPERCASE message.
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Howler (upper-cases input)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('input',
                        metavar='str',
                        help='Input string or file')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='str',
                        type=str,
                        default='')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """And it begins..."""

    args = get_args()
    command_input = args.input
    output_file = args.outfile

    input_string_or_file = ""
    if os.path.isfile(command_input):
        input_string_or_file = open(command_input, 'r').read().rstrip()
    else:
        input_string_or_file += command_input

    if output_file:
        out_fh = open(output_file, 'wt')
        out_fh.write(input_string_or_file.upper())
    else:
        print(input_string_or_file.upper())


# --------------------------------------------------
if __name__ == '__main__':
    main()
