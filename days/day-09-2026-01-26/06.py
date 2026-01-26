print(ord("А"))  # 1040
print(ord("Ё"))  # 1040

for n in range(1040, 1040+32):
    print(n, chr(n), n+32, chr(n+32))
