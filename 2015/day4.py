from hashlib import md5


def func(secret_key, startswith='00000'):
    x = 0
    while 1:
        m = md5()
        m.update('{0}{1}'.format(secret_key, x).encode('utf-8'))
        if m.hexdigest().startswith(startswith):
            break
        x += 1
    return x

assert func('abcdef') == 609043
assert func('pqrstuv') == 1048970

print('PART1, PART2', func('yzbqklnj'), func('yzbqklnj', '000000'))
