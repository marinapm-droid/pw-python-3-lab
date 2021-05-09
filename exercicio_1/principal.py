import analisa_ficheiro
import json

def main():
    nome_json = analisa_ficheiro.gera_nome()    
    nome_ficheiro = nome_json.split(".")
    file = open(nome_json, "a")
    file.write(analisa_ficheiro.calcula_linhas(nome_ficheiro[0]+".txt")+"\n")
    file.write(analisa_ficheiro.calcula_carateres(nome_ficheiro[0]+".txt")+"\n")
    file.write(analisa_ficheiro.calcula_palavra_comprida(nome_ficheiro[0]+".txt")+"\n")
    file.write(str(analisa_ficheiro.calcula_ocorrencia_de_letras(nome_ficheiro[0]+".txt")))
    file.close()

if __name__ == "__main__": 
    main()