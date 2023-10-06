import pygame
import time

# Inicializar o Pygame
pygame.init()

# Configurações da janela
largura, altura = 1324, 768
janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Frase Piscante")

#local da imagem de fundo
imagem_de_fundo = pygame.image.load('C:/Users/dev-sistemas-tarde/Downloads/intro.jpg')

# Redimensionar a imagem para o tamanho da janela 
imagem_de_fundo = pygame.transform.scale(imagem_de_fundo, (largura, altura))

# Cores
branco = (255, 255, 255)
preto = (0, 0, 0)

# Fonte e texto
fonte = pygame.font.Font('OptimusPrinceps.ttf', 24)
frase = "PRESSIONE ENTER PARA CONTINUAR"


posicao_x = (largura - fonte.size(frase)[0]) // 2
posicao_y = altura + 20  # Comece abaixo da tela

# Variável para controlar o tempo de piscagem
piscando = True

# Loop principal do jogo
executando = True
while executando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False

    janela.blit(imagem_de_fundo, (0, 0))

    if piscando:
        texto = fonte.render(frase, True, branco)
        janela.blit(texto, (posicao_x, posicao_y))

    pygame.display.flip()

    # Ajuste para controlar a velocidade de movimento
    posicao_y = 600  

    # Aguarda um curto período de tempo
    time.sleep(0.8)  

    # Inverte o estado de piscagem
    piscando = not piscando  

# Encerra o Pygame
pygame.quit()
