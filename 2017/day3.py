# 17  16  15  14  13
# 18   5   4   3  12
# 19   6  _1_  2  11
# 20   7   8   9  10
# 21  22  23  24  25

target = 289326

def get_edges(jump, start, nums):
    step = nums / 4
    res = []
    centered = jump // 2 - 1
    for x in range(4):
        res.append(start + centered + x * step)
    print(res)
    return res


total = 1
ini = 0

for jump in range(3, 1025, 2):
    ini += 1
    start = total + 1
    nums = jump * 2 + (jump - 2) * 2
    total += nums
    #print(total, ini)

    if total > target:
        # sides: 
        edges = get_edges(jump, start, nums)
        extra = min(map(lambda x: abs(target - x), edges))
        print("SOL para {0} es {1}".format(target, ini + extra))
        break

