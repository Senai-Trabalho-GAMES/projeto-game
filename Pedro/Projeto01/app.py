import pygame

# Inicialize o Pygame
pygame.init()

# Configurações da janela
tela = pygame.display.set_mode((1366, 720))
pygame.display.set_caption("TESTE")

preto = (0, 0, 0)
branco = (255, 255, 255)
cinza = (50, 50, 50)

texto= "Eai pessoal, tudo bem? aqui quem fala e o Edu"
fonte = pygame.font.Font(r'C:\Users\dev-sistemas-tarde\Documents\Python(tarde)\Projeto01\Fontes\darksouls.ttf', 32)
fonte = pygame.font.Font(None, 25)
x=450
y=400


main_title = pygame.image.load(r'C:\Users\dev-sistemas-tarde\Documents\Python(tarde)\Projeto01\Imagens\images.jpg')
main_title = pygame.transform.scale(main_title, (1366, 720))
background1=pygame.image.load(r'C:\Users\dev-sistemas-tarde\Documents\Python(tarde)\Projeto01\Imagens\imagen2.jpg')

# Inicialize o mixer de áudio
pygame.mixer.init()
musictheme = pygame.mixer.Sound(r'C:\Users\dev-sistemas-tarde\Documents\Python(tarde)\Projeto01\Sounds\Main_Theme.mp3')

jogo_iniciado = False
executando = True
opacidadefundo=0
volume= 1.0
opacidade2=0

# Loop principal do jogo
while executando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RETURN:  # Verifica se a tecla Enter foi pressionada
                jogo_iniciado = True  # Inicia o jogo quando o Enter é pressionado
    
    # Reproduzir o efeito sonoro
    musictheme.play()
    #Aparecendo o menu inicial aos poucos
    if opacidadefundo<255:
        opacidadefundo +=1
    main_title.set_alpha(opacidadefundo)
    tela.blit(main_title, (0, 0))
    
    #Verifica se o enter foi pressinado
    if jogo_iniciado:
        #Abaixa gradualmente a opacidade?volume do fundo
        if opacidadefundo > 0:
            opacidadefundo -= 5  # Ajuste a velocidade de transição como desejar        
        if volume >0:
            volume -= 0.02
        # Renderize o plano de fundo/musica com a opacidade/volume atual
        musictheme.set_volume(volume)
        main_title.set_alpha(opacidadefundo)
        #deixa a tela preta
        tela.fill(preto)
        if opacidadefundo==0:
            if opacidade2<255:
                opacidade2 +=5
        background1.set_alpha(opacidade2)       
        tela.blit(background1, (0, 0))
        tela.blit(main_title, (0, 0))
        if opacidade2 ==255:
            texto1 = fonte.render(texto, True, branco)
            tela.blit(texto1, (x, y))
            dialogo1=pygame.draw.rect(tela, cinza, (245, 450, 900, 250), 2)  # Caixa (borda mais fina)
            dialogo2=pygame.draw.rect(tela, preto, (250, 455, 890, 240))  # Interior da caixa

    # Atualize a tela
    pygame.display.flip()

# Encerre o Pygame
pygame.quit()