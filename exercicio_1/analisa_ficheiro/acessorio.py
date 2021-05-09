def pede_nome()->"String":
    count=0
    while True:
        nome = input("Insira um nome de um ficheiro de texto, com extensão .txt\n")
        for n in nome:
            if n == ".":
                split = nome.split(".")
                if split[1] == "txt":
                    return split[0]
                    exit()            

def gera_nome():
    nome_txt = pede_nome()
    return (nome_txt+".json")

