autonomia=0

class automovel():

    def __init__(self, cap_dep, quant_comb, consumo):
        self.cap_dep = cap_dep
        self.quant_comb = quant_comb
        self.consumo = consumo
    
    def combustivel(self):
        return self.quant_comb

    def autonomia(self):
        global autonomia
        if autonomia==0:
            return (int(self.quant_comb)*100)/int(self.consumo)
        else:
            return autonomia
    
    def abastece(self, n_litros):
        global autonomia
        if n_litros == "0":
            return (int(self.quant_comb)*100)/int(self.consumo)
        else:
            if int(self.quant_comb)+int(n_litros)>int(self.cap_dep):
                print("\nERRO")
                return (int(self.quant_comb)*100)/int(self.consumo)
            else:     
                
                self.quant_comb=str(int(self.quant_comb)+int(n_litros))
                autonomia = (int(self.quant_comb)*100)/int(self.consumo)                
                return autonomia

            
    def percorre(self, n_km):
        global autonomia
        if int(n_km) > autonomia:
            print("\nERRO TRAJETO NÃO EFETUADO")
        else:
            autonomia -= int(n_km)
            self.quant_comb = str(int(self.quant_comb)-((int(n_km)*int(self.consumo))/100))
        return autonomia


def main():
    cap_dep = input("Por favor, insira a capacidade do depósito\n")
    quant_comb = input("Por favor, insira a quantidade de combustível disponível\n")
    consumo = input("Por favor, insira o consumo do automóvel em litros aos 100km\n")
    foo = automovel(cap_dep, quant_comb, consumo) #criar instância
    while True:
        opcao = input ("\nPor favor, escolha uma das seguintes opções:\n1 - combustível\n2 - autonomia\n3 - abastece\n4 - percorre\n5 - exit\n\n")
        if opcao == "1":
            print("\nA quantidade de combustível disponível no depósito é: " + foo.combustivel() + "\n\n")
        elif opcao == "2":
            print("\nO número de km que é possível percorrer com o combustível no depósito é: " + str(foo.autonomia()) + "\n\n")
        elif opcao == "3":
            n_litros = input("\nPor favor insira o número de litros que pretende abastecer:\n")
            print("\nA autonomia é de: "+ str(foo.abastece(n_litros)))
        elif opcao == "4":
            n_km = input("\nPor favor indique o número de km que pretende percorrer:\n")
            print("\nA autonomia é de: "+ str(foo.percorre(n_km)))
        elif opcao == "5":
            print("\nAdeus!")
            exit()

if __name__ == "__main__": 
    main()