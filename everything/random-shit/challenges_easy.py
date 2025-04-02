def missingNumber(lista: list) -> int:
    for i in range(1, len(lista)+1):
        if i+1 not in lista:
            return (i+1)
    return None
        

#lista = [1, 2, 3, 4, 5, 6, 7, 9] # 8
#print(missingNumber(lista))

def maiorDiff(lista: list) -> int:
    biggest = lista[0]
    lowest = lista[0]

    for x in lista:
        if x > biggest:
            biggest = x
        if x < lowest:
            lowest = x
    
    return (biggest-lowest)



# lista = [5, 10, 20, 15, 30]
# print(maiorDiff(lista))

def online_count(status: dict) -> int:
    count = 0
    for x in status.values(): # acessar os values das keys
        if x == "online":
            count += 1
    return count


status = { "Alice": "online", "Bob": "offline", "Eve": "online", }

print(online_count(status))
