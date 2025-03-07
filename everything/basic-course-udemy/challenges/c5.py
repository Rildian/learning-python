def dobro(x: int) -> int:
    return x*2

def quadrado(x: int) -> int:
    x = dobro(x)
    return x**2

def tudo(x: int) -> int:
    dobro = lambda y: y*2
    quadrado = lambda y: y**2
    x = dobro(x)
    x = quadrado(x)
    return x

print(quadrado(2))
print(tudo(2))
cubo = lambda x: x**3
multi = lambda x,y: x*y
print(cubo(3))
print(multi(2,5))