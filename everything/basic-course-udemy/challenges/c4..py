def countries(country):

    paises_capitais = {
        "Brasil": "Brasília",
        "Japão": "Tóquio",
        "Estados Unidos": "Washington, D.C.",
        "França": "Paris",
        "Alemanha": "Berlim",
        "Itália": "Roma",
        "Canadá": "Ottawa",
        "Austrália": "Camberra",
        "China": "Pequim",
        "Índia": "Nova Delhi",
        "Rússia": "Moscou",
        "Argentina": "Buenos Aires",
        "México": "Cidade do México",
        "Reino Unido": "Londres",
        "Espanha": "Madri",
        "Portugal": "Lisboa",
        "África do Sul": "Pretória (executiva), Cidade do Cabo (legislativa), Bloemfontein (judiciária)",
        "Coreia do Sul": "Seul",
        "Tailândia": "Bangkok",
        "Egito": "Cairo"
    }
    
    return paises_capitais[country]
    

i = input("Digite o país pra saber a capital ")

print(countries(i))