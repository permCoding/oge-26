r = 2 * 32_000 * 16 * 147  # bit
print(r / 8 / 1024)  # 18375

r1 = 2 * 48_000 * 24 * (8*60+32)  # bit
r2 = 1 * 32_000 * 16 * (8*60+32)  # bit
r2 = r2 * 0.66
print( (r1-r2) / 8 / 2**20 )

from math import log2, ceil


print( log2(555) )
print( ceil( log2(555) ) )
