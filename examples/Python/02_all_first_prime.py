def get_first_del(n):
    d = 2
    while n % d > 0:
        d = d + 1
    return d

a = 12
while a > 1:
    d = get_first_del(a)
    print(d)
    a = a / d