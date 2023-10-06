import pygame
import sys

pygame.init()

def escolhas(a, b):
    choice=0
    tamanho_fonte = 32
    fonte = pygame.font.Font(None, tamanho_fonte)
    opcao1 = a
    opcao2 = b
    opcao_selecionada = None
    executando1 = True
    while executando1:
        for evento in pygame.event.get():
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 1:  # Botão esquerdo do mouse
                    # Verifica se o clique foi em uma das opções
                    if opcao1_rect.collidepoint(evento.pos):
                        opcao_selecionada = opcao1
                        if pygame.MOUSEBUTTONDOWN:
                            choice=1
                            executando1 = False
                    elif opcao2_rect.collidepoint(evento.pos):
                        opcao_selecionada = opcao2
                        if pygame.MOUSEBUTTONDOWN:
                            choice=2
                            executando1 = False
        # Limpe a tela
        tela.fill(branco)
        # Desenhe a caixa de diálogo
        pygame.draw.rect(tela, cinza, (245, 450, 900, 250), 2)  # Caixa (borda mais fina)
        pygame.draw.rect(tela, preto, (250, 455, 890, 240))  # Interior da caixa
        # Renderize o texto das opções com tamanho variável
        opcao1_superficie = fonte.render(a, True, branco)
        opcao1_rect = opcao1_superficie.get_rect(topleft=(300, 600))
        if opcao1_rect.collidepoint(pygame.mouse.get_pos()):
            tamanho_fonte_aumentado = tamanho_fonte + 5
            fonte = pygame.font.Font(None, tamanho_fonte_aumentado)
        else:
            fonte = pygame.font.Font(None, tamanho_fonte)
        tela.blit(fonte.render(a, True, branco), opcao1_rect)
        
        opcao2_superficie = fonte.render(b, True, branco)
        opcao2_rect = opcao2_superficie.get_rect(topleft=(300, 650))
        if opcao2_rect.collidepoint(pygame.mouse.get_pos()):
            tamanho_fonte_aumentado = tamanho_fonte + 5
            fonte = pygame.font.Font(None, tamanho_fonte_aumentado)
        else:
            fonte = pygame.font.Font(None, tamanho_fonte)
        tela.blit(fonte.render(b, True, branco), opcao2_rect)

        pygame.display.flip()

    return (choice)


# Configurações da janela
largura, altura = 1366, 720
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Caixa de Diálogo Estilo Dark Souls 3")

# Cores
preto = (0, 0, 0)
branco = (255, 255, 255)
cinza = (50, 50, 50)

# Fonte estilo Dark Souls 3
tamanho_fonte = 32
fonte = pygame.font.Font(None, tamanho_fonte)

executando = True
while executando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False

    # Limpe a tela
    tela.fill(branco)
    # Desenhe a caixa de diálogo
    pygame.draw.rect(tela, cinza, (245, 450, 900, 250), 2)  # Caixa (borda mais fina)
    pygame.draw.rect(tela, preto, (250, 455, 890, 240))  # Interior da caixa
    
    a = "1. adsd"
    b = "2. asdasd"

    escolha = escolhas(a, b)
    print (escolha)
    pygame.display.flip()

# Encerre o Pygame
pygame.quit()
sys.exit()
