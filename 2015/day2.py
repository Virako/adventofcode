# PART 1 and 2

def get_sort_dimension(dim_str):
    """ Return l, w, h dimension. """
    return sorted(list(map(lambda x: int(x), dim_str.split('x'))))

def box(dimension):
    l, w, h = get_sort_dimension(dimension)
    return 2*l*w + 2*w*h + 2*h*l + l*w

def boxes(dimensions):
    return sum([box(d) for d in dimensions])

def ribbon(dimension):
    l, w, h = get_sort_dimension(dimension)
    return 2*l + 2*w + l*w*h

def ribbons(dimensions):
    return sum([ribbon(d) for d in dimensions])


# tests
assert box('2x3x4') == 58
assert box('1x1x10') == 43
assert boxes(['2x3x4', '1x1x10']) == 58 + 43

assert ribbon('2x3x4') == 34
assert ribbon('1x1x10') == 14
assert ribbons(['2x3x4', '1x1x10']) == 34 + 14


with open('input-day2.txt', 'r') as f:
    lines = f.readlines()
    print("part1:", boxes(lines))
    print("part2:", ribbons(lines))

