import pygame
import sys


# Inicialize o Pygame
pygame.init()


# Defina as cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
WINDOW_COLOR = (200, 200, 200)  # Cor da janela de texto
TEXT_COLOR = (255, 0, 0)  # Cor do texto (vermelho)


# Defina a largura e altura da tela
WIDTH, HEIGHT = 800, 600


# Crie uma janela
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Janela de Texto")


# Carregue o arquivo de texto e armazene as linhas em uma lista
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


# Função para exibir um conjunto de linhas em uma janela de texto do Pygame
def exibir_linhas_em_janela_de_texto(start, num_linhas):
    fonte = pygame.font.Font(None, 24)  # Tamanho da fonte menor


    running = True


    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Clique esquerdo do mouse
                    start += num_linhas


        screen.fill(BLACK)  # Preencha o fundo com a cor preta


        # Desenha a janela de texto
        pygame.draw.rect(screen, WINDOW_COLOR, (50, 50, 300, 400))


        # Exibe o conjunto de linhas
        y = 70  # Ajuste a posição vertical inicial
        end = start + num_linhas
        for i in range(start, min(end, len(linhas))):
            linha = linhas[i].strip()  # Remove espaços em branco e caracteres de nova linha
            texto = fonte.render(linha, True, TEXT_COLOR)  # Use a cor de texto personalizada
            screen.blit(texto, (70, y))
            y += 30  # Ajuste o espaçamento vertical


        pygame.display.flip()


        # Verifica se chegou ao final do diálogo
        if start >= len(linhas):
            running = False


    pygame.quit()


# Chamada da função para ler o arquivo
arquivo_path = "dialog.txt"
linhas = ler_arquivo_txt(arquivo_path)


# Linha inicial para exibição
start = 0


# Número de linhas a serem exibidas a cada clique
num_linhas_por_clique = 3


# Chamada da função para exibir as linhas em uma janela de texto do Pygame
exibir_linhas_em_janela_de_texto(start, num_linhas_por_clique)
