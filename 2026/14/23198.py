for x in range(1, 3000):
    n = 9**150 + 9**30 - x
    k = 0
    while n > 0:
        if n%9 == 0: k += 1
        n //= 9
    if k == 122:
        print(x)  # 81 <== это ответ
        break
