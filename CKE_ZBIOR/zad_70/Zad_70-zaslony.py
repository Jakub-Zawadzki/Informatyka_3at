gorny_y = 19 + 61/125
dolny_y = -32 -2/3
lewy_x = 2



# prawy_X = calki

def f(x):
    return x * x + 1

a = 0
b = 4
n = 1000
dx = (b - a) / n
pole = 0

for i in range(n):
    x = a + i * dx
    y = f(x)
    pole += y * dx

print(pole)