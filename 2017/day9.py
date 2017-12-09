def count_groups(stream):
    is_garbage = False
    ignore = False
    depth = 0
    groups = 0
    garbages = 0

    for char in stream:
        if ignore:
            ignore = False
            continue
        if char == '!':
            ignore = False if ignore else True
        elif is_garbage:
            if char == '>':
                is_garbage = False
            else:
                garbages += 1
        elif char == '{':
            depth += 1
        elif char == '}':
            groups += depth
            depth -= 1
        elif char == '<':
            is_garbage = True

    return (groups, garbages)

assert count_groups('{}') == (1, 0)
assert count_groups('{{{}}}') == (6, 0)
assert count_groups('{{},{}}') == (5, 0)
assert count_groups('{{{},{},{{}}}}') == (16, 0)
assert count_groups('{<a>,<a>,<a>,<a>}') == (1, 4)
assert count_groups('{{<ab>},{<ab>},{<ab>},{<ab>}}') == (9, 8)
assert count_groups('{{{}},{<ab>},{<ab>},{<ab>}}') == (12, 6)
assert count_groups('{{<ab>{}},{<ab>},{<ab>},{<ab>}}') == (12, 8)
assert count_groups('{{<!!>},{<!!>},{<!!>},{<!!>}}') == (9, 0)
assert count_groups('{{<a!>},{<a!>},{<a!>},{<ab>}}') == (3, 17)
assert count_groups('{{<<<<<>}}') == (3, 4)


with open('input-day9.txt', 'r') as f:
    print('(PART1, PART2)',  count_groups(f.read()))

