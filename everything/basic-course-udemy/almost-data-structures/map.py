import math

def test():
    return lambda x: x**2
    
teste = test()
print(teste(math.sqrt(2)))
lista2 = [2823809, 329823, 3]
lista3 = map(test(), lista2)

print(list(lista3))
print(list(map(lambda x: x**2, [2823809, 329823, 3])))

lista = [1, 2, 3, 4, 10, 30, 40, 32089, 32, 32, 44]
def remove(x):
    return x > 20
# map basically transforms something into another thing, it's some sort of f(x)
# in this case, i'm picking every element and doing something
print(list(map(remove, lista))) # it returns boleean form
print(list(map(lambda x: x**2, lista))) #im picking each element and doind what this lambda does, its basically a for loop
print(list(filter(lambda x: x > 20, [1, 2, 3, 4, 10, 30, 40, 32089, 32, 32, 44]))) # returns the values

# entender melhor o map e filter
