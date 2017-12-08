def p1(filename):
    with open(filename, 'r') as f:
        txt = f.read()
        return txt.count('(') - txt.count(')')

def p2(filename):
    with open(filename, 'r') as f:
        txt = f.read()
        print(txt)
        index = 0
        total = 0
        while True:
            if txt[index] == '(':
                total += 1
            else:
                total -= 1
            if total < 0:
                break
            index += 1
        return index + 1

#res = p1('input-day1.txt')
res = p2('input-day1.txt')
print(res)

