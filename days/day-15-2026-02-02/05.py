# позиции внутри строки начинаются с нуля

s = input("Введите целое число - ")  # ______

res = 0
for x in s:
    res = res + int(x)
print(res)


"""
res = 0
res = res + 1  # 0 + 1 = 1
res = res + 1  # 1 + 2 = 3
"""
