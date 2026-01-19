from math import sqrt, sin

x = .1
y = 5*x + 3*x**2 * sqrt(1 + sin(x) ** 2)
print(y)
