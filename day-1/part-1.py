#!/usr/bin/python3
# -*- coding: utf-8 -*-

import re
import sys

def main(input_file):
    with open(input_file) as file:
        lines = file.readlines()
    res = 0
    for l in lines:
        digits = re.findall('[0-9]', l)
        res += int(f'{digits[0]}{digits[-1]}')
    print(f'The sum of all of the calibration values is {res}')

if __name__ == '__main__':
    try:
        input_file = sys.argv[1]
    except IndexError:
        input_file = 'input.txt'

    main(input_file)