#!/usr/bin/python3
# -*- coding: utf-8 -*-

import re

def main():
    with open('./calibration-document.txt') as file:
        lines = file.readlines()
    res = 0
    for l in lines:
        digits = re.findall('[0-9]', l)
        res += int(f'{digits[0]}{digits[-1]}')
    print(f'The sum of all of the calibration values is {res}')

if __name__ == '__main__':
    main()