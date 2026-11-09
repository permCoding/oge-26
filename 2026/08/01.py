s = "ЛЕГКО"
k = 0
for s1 in s:
  for s2 in s:
    for s3 in s:
      for s4 in s:
        for s5 in s:
          for s6 in s:
            lst = [s1, s2, s3, s4, s5, s6]
            u1 = s1 != "Г"
            u2 = lst.count("О") <= 1
            u3 = s6 != "Е" and s6 != "О"
            if u1 and u2 and u3:
              k += 1
print(k)


from itertools import product

n = 0
for w in product("ЕИОРТЯ", repeat=6):
  n += 1
  if w[0] not in "РТЯ" and w.count("И") >= 2:
    if n%2 != 0:
      print(n, w)  # 23159