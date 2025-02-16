list_test = ['aaa', 1, 2, {'opa': 1}]
print(list_test[-1]) # the last element (the dict)
print(list_test[-2]) # second to last (2)

list_test.append('ablueblue')
print(list_test) # added as the lastest element 

list_test.insert(0, '1st element') # we gave the position and the element you want to add
print(list_test) 

list_test.remove(1) # search for the 1 and removes it, but what if
print(list_test)

for i in range(2):
    list_test.append(1)
list_test.remove(1)
print(list_test) # yeah, only remove the 1st 1 that i encounters

list_test.pop(1) # this is the index, the 'removes' is the element itself  
print(list_test)

print(f"the number 1 appeared {list_test.count(1)} time(s)!")

list_test.clear() # removes everything, similar to [:]
print(list_test)

lista1 = [{1:2}, {3:4}, {5,6}, {7,8}]
lista2 = ['1', '2', '3']
lista2.extend(lista1) # remembers the extend in oo? exactly.
print(lista2) 
lista3 = lista1
print(f"original: {lista1}")
print(f"copy: {lista3}")
print(lista1 == lista3) # does it copy the memory address?
lista3[0] = 'ive changed'

print(f"original: {lista1[0]}") 
print(f"copy: {lista3[0]}")
# yeah, it does copy the memory adress

# a way to copy without changing the old list is:

lista4 = ['howdy doo', 'hello', 'hello mr n']
lista4 = lista3.copy()
print(f"this is the 4th list: {lista4}")
print(lista3 == lista4) # they compare the elements, not the memory adress. Interesting.
lista4[0] = 'Hello World'
print(f"list 3: {lista3}")
print(f"list 4: {lista4}")

lista4 += lista3
print(lista4)

lista4 = lista3 + lista1 # concatenation
print(lista4)

item1, item2, item3, *items = lista4 # it associates w/ each index. Carefully not to have index out of range
print(f"1st item i guess {item1}")
print(f"2nd item i guess {item2}")
print(f"3rd item i guess {item3}")
print(f"the rest {items}")

item1, item2, *items, item3  = lista4 
print(f"1st item i guess {item1}")
print(f"2nd item i guess {item2}")
print(f"the rest in the middle {items}") # basically, it didnt pick elements from the item1, item2 and the last elements
print(f"supposed to be the last i guess {item3}") # it picked the last element

print("\n")

item1, *items, item2, item3  = lista4
print(f"1st item i guess {item1}")
print(f"the middle on 2nd position {items}")
print(f"the rest in the middle {item2}") 
print(f"supposed to be the last i guess {item3}") 
#essentialy, the xargs doesnt pick the previously element chosed, then, if we have more elements
#after the xargs variable, then, the number of elements the xargs will pick:
#amount_xargs = 
# total_elements - [(amount elements the 1st variable picked) + (amount elements of the variables after xargs)] 

colors = ['blue', 'red', 'yellow', 'brown']
numbers = [0, 1, 2, 3, 4]
i_Want = 'blue'

print("there it is") if i_Want in colors else print("nooo")
# true if else false (tipo assim)

print(list('banana')) # i guess its same thing to do w/ for i in 'banana' lista.append(i)
zip_result = []
zip_result = zip(colors, numbers)
print(list(zip_result)) # interesting, the element that doesnt have correspondency doesnt appear