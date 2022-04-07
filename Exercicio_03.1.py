#Lista 4:

def exercicio3_lista4():

    notas = 5.0, 4, 8, 10

    media = sum(notas)/len(notas)

    print("As notas são: ", notas)
    print("A média das notas é: ", media)

#exercicio3_lista4()

def exercicio9_lista4():

    janeiro = float(input("Qual a temperatura média em Janeiro:"))
    fevereiro = float(input("Qual a temperatura média em Fevereiro:"))
    março = float(input("Qual a temperatura média em Março:"))
    abril = float(input("Qual a temperatura média em Abril:"))
    maio = float(input("Qual a temperatura média em Maio:"))
    junho = float(input("Qual a temperatura média em Junho:"))
    julho = float(input("Qual a temperatura média em Julho:"))
    agosto = float(input("Qual a temperatura media em Agosto:"))
    setembro = float(input("Qual a temperatura média em Setembro:"))
    outubro = float(input("Qual a temperatura média em Outubro:"))
    novembro = float(input("Qual a temperatura média em Novembro:"))
    dezembro = float(input("Qual a temperatura média em Dezembro:"))

    meses = [janeiro, fevereiro, março, abril, maio, junho, julho, agosto, setembro, outubro, novembro, dezembro]
    media = sum(meses)/12

    print("A temperatura média anual é:", media)

    if janeiro > media:
        print("Janeiro é maior que a média anual:", janeiro)
    if fevereiro > media:
        print("Fevereiro é maior que a média anual:", fevereiro)
    if março > media:
        print("Março é maior que a média anual:", março)
    if abril > media:
        print("Abril é maior que a média anual:", abril)
    if maio > media:
        print("Maio é maior que a média anual:", maio)
    if junho > media:
        print("Junho é maior que a média anual:", junho)
    if julho > media:
        print("Julho é maior que a média anual:", julho)
    if agosto > media:
        print("Agosto é maior que a média anual:", agosto)
    if setembro > media:
        print("Setembro é maior que a média anual:", setembro)
    if outubro > media:
        print("Outubro é maior que a média anual:", outubro)
    if novembro > media:
        print("Novembro é maior que a média anual:", novembro)
    if dezembro > media:
        print("Dezembro é maior que a média anual:", dezembro)
    else:
        print("Nenhuma temperatura está acima da média.")
    
#exercicio9_lista4()
    
#Lista 6:

def exercicio6_lista6():

    linha = int(input("Insira o numero de linhas: "))
    coluna = int(input("Insira o numero de colunas: "))

    if linha == 1:
        if coluna > 1:
            print("+", (int(coluna) - 2) * "- ", "+")
        elif coluna == 1:
            print("+")
    elif linha > 20:
        print("Linha não pode ser maior que 20, será considerado Linha = 20")
        if coluna > 20:
            print("Coluna não pode ser maior que 20, será considerado Coluna = 20")
            coluna = 20
        linha = 20
        print("+", (int(coluna) - 2) * "- ", "+")
        print((int(linha) - 2) * "| \n", int(coluna)* " ", int(linha) * "|") #Não consigo botar esse ultimo "|" na ultima coluna
        print("\033[A+")
    elif linha > 1:
        print("+", (int(coluna) - 2) * "- ", "+")
        print((int(linha) - 2) * "| \n", int(coluna)* " ", int(linha) * "|") 
        print("\033[A+")
    elif linha < 1:
        print("Linha não pode ser menor do que 1, sera considerado Linha = 1")
        linha = 1
        print("+", (int(coluna) - 2) * "- ", "+")

#exercicio6_lista6()


def exercicio4_lista6():

    string1 = "Brasil Hexa 2006"
    string2 = "Brasil Hexa 2022!"

    print("String 1:", string1)
    print("String 2:", string2)

    print("Tamanho de", "'",string1, "'", "é: ", len(string1), "caracteres")
    print("Tamanho de", "'",string2, "'", "é: ", len(string2), "caracteres")
    
    if string1 == string2:
        print("As duas strings tem conteudos iguais")
    else:
        print("As duas strings tem conteudos diferentes")

    if len(string1) == len(string2):
        print("As duas strings são de tamanhos iguais")
    else:
        print("As duas strings tem tamanhos diferentes")

#exercicio4_lista6()
