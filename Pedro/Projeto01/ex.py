import pygame
import sys

def ler_arquivo_txt(arquivo_path):
    linhas = []
    try:
        with open(arquivo_path, 'r', encoding='utf-8') as arquivo:
            linhas = arquivo.readlines()
    except FileNotFoundError:
        print(f"O arquivo '{arquivo_path}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo: {e}")
    return linhas
def digit(texto,x,y):
    pygame.init()

    # Configurações da janela
    largura, altura = 1366, 720
    tela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("Caixa de Diálogo Estilo Dark Souls 3")

    # Cores
    preto = (0, 0, 0)
    branco = (255, 255, 255)
    cinza = (50, 50, 50)
    texto_completo = texto
    texto_exibido = ""
    contador_caracteres = 0
    tempo_por_caractere = 35
    tempo_anterior = pygame.time.get_ticks()
    fonte = pygame.font.Font(None, 32)  # Tamanho da fonte inicial
    executando = True

    while executando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                executando = False
            elif evento.type == pygame.MOUSEBUTTONDOWN:  # Verifica se houve um clique do mouse
                if evento.button == 1:  # 1 representa o botão esquerdo do mouse
                    if contador_caracteres < len(texto_completo):
                        # Se ainda houver caracteres a serem exibidos, mostre todos de uma vez
                        texto_exibido = texto_completo
                        contador_caracteres = len(texto_completo)

        # Limpe a tela
        tela.fill(branco)
        # Desenhe a caixa de diálogo
        pygame.draw.rect(tela, cinza, (245, 450, 900, 250), 2)  # Caixa (borda mais fina)
        pygame.draw.rect(tela, preto, (250, 455, 890, 240))  # Interior da caixa

        # Atualize o texto exibido gradualmente com base no tempo
        tempo_atual = pygame.time.get_ticks()
        if tempo_atual - tempo_anterior >= tempo_por_caractere and contador_caracteres < len(texto_completo):
            texto_exibido += texto_completo[contador_caracteres]
            contador_caracteres += 1
            tempo_anterior = tempo_atual
        # Renderize o texto no centro da caixa de diálogo
        texto_superficie = fonte.render(texto_exibido, True, branco)
        texto_retangulo = texto_superficie.get_rect(topleft=(x, y))
        
        tela.blit(texto_superficie, texto_retangulo)
        
        pygame.display.flip()

    pygame.quit()
    sys.exit()
import pygame
import sys

pygame.init()

# Configurações da janela
largura, altura = 1366, 720
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Caixa de Diálogo Estilo Dark Souls 3")

# Cores
preto = (0, 0, 0)
branco = (255, 255, 255)
cinza = (50, 50, 50)

# Fonte estilo Dark Souls 3
fonte = pygame.font.Font(r'C:\Users\dev-sistemas-tarde\Documents\Python(tarde)\Projeto01\Fontes\darksouls.ttf', 32) 
fonte = pygame.font.Font(None, 25)

executando = True
while executando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False
    # Limpe a tela
    tela.fill(preto)
    # Desenhe a caixa de diálogo
    x, y=255, 460
    texto="Ander é um undead que nasceu do nada, e de nada vivia, vagando anos e anos,fraco e sozinho, na esperança de que um dia o mundo será um lugar melhor,que a chama será reacendida, e que seu sofrimento acabará. Indo de lugar a lugar furtando e acumulando itens apenas para ter uma razão para viver."
    digit(texto,x,y)
    
    pygame.display.flip()

# Encerre o Pygame
pygame.quit()
sys.exit()