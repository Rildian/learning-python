def teste(name, qnt=4):
    print(f"hello {name}, i havve {qnt} legs.")

print(teste("joao")) # => hello joao i have 4 legs, default argument
print(teste("ed", 8)) # => hello ed i have 8 legs now the argument isnt default anymore, it is nondefault

# something interesting is that default cant be after non default argument

#def teste2(name='n', qnt):
    #print(f"hello {name} i have {qnt} legs") 

# print(teste2()) # SyntaxError: non-default argument follows default argument

def teste3(qnt, name="n"): # now i can use this
    print(f"hello {name} i have {qnt} legs")

teste3(3)


