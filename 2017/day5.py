def part1():
    with open('input-day5.txt', 'r') as f:
        lines = f.readlines()
        target = list(map(lambda x: int(x), lines))

        steps = 0
        index = 0
        while index >= 0 and index <= len(target):
            try:
                current_instruction = target[index] * 1
            except IndexError:
                print(steps)
                break
            target[index] += 1
            index += current_instruction
            steps += 1


def part2():
    with open('input-day5.txt', 'r') as f:
        lines = f.readlines()
        target = list(map(lambda x: int(x), lines))

        steps = 0
        index = 0
        while index >= 0 and index <= len(target):
            try:
                current_instruction = target[index] * 1
            except IndexError:
                print(steps)
                print(target)
                break
            target[index] += -1 if current_instruction >= 3 else 1
            index += current_instruction
            steps += 1

#part1()
part2()
