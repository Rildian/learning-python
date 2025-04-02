
def escreva(input: str) -> str:
    newList = []

    for i in range(1, (len(input) +1)):
        newList.append(str(i))
    
    newList = str(newList)

    return ''.join(newList)

def diferente(input: str) -> int:
    listaAux = escreva(input)

    """ver melhor isso aki, complete o desafio""" 
    for i in zip(listaAux, input):
        if i in listaAux and not i in input:
            return input[i-1]

input = "1235678"
print(diferente(input))