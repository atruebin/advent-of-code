#!/usr/bin/python3
# -*- coding: utf-8 -*-

import re

cube_max_count = {
    'red': 12,
    'green': 13,
    'blue': 14
}

def check_excess(color: str, count: int):
    if count > cube_max_count[color]:
        return True
    return False

color_re = '|'.join(cube_max_count.keys())
cube_re = rf'([0-9]+) ({color_re})'

def main():
    with open('./game-recordings.txt') as file:
        lines = file.readlines()
    res = 0
    for l in lines:
        game, game_data = l.split(': ')
        cubes = re.findall(cube_re, game_data)
        for count, color in cubes:
            if check_excess(color, int(count)):
                break
        else:
            game_id = int(game.split(' ')[1])
            res += game_id

    print(f'The sum of IDs of possible games is {res}')

if __name__ == '__main__':
    main()