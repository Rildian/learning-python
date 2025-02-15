value = 30

if 25 <= value < 40: # and you only use it once
    print("It works!")
else:
    print("it doesnt.") 

#FANTASTICO PARA F A N T A S T I C O

s = 'FANTASTICO'

for space in s:
    print(f"{space} """, end="") # end="" prevents the line break

print("\n")

for i in range(1, 7):
    print("*"*i) # lol

def mymax(a,b):
    return a if a > b else b # ternary operator lol

print(max(3, 5))

