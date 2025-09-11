a, b = 1, 3

while True:
    b -= 1
    a -= b
    if b <= 0:
        break

print(a, b)

while a <= 8:
    a += 2
    b -= 3

print(a, b)
