try:
    teste = [1, 2, 3, 4]
    print(teste[10])
except IndexError:
    print('Index inexistente')

try:
    right = int(input("type here mf "))
except ValueError:
    print('era pra ser um numero SEU JEGUE')



try:
    right = int(input("type here "))
except ValueError:
    print("numero pae")
finally:
    print(right)

def divide(x,y):
    try:
        result = x/y
    except ZeroDivisionError:
        print("tu dividiu por ZERO")
    else:
        print(f"Resultado: {result}")
    finally:
        print("isso é executado toda vez")


print(divide(2, 0))
