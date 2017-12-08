
# PART 1
def part1():
    valids = 0
    invalids = 0
    with open('input-day4.txt', 'r') as f:
        for line in f.readlines():
            lista = line.split()
            if len(lista) == len(set(lista)):
                valids += 1
            else:
                invalids += 1
    print(valids, invalids)

# PART 2
def part2():
    valids = 0
    invalids = 0
    with open('input-day4.txt', 'r') as f:
        for line in f.readlines():
            lista = line.split()
            lista_sort = list(map(lambda x: "".join(sorted(x)), lista))
            if len(lista_sort) == len(set(lista_sort)):
                valids += 1
            else:
                invalids += 1
    print(valids, invalids)

#part1()
part2()
