from itertools import product

pos = 0
for combo in product("АЕКНТЦ", repeat=5):
    pos += 1
    if pos % 2 == 0:
        if combo[0] not in "АЕК":
            if combo.count("Т") >= 1:
                print(pos, *combo)
                break
print(int("30041", 5))
