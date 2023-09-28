# finais:

'''
Interface gráfica TKInter
Armazenamento de dados em arquivo
Leitura de dados em arquivo
Dados estruturados na forma de listas E dicionários
Busca por informações no arquivo em disco ou em dados em tempo de execução
Classificação de dados usando dois ou mais critérios
As funcionalidades do programa devem ser de fato escritas na forma de funções (demonstrem a capacidade de criar funções com e sem Parâmetros).
Usem comentários no código para facilitar a compreensão do que foi criado por parte do avaliador.
'''

# bom: (1,3,4)
# neu: (2,3,4)
# rui: (1,3,2)

floresta=False
estrada=False
pantano=False
quatro=False

for i in range(0,3):
    esc=int(input("Escolhas? (1)(2)(3)(4)"))
    match esc:
        case 1:
            um=True
            pass
        case 2:
            dois=True
            pass
        case 3:
            tres=True
            pass
        case 4:
            quatro=True
            pass
        case _:
            pass


if um==True and tres==True and quatro==True:
    print("Final feliz")
elif dois==True and tres==True and quatro==True:
    print("Final Neutro")
elif um==True and tres==True and dois==True:
    print("Final Ruim")
else:
    pass