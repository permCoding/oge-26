n = int(input())  # 1417

k = 0
while n > 0:
    # 
    if n % 10 == 1:
        k += 1
    n //= 10
print(k)


# print(1417 % 10)  # 7
# print(141 % 10)  # 1
# print(14 % 10)  # 4
# print(1 % 10)  # 1


