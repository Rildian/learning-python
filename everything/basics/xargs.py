def sum(*num): # i can receveie x parameters
    j = 0
    for i in num:
        j += i
    return j

print(sum(2, 3, 4, 5, 6))


def agencial(**car): # xargs and xparameters
    return car

print(agencial(marca='Gol', cor='Branca', motor=1.0)) # it creates a dictionary
