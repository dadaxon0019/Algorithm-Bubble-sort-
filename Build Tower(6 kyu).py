#Long method
def tower_builder(n_floors):
    res = []
    for i in range(n_floors):
        asterisks = "*" * (2 * i + 1)
        if i+1 != len(range(n_floors)):
            res.append(' ' * (n_floors - i - 1) + asterisks + ' ' * (n_floors - i - 1))
        else:
            res.append(asterisks)
    return res
res = tower_builder(3)
print(res)

#Short method
def tower_builder(n):
    return [("*" * (i*2-1)).center(n*2-1) for i in range(1, n+1)]
res1 = tower_builder(3)
print(res1)