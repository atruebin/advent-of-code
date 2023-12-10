#!/usr/bin/python3
# -*- coding: utf-8 -*-

import re
import math

colors = (
    'red',
    'green',
    'blue'
)

color_re = '|'.join(colors)
cube_re = rf'([0-9]+) ({color_re})'

def main():
    with open('./game-recordings.txt') as file:
        lines = file.readlines()
    res = 0
    for l in lines:
        _, game_data = l.split(': ')
        cubes = re.findall(cube_re, game_data)
        max_count = {color: 0 for color in colors}
        for cube in cubes:
            max_count[cube[1]] = max(max_count[cube[1]], int(cube[0]))
        res += math.prod(max_count.values())

    print(f'The sum of power of the set of each game is {res}')

if __name__ == '__main__':
    main()
