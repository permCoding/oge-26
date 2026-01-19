N = 83
K = 1

D = 0
while K <= N:
    if N % K == 0:
        D = D + 1
    K = K + 1

if D == 2:
    print(N, "- простое")
else:
    print(N, "- составное")
