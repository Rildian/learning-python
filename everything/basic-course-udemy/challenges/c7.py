dobro = lambda x: x*2
lista = [1, 2, 3, 4]
print(list((map(dobro, lista)))) # map faz um for embutido pelo que entendi, tem q converter dps

quadrado = lambda y: y**2
print(list(map(quadrado, lista)))