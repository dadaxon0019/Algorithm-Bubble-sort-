def digit(n):
    return [int(i) for i in str(n)[::-1]]

res = digit((14234234))
print(res)
