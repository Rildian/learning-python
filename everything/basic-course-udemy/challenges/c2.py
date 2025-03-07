
def sql(funcionarios: list, turno_dia: list, turno_noite: list, tem_carro: list) -> list:
    # Lista1: tem carro e trabalha a noite
    # Lista2: tem carro e trabalha dia
    # Lista3: não tem carro

    Lista1 = []
    Lista2 = []
    Lista3 = []

    for i in funcionarios:
        if i in tem_carro and i in turno_noite:
            Lista1.append(i)
        if i in tem_carro and i in turno_dia:
            Lista2.append(i)
        if i not in tem_carro:
            Lista3.append(i)
    
    return Lista1, Lista2, Lista3





funcionarios = [
    "Ana Silva", "Bruno Costa", "Carla Mendes", "Diego Oliveira",
    "Elena Santos", "Fábio Rocha", "Gisele Lima", "Hugo Almeida", 
    "Igor Pereira", "Julia Carvalho"
]


turno_dia = [
    "Ana Silva",           
    "Bruno Costa",        
    "Carla Mendes",        
    "Diego Oliveira",      
    "Elena Santos"         
]


turno_noite = [
    "Elena Santos",       
    "Fábio Rocha",         
    "Gisele Lima",        
    "Hugo Almeida",        
    "Igor Pereira"         
]


tem_carro = [
    "Bruno Costa",         
    "Diego Oliveira",      
    "Hugo Almeida",        
    "Igor Pereira",        
    "Julia Carvalho"       
]

y = sql(funcionarios, turno_dia, turno_noite, tem_carro)
print(y)