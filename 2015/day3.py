def part1(instructions):
    last_house = (0, 0)
    houses = []
    houses.append(last_house)
    for instruction in instructions:
        if instruction == '<':
            mov = (0, -1)
        elif instruction == '>':
            mov = (0, 1)
        elif instruction == '^':
            mov = (1, 0)
        elif instruction == 'v':
            mov = (-1, 0)
        last_house = (last_house[0] + mov[0], last_house[1] + mov[1])
        if not last_house in houses:
            houses.append(last_house)
    return len(houses)


def part2(instructions):
    pos_santa = (0, 0)
    pos_robot = (0, 0)
    houses = []
    houses.append(pos_santa)

    for index, instruction in enumerate(instructions):
        if instruction == '<':
            mov = (0, -1)
        elif instruction == '>':
            mov = (0, 1)
        elif instruction == '^':
            mov = (1, 0)
        elif instruction == 'v':
            mov = (-1, 0)

        if index % 2 == 0:  # Santa
            pos_santa = (pos_santa[0] + mov[0], pos_santa[1] + mov[1])
            if not pos_santa in houses:
                houses.append(pos_santa)
        else:  # Robot
            pos_robot = (pos_robot[0] + mov[0], pos_robot[1] + mov[1])
            if not pos_robot in houses:
                houses.append(pos_robot)
    return len(houses)


for instructions, res in [('>', 2), ('^>v<', 4), ('^v^v^v^v^v', 2)]:
    sol = part1(instructions)
    assert sol == res


for instructions, res in [('^v', 3), ('^>v<', 3), ('^v^v^v^v^v', 11)]:
    sol = part2(instructions)
    assert sol == res


with open('input-day3.txt', 'r') as f:
    instructions = f.read()

print('PART 1', part1(instructions))
print('PART 2', part2(instructions))
