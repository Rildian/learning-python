from array import array


letters = array('u', ['a', 'b', 'c'])
print(letters)

# each array has your type, instead of using 'int', 'float' to determine the type of your array
# python relies on using only one letter

integers = array('I', [1, 2, 3, 4])
print(integers)

tupla = ('a', 'b', 'c')
tupla *=2
print(tupla) # ... why can do that?
# oh, now thats interesting
tupla3 = (1, 2, 3)
print(id(tupla3)) # id is 2524089117632
tupla3 *= 3 
print(id(tupla3)) # id is 2541297481232

list3 = [1, 2, 3]
print(id(list3)) # id is 2348013283328
list3 *= 3 
print(id(list3)) # id is 2075343678208

# its different tuples and its the same list
