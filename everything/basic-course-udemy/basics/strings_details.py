string = """
Does it work?

"""
print(string) # it does!


#slicing
string = "Hello World"
print(string[0:3]) # it excludes the 3rd element
print(string[3:10]) # it iniciantes from the 3rd (counting 0-3) and again, it excludes the last
print(string[-1]) # i got the last one lol
print(string[::]) # prints everything
print(string[-3:-1]) # it kinda does -3 + 2, but again, it excludes the last, so it'll print rl
print(string[::-1]) # it inverts the string
print(string[:len(string)]) # prints everything
print(string[0:10:4]) # it jumps 4 to for, actually, it was supposed to get the 9th element, but since jumps 4, then it only gets until the 8th element
print(string[1:0]) # where am i going?
print(string[0::-1]) # theres nowhere that i can go. The 3rd element is to increment