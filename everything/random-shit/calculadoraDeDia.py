from datetime import date

""""so funciona pra dd/mm/yy"""
"""uma missão seria fazer uma interface grafica"""


def calculadora(data1: str, dias: int) -> str:
    bissexto = ehBissexto(int(data1[6:10]))

    if not ehValido(data1) or dias < 0:
        return "Data inválida."
    

    meses = {
        1: 31,
        2: 29 if bissexto else 28,  
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }

    dia = int(data1[:2])
    mes = int(data1[3:5])
    ano = int(data1[6:10])

    if dias == 0:
        dia_semana = diaDaSemana(ano, mes, dia)
        data = f"dia: {dia_semana}, data: {dia}/{mes}/{ano}"
        
        return data


    for i in range(dias):
        
        max_dia = meses[mes]
        
        if dia == max_dia:
            dia = 1
            mes += 1
        else:
            dia += 1
        
        if mes > 12:
            ano += 1
            mes = 1
  
    dia_semana = diaDaSemana(ano, mes, dia)
    data = f"dia: {dia_semana}, data: {dia}/{mes}/{ano}"

    return data
    


def ehBissexto(ano : int) -> bool:
    if ano % 4 == 0 and ano % 100 != 0:
        return True
    return False

def ehValido(data) -> bool:
    dia_estranho = int(data[0:2])
    ano = int(data[6:10])

    if not ehBissexto(ano) and dia_estranho == 29:
        return False
    return True

def diaDaSemana(ano: int, mes: int, dia: int) -> str:
    dia = date(ano, mes, dia).weekday()

    dias_da_semana = {
    0: "segunda",
    1: "terça",
    2: "quarta",
    3: "quinta",
    4: "sexta",
    5: "sábado",
    6: "domingo"
    }

    return dias_da_semana[dia]



string = '21/03/2025'
dias = 45
print(calculadora(string, dias))