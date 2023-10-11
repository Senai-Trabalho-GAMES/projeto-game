import random
def itens(n):


    itens = ["Braseiro", "Fragmento de Titanita", "Resina"]
    itens_bons = ["Pedaço de Titanita", "Osso do Regresso", "Fragmento de Estus"]

    numeros_de_itens_coletados = n
    contagem_itens = {}
    itembom= False
    soma=0
    for i in range(numeros_de_itens_coletados):
        item_bom_check=random.randint(0, 25)    
        if item_bom_check == 5 and itembom== False:
            soma+=5
            itembom=True
            aleatorio2 = random.randint(0, 2)
            item_sorteado2 = itens_bons[aleatorio2]
            if not item_sorteado2 in contagem_itens:
                contagem_itens[item_sorteado2] = 1
        else:
            soma+=1
            aleatorio = random.randint(0, 2)
            item_sorteado = itens[aleatorio]
            #Verifica se o item sorteado existe no dicionario, caso exista, adicionará mais um a quantidade do item
            if item_sorteado in contagem_itens:
                contagem_itens[item_sorteado] += 1
            #Caso não existá, adicionará o item ao dicionario
            else:
                contagem_itens[item_sorteado] = 1


    #A função imprime os itens conseguidos, e pode armazernar o total de pontos conseguidos.
    for item, quantidade in contagem_itens.items():
        print(f"{quantidade}x {item}")
    return(soma)
numero_de_itens_coletados=10
pts=itens(numero_de_itens_coletados)
print(pts)
