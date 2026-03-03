k = int(input())

mx = 0
for i in range(k):
    n = int(input())
    if n%5 == 0:
        if n > mx:
            mx = n

print(mx)

"""
цикл
ветвление
остаток от деления

3
25
10
12

"""