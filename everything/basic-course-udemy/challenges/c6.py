calculo_loko = lambda x: x*10 if x < 2 else (x**2 if x < 4 else x+10)
print(calculo_loko(2))

even_or_odd = lambda x: "par" if x % 2 == 0 else "impar"
print(even_or_odd(3))
# (atribuição) se (isso no if)
# else (atribuição)
# no if a atribuição vem antes da condição
# no else, a atribuição vem depois