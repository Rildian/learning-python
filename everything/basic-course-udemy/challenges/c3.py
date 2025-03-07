frutas = [
    "maçã", "banana", "laranja", "uva", "morango", 
    "abacaxi", "melancia", "mamão", "kiwi", "pêssego",
    "pera", "limão", "tangerina", "goiaba", "maracujá",
    "ameixa", "framboesa", "manga", "abacate", "cereja"
]

for i in range(len(frutas)):
    for j in range(i+1, len(frutas)):
        print(f"{frutas[i]} com {frutas[j]}")





