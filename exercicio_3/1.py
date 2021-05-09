import os.path
import os

soma=0

def pede_pasta():
    while True:
        global path
        path=input("Insira o caminho para uma pasta: ")
        if os.path.isdir(path) == True:
            return path

def calcula_tamanho_pasta(pasta):

    soma = 0
    soma = os.path.getsize(pasta)

    for item in os.listdir(pasta):
        itempath = os.path.join(pasta, item)

        if os.path.isfile(itempath):
            print(item)
            soma += os.path.getsize(itempath)
            print(os.path.getsize(itempath)/1024)

        elif os.path.isdir(itempath):
            soma += calcula_tamanho_pasta(itempath)

    return soma/1024


print("O tamanho da pasta em MBytes é: "+str(calcula_tamanho_pasta(pede_pasta())))