import pygame


pygame.init()

largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Viusal")

#BCG atual
atual=0
RealAtual=0

# Coordenadas e tamanho do retângulo
x, y = 40, 390
largura_retangulo, altura_retangulo =720, 170
# Cor do retângulo (no formato RGB)
cor_retangulo = (200, 200, 200)


fonte=pygame.font.Font(None,36)
texto=f"Teste"
lista=[]
bcg=["a.png","b.png"]
cortexto=(0,0,255)
textSurface=fonte.render(texto,True,cortexto)
textRect=textSurface.get_rect()


indice_dialogo_atual = 0  # Inicialize com 0 para começar a partir da primeira linha
linhas_por_clique = 4  # Número de linhas a serem exibidas a cada clique


def processarTxt():
    arquivo = "dialog.txt"
    with open(arquivo, 'r',encoding='utf-8') as arquivo:
        for linha in arquivo:
            lista.append(linha.strip())

def mostrarBCG(atual):
    background = pygame.image.load(bcg[atual])
    background = pygame.transform.scale(background, (largura, altura))

    tela.blit(background, (0, 0))

def mostrarText():
    global textSurface, textRect,x,largura_retangulo,y,altura_retangulo,indice_dialogo_atual,linhas_por_clique,RealAtual
    atual=RealAtual
    mostrarBCG(atual)
    pygame.draw.rect(tela, cor_retangulo, (x, y, largura_retangulo, altura_retangulo))

    yAtual=y+25
    for i in range(indice_dialogo_atual, indice_dialogo_atual + linhas_por_clique):
        if i < len(lista):
            if i==11:
                RealAtual=1
                pass
                # Evento que vai acontecer na linha 11
                # tela.fill((0,0,0))
            else:
                linha = lista[i]
                textSurface=fonte.render(linha,True,cortexto)
                tela.blit(textSurface,(x_texto,yAtual))
                textRect.center=(x+largura_retangulo//2,y+altura_retangulo//2)
                yAtual+=35
        else:
            # Evento que vai acontecer quando as linhas acabarem
            # tela.fill((0,0,0))
            pass #Oque vai acontecer depois do dialogo
            
    pygame.display.update()



mostrarBCG(RealAtual)
processarTxt()
x_texto = 70
y_texto = y + (altura_retangulo - textSurface.get_height()) // 2 

executando=True
while executando:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                executando = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mostrarText()
                indice_dialogo_atual += linhas_por_clique
                pass

    
    
    


    pygame.display.flip()



pygame.quit()