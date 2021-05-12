def pede_nome()->"String":
    while True:
        nome = input("Insira um nome de um ficheiro de texto, com extensão .txt\n")
        try:
            open(nome, "r")
            for n in nome:
                if n == ".":
                    split = nome.split(".")
                    if split[1] == "txt":
                        return split[0]
                        exit()      
        except IOError:
            print("nono")

def gera_nome():
    nome_txt = pede_nome()
    return (nome_txt+".json")

pede_nome()

