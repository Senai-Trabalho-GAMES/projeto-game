info=[
    {'local':1,'gob':0,'item':3},
    {'lqq':0,'gow':0,'iem':0},
    {'lqq':0,'gow':0,'iem':0}
]

# for item in info:
#     for escolha in item:
#         if escolha == 'local':
#             if item[escolha] == 0:  
#                 print("aaa")
#             elif escolha == 'local':
#                 if item[escolha] == 1:  
#                     print("bbb")
#             elif escolha == 'local':
#                 if item[escolha] == 2:  
#                     print("ccc")
#         elif escolha == 'gob':
#             if item[escolha] == 0:  
#                 print("goblio")
#             elif escolha == 'gob':
#                 if item[escolha] == 1:  
#                     print("gob")
#             elif escolha == 'gob':
#                 if item[escolha] == 2:  
#                     print("lio")
#         elif escolha == 'item':
#             if item[escolha] == 0:  
#                 print("pocão")
#             elif item[escolha] == 0:  
#                 print("pocão")
#             elif item[escolha] == 0:  
#                 print("pocão")

dialog=[]

def countLinhas(arquivo_path):
    with open(arquivo_path, 'r') as arquivo:
        linhas = arquivo.readlines()
        return len(linhas)

arquivo_path="dialog.txt"
numLinhas=countLinhas(arquivo_path)
print(numLinhas) #Numero de linhas

with open(arquivo_path,"r") as f:
    for i in range(numLinhas):
        linhas=f.readline()
        dialog.append(linhas.strip())


print(dialog)


for i in dialog:
    print(i)

print(f"\n{dialog[5]}")
