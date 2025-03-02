from another_package.find_index import findIndex
from module import *
import os
from pathlib import Path 

# lista = [1, 2, 3, 9]
# print(findIndex(lista, 9))

dir = "learning-python\everything\basic-course-udemy\oop\constructors.py" 
print(os.path.abspath(dir)) # get the absolute path

dir2 = "D:\learn-python\learning-python\everything\basic-course-udemy\os_module\module.py"
print(os.path.realpath(dir2))

DIR3 = "oop" # he identifies as a dir, huh, but it's better when the folder is the same level
print(os.path.abspath(DIR3))

DIR5 = "learning-python\\everything\\basic-course-udemy\\basics" # its kinda problematic
# it works on windows because im using backslashes \\, but what if its macos? linux?
lista = [x for x in os.listdir(DIR5) if x.endswith("py")]
print(lista)

DIR6 = os.path.dirname("oop")
print(DIR6)

OUTPUT = "learning-python\\everything\\basic-course-udemy\\os_module\\saida"

if not os.path.exists(OUTPUT):
    os.makedirs(OUTPUT)

with open (os.path.join(OUTPUT, "text.txt"), "a") as arq:
    arq.write("Hello World!")