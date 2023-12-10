#!/usr/bin/python3
# -*- coding: utf-8 -*-

import re

letter_digits = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

letter_re = '|'.join(letter_digits.keys())

def get_digit(digits, index):
    digit_str = digits[index]
    try:
        digit = int(digit_str)
    except ValueError:
        digit = letter_digits[digit_str]
    return digit

def main():
    with open('./calibration-document.txt') as file:
        lines = file.readlines()
    res = 0
    for l in lines:
        digits = re.findall(rf'(?=([0-9]|{letter_re}))', l)
        first = get_digit(digits, 0)
        last = get_digit(digits, -1)
        res += int(f'{first}{last}')
    print(f'The sum of all of the calibration values is {res}')

if __name__ == '__main__':
    main()