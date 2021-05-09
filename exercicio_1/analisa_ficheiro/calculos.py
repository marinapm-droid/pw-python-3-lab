def calcula_linhas(nome_ficheiro):
    try:
        file = open(nome_ficheiro,'r')
        count = 0
        content = file.read()
        content_split = content.split("\n")
        for i in content_split:
            if i:
                count+=1
        return "O número de linhas que o ficheiro tem é "+str(count)
    except OSError:
        print("Não conseguiu abrir/ler o ficheiro: ", nome_ficheiro)
        exit()

def calcula_carateres(nome_ficheiro):
    try:
        file = open(nome_ficheiro,'r')
        count = 0
        content = file.read()
        for i in content:
            count+=1
        return "O número de caracteres que o ficheiro tem é "+str(count)
    except OSError:
        print("Não conseguiu abrir/ler o ficheiro: ", nome_ficheiro)
        exit()

def calcula_palavra_comprida(nome_ficheiro):
    try:
        file = open(nome_ficheiro,'r')
        content = file.read()
        big_word=""
        for word in content.split():
            if len(word) > len(big_word):
                big_word=word
        return "A palavra mais comprida do ficheiro é "+ big_word
    except OSError:
        print("Não conseguiu abrir/ler o ficheiro: ", nome_ficheiro)
        exit()

def calcula_ocorrencia_de_letras(nome_ficheiro):
    dicionario={}
    try:
        file = open(nome_ficheiro,'r')
        content = file.read()
        for caracter in content:
            if caracter != "\n":
                if caracter in dicionario:
                    dicionario[caracter] += 1
                else:
                    dicionario[caracter] = 1
        return dicionario
    except OSError:
        print("Não conseguiu abrir/ler o ficheiro: ", nome_ficheiro)
        exit()
