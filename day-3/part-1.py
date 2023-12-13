#!/usr/bin/python3
# -*- coding: utf-8 -*-

import re
import sys

num_re = r'[0-9]+'
sym_re = r'[^.0-9\n]+'

def parse_lines(lines):
    numbers = []
    symbols = []
    for l in lines:
        line_numbers = []
        line_symbols = []
        for num in re.finditer(num_re, l):
            line_numbers.append((int(num.group()), num.span()))
        for sym in re.finditer(sym_re, l):
            line_symbols.append(sym.start())
        numbers.append(line_numbers)
        symbols.append(line_symbols)

    return numbers, symbols

def get_line_sum(numbers, prev_sym, cur_sym, next_sym):
    sym = set(prev_sym + cur_sym + next_sym)
    res = 0
    for num in numbers:
        indexes = num[1]
        start_i = max(0, indexes[0] - 1)
        end_i = indexes[1] + 1
        for i in range(start_i, end_i):
            if i in sym:
                res += num[0]
                break
    return res

def get_part_nums_sum(numbers, symbols):
    res = 0
    res += get_line_sum(numbers[0], [], symbols[0], symbols[1])
    res += get_line_sum(numbers[-1], symbols[-2], symbols[-1], [])
    for i in range(1, len(numbers) - 1):
        res += get_line_sum(numbers[i], *symbols[i-1:i+2])

    return res

def main(input_file):
    with open(input_file) as file:
        lines = file.readlines()

    nums, syms = parse_lines(lines)
    res = get_part_nums_sum(nums, syms)

    print(f'The sum part numbers is {res}')

if __name__ == '__main__':
    try:
        input_file = sys.argv[1]
    except IndexError:
        input_file = 'input.txt'

    main(input_file)