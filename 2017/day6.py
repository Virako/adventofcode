def p(filename):
    with open(filename, 'r') as f:
        lista = f.read().split('\t')
        lista = list(map(lambda x: int(x), lista))
        #lista = [0, 2, 7, 0]  # example
        len_list = len(lista)

        memory = []  # saved previous generated list

        counter = 0
        while not lista in memory:
            memory.append(lista[:])
            
            win = max(lista)
            index = lista.index(win)
            lista[index] = 0

            for i in range(index, index + win):
                lista[(i + 1) % len_list] += 1

            counter += 1
    return counter, len(memory) - memory.index(lista)


sol = p('input-day6.txt')
print('parte 1: {0}. parte 2: {1}'.format(*sol))
