def check_exp(value_register, op, num):
    if op == '<':
        return value_register < num
    elif op == '>':
        return value_register > num
    elif op == '<=':
        return value_register <= num
    elif op == '>=':
        return value_register >= num
    elif op == '==':
        return value_register == num
    elif op == '!=':
        return value_register != num

def func(lines):
    register = {}
    total_max = 0
    for line in lines:
        var, op, inc, _, exp_var, exp_op, exp_num = line.split()

        value_register = register.get(exp_var) or 0
        print(value_register)
        if check_exp(value_register, exp_op, int(exp_num)):
            inc = 1 * int(inc) if op == 'inc' else -1 * int(inc)
            if register.get(var):
                register[var] += inc
            else:
                register[var] = 1 * inc
            if register[var] > total_max:
                total_max = register[var]

    return max(register.values()), total_max


with open('input-day8-example.txt', 'r') as f:
    assert func(f.readlines())[0] == 1

with open('input-day8.txt', 'r') as f:
    print('(PART1, PART2)',  func(f.readlines()))
