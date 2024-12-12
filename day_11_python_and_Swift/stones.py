#!/usr/bin/env python3

stones = [5, 62914, 65, 972, 0, 805922, 6521, 1639064]

blinks = 25

working_stones = []

for i in range(blinks):
    for index, stone in enumerate(stones):
        if stone == 0:
            working_stones.append(1)

        elif len(str(stone)) % 2 == 0:
            stone_string = str(stone)
            cut_point = len(stone_string) // 2
            working_stones.append(int(stone_string[0:cut_point]))
            working_stones.append(int(stone_string[cut_point:]))

        else:
            working_stones.append(stone * 2024)

    stones = working_stones
    working_stones = []


print(len(stones))
