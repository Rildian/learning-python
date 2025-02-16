import math

soma = lambda x: x + 10 # a lambda function
# you use a certain amount of arguments and then you call everyone 

print(soma(2)) # need to pass this argument

soma2 = lambda x,y: x + y + 10

print(soma2(2, 3)) # x,y called


def funcao(x : int) -> int:
    teste = lambda x: x * 2 # you need to associate to a variable
    teste2 = lambda x: x + pow(x,2)
    teste3 = teste(x) + teste2(x) # i need to get the result, like the f(x)
    return teste3

print(funcao(2))

