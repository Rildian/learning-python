from pathlib import Path, PurePosixPath, PureWindowsPath

FILEPATH = Path("learning-python\\everything\\basic-course-udemy\\basics\\text.txt")

FILEPATH_WINDOWS = PureWindowsPath(FILEPATH)
FILEPATH_NOTWINDOWS = PurePosixPath(FILEPATH)

print(FILEPATH)
print(FILEPATH_WINDOWS)
print(FILEPATH_NOTWINDOWS)

with open(FILEPATH, "w") as arq:
    arq.writelines("aaaaaaaaaaaa")



# agr deu certo, veja q segue o diretorio do proprio repositorio, parte do
# learning-python -> até ai, não depende de C:\\, D:// e etc