from sys import getsizeof

lista = ['abacata', 'Rildian', 'The Mr N', 'Stardew Valley']
#newlist = [expression for item in iterable if condition == True]
lista2 = [x for x in lista if 'R' in x]
print(lista2)
lista3 = [x for x in lista if 'a' not in x]
print(lista3)
lista4 = [x for x in range(10)] # the append is not necessary
print(lista4)
# the values are increased ten by ten
lista5 = [x for x in range(0, 101, 10)]
# generation expressions
lista6 = (x for x in range(0, 101, 10))
print(lista5)
print(getsizeof(lista6)) # 104 -> the value is going to bem permantely 104
print(getsizeof(lista5)) # 184 holy fuck

lista5 = [x for x in range(0, 1000, 10)]
lista6 = (x for x in range(0, 1000, 10))

print(getsizeof(lista6)) # 104, its a generator
print(getsizeof(lista5)) # 920



