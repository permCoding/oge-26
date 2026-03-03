k = int(input())

sm = 0
for i in range(k):
    n = int(input())
    if n%6 == 0:
        sm += n  # sm = sm + n

print(sm)

"""
цикл
ветвление
остаток от деления

3
25
10
12

sm //= n  # sm = sm // n
sm -= n
sm *= n
sm /= n
sm %= n

"""