def paint_wall(h: float, w: float) -> None:
    # mostrar opções q eu possa pintar
    cores = {
        "rosa": 10,
        "azul": 19,
        "verde": 12,
        "amarelo": 3,
        "vermelho": 4
    }
    # rosa consegue pintar 10m^2

    total : int = h*w

    for k, v in cores.items(): # isso acessa tanto chave quanto valor no python
        print(f"Para a cor {k}, você precisaria de {total/(int(v))} latas de tinta")


h : float = int(input("Diga a altura da parede: \n"))
w : float = int(input("Dita a largura da parede: \n"))

paint_wall(h, w)