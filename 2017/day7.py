from anytree import Node, RenderTree

nodes = []

def get_index_node(name):
    try:
        return [n.name[0] for n in nodes].index(name)
    except ValueError:
        return

def get_total_weigth(node):
    total = 0
    if node.children:
        total += sum([child.name[1] for child in node.children])
        for child in node.children:
            total += get_total_weigth(child)
    return total

def get_unbalanced(node):
    res = {}
    for c in node.children:
        name, w = c.name
        res[name] = w + get_total_weigth(c)

    stack = list(res.values())

    try:
        v1, v2 = list(set(stack))
    except ValueError:
        return

    if stack.count(v1) == 1:
        problem = v1
        diff = v1 - v2
    else:
        problem = v2
        diff = v2 - v1

    res_units = -1
    for key, value in res.items():
        if problem == value:
            res_units = nodes[get_index_node(key)].name[1] - diff
            break

    return get_unbalanced(nodes[get_index_node(key)]) or res_units

def treed(lines):
    index = 0
    for line in lines:
        parent = None
        name, leftovers = line.split(' (')
        weigth = int(leftovers.split(')')[0])
        if line.find('->') != -1:
            children = line.split('-> ')[1].split(',')
            children = list(map(lambda x: x.strip(), children))
        else:
            children = []

        index_node = get_index_node(name)
        if index_node is not None:
            node = nodes[index_node]
            node.name = (name, weigth)
        else:
            node = Node((name, weigth))
            nodes.append(node)
            index += 1

        for child in children:
            index_node = get_index_node(child)
            if index_node is not None:
                node_child = nodes[index_node]
                node_child.parent = node
            else:
                node_child = Node((child, -1), parent=node)
                nodes.append(node_child)
                index += 1

    print(len(nodes))
    root = nodes[0].root

    for pre, fill, node in RenderTree(root):
        print("%s%s" % (pre, node.name[0]))

    unbalanced = get_unbalanced(root)

    return root.name[0], unbalanced


lista = """pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)""".split('\n')


assert treed(lista) == ('tknk', 60)

nodes = []
with open('input-day7.txt', 'r') as f:
    lines = f.readlines()
    print("part1: {0}. part2: {1}".format(*treed(lines)))
