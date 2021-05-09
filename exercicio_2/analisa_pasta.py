import os.path
import os
import csv
from matplotlib import pyplot as plt


path = ""
dicionario = {}

def pede_pasta():
    while True:
        global path
        path=input("Este programa analisa o tipo de ficheiros presente numa pasta. Insira o caminho para uma pasta: ")
        if os.path.isdir(path) == True:
            return path

def faz_calculos():
    global path
    global dicionario
    pede_pasta()
    listaFicheiros = os.listdir(path)
    myList = [i.split('.',1) for i in listaFicheiros]
    for ficheiro in myList:
        if (os.path.isdir(path+"\\"+ficheiro[0])==False): #verificar se NÃO é uma pasta
            if ficheiro[1] in dicionario:
                dicionario[ficheiro[1]]['quantidade'] +=1
                dicionario[ficheiro[1]]['volume'] += os.path.getsize(path+"\\"+ficheiro[0]+"."+ficheiro[1])/1024

            else:
                dicionario[ficheiro[1]]= dict({'volume': 0, 'quantidade': 0})
                dicionario[ficheiro[1]]['volume'] = (os.path.getsize(path+"\\"+ficheiro[0]+"."+ficheiro[1]))/1024
                dicionario[ficheiro[1]]['quantidade']= 1

    print(dicionario)
    return(dicionario)


def guarda_resultados():
    global path
    global dicionario
    path_split = path.split("\\")
    file_name= path_split[len(path_split)-1]
    with open(file_name+'.csv', 'w', newline='') as ficheiro:
        campos = ['Extensao', 'Quantidade','Tamanho[kByte]']
        writer = csv.DictWriter(ficheiro, fieldnames=campos)   
        writer.writeheader()
        for k, v in dicionario.items(): #k dict_1 -> json, v dict_2 -> {'volume': 0.2607421875, 'quantidade': 1}
            writer.writerow({'Extensao':k, 'Quantidade':dicionario[k]['quantidade'], 'Tamanho[kByte]':dicionario[k]['volume']})
    print("Os resultados foram guardados no ficheiro " + file_name+".csv")


def faz_grafico_queijos():
    global path
    global dicionario
    faz_calculos()
    guarda_resultados()
    lista_chaves=[]
    lista_valores=[]
    resposta=""
    while resposta != '1' and resposta != '2':
        resposta = input("Escreva um dos seguintes números para observar os dados no gráfico de queijos:\n1 - Extensão e Quantidade\n2 - Extensão e Tamanho\n")
        for k, v in dicionario.items():
            #print(dicionario[k]['quantidade'])

            if resposta=='1':
                titulo = 'Quantidade'
                lista_chaves.append(k)
                lista_valores.append(dicionario[k]['quantidade'])

            elif resposta=='2':
                titulo = 'Tamanho'
                lista_chaves.append(k)
                lista_valores.append(dicionario[k]['volume'])

    plt.pie(lista_valores, labels=lista_chaves, autopct='%1.0f%%')
    plt.title(titulo)
    plt.show()
    

def faz_grafico_barras():
    global path
    global dicionario
    faz_grafico_queijos()
    lista_chaves=[]
    lista_valores=[]
    resposta=""
    while resposta != '1' and resposta != '2':
        resposta = input("Escreva um dos seguintes números para observar os dados no gráfico de barras:\n1 - Extensão e Quantidade\n2 - Extensão e Tamanho\n")
        for k, v in dicionario.items():
            #print(dicionario[k]['quantidade'])

            if resposta=='1':
                titulo = 'Quantidade'
                lista_chaves.append(k)
                lista_valores.append(dicionario[k]['quantidade'])

            elif resposta=='2':
                titulo = 'Tamanho'
                lista_chaves.append(k)
                lista_valores.append(dicionario[k]['volume'])

    plt.bar(lista_chaves, lista_valores)
    plt.title(titulo)
    plt.show()
    
