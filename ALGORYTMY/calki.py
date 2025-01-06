def function(x):
    return x*x+1
def calki(a, b, skala = 1000):
    x = (b-a)/skala
    pole = 0
    for i in range(skala):
        y = function(a+i*x)
        pole += y*x
    return pole
print(calki(1,3))