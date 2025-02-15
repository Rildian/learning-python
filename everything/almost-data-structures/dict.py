# dict doesnt seem to have index, instead, you use their keys as an index

dictionary = {
    1:2, 
    'name':'Rildian', 
    'Age':21
}

print(dictionary[1]) # it shows the value of the key 1

dictionary.update({'name': 'Mr N', 1:69})
print(dictionary)

for i in dictionary: # its the same of dictionary.keys()
    print(i)

for i in dictionary.values():
    print(i)

for k, v in dictionary.items(): # ok
    print(k, v)
print(dictionary.get('name')) # gets the value of this key
print("\n")
print(dictionary.keys()) # it generantes a dict of keys
print(dictionary.values()) # it generates a dict of values