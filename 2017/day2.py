def get_div_result(line):
    for val1 in line:
        for val2 in line:
            if val1 == val2:
                continue
            if val1 % val2 == 0:
                break
        if val1 % val2 == 0:
            break
    print("VALS", val1, val2)
    if val1 % val2 != 0:
        return 0
    return val1 // val2 if val1 > val2 else val2 // val1
        

def func(lines, res=0):
    res1 = 0
    res2 = 0

    for line in lines:
        res1 += max(line) - min(line)
        if res == 1:
            continue
        res2 += get_div_result(line)

    print(res1, res2)
    if res == 1:
        return res1
    elif res == 2:
        return res2
    else:
        return res1, res2

example = [[5, 1, 9, 5], [7, 5, 3], [2, 4, 6, 8]]
assert func(example, 1) == 18

example = [[5, 9, 2, 8], [9, 7, 4, 3], [3, 8, 6, 5]]
assert func(example, 2) == 9


with open("input-day2.txt", "r") as f:
    lines = []
    for line in f.readlines():
        lines.append(list(map(lambda x: int(x), line.split("\t"))))

print('PART1: {0}. PART2: {1}'.format(*func(lines)))
