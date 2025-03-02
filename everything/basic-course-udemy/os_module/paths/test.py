path = "D://learn-python//learning-python//everything//basic-course-udemy//os_module//text.txt"
from to_import import disciplinas, notas
arquivo = open(path, "r")
print(arquivo.read())
arquivo.close() 

# now, if i use with open, it closes once you've done whatever you wanted to do

# with open(path, "r") as arq: # como ta usando nesse escopo, fica identado
#     print(arq.read())

# with open(path, "w") as arq2:
#     arq2.write("teste")
    # i dont need to use read this, basically it overwrites and then reads
    # it cleary has some kind of order

# with open(path, "a") as arq3:
#     arq3.writelines("\ncuteste")

content = ""
for i in range(5):
    content += f"Nota da discplina {disciplinas[i]} foi: {notas[i]}\n"

with open(path, "w") as arq5:
    arq5.writelines(content)

with open (path, "r") as arq6:
    arq6.read()

