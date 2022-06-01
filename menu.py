import pygame
from random import randint

pygame.init()
janela = pygame.display.set_mode((800, 600))
pygame.display.set_caption("COLETA_DOS_CAMPEOES")
tela = pygame.image.load('telaInicial.jpeg')
quadro = pygame.image.load('quadro.png')


def menu():
    janela.blit(tela, (0, 0))
    # text(janela, 'start', 22, 80, 250)
    # text(janela, 'quit', 22, 80, 280)
    start_box = pygame.Rect(58, 250, 48, 27)
    sair_box = pygame.Rect(58, 280, 45, 27)

    while pygame.event.wait() or pygame.event.get():

        mouse = pygame.mouse.get_pos()
        press = pygame.mouse.get_pressed()[0]

        if 400 + 40 > mouse[0] > 400 and 300 + 40 > mouse[1] > 300:
            text2(janela, 'Iniciar', 50, 400, 300)

            if press:
                jogo()
        else:
            text(janela, 'Iniciar', 50, 400, 300)

        if 400 + 50 > mouse[0] > 400 and 340 + 50 > mouse[1] > 340:
            text2(janela, 'Sair', 50, 400, 340)

            if press:
                quit()
        else:
            text(janela, 'Sair', 50, 400, 340)

        if 400 + 60 > mouse[0] > 400 and 380 + 60 > mouse[1] > 380:
            text2(janela, 'Objetivo', 50, 400, 380)

            if press:
                objetivo()
        else:
            text(janela, 'Objetivo', 50, 400, 380)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        pygame.display.update()


font_name = pygame.font.match_font('berlin sans FB', True, True)


def text(surf, text, size, x, y):
    cor = (0, 0, 0)
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, (cor))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


def text2(surf, text, size, x, y):
    cor = (0, 80, 0)
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, (cor))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


def objetivo():
    while pygame.event.wait() or pygame.event.get():
        janela.blit(quadro, (0, 0))
        mouse = pygame.mouse.get_pos()
        press = pygame.mouse.get_pressed()[0]

        if 400 + 50 > mouse[0] > 400 and 500 + 50 > mouse[1] > 500:
            text2(janela, 'Voltar', 50, 400, 500)

            if press:
                menu()

        else:
            text(janela, 'Voltar', 50, 400, 500)
        pygame.display.update()


def jogo():
    TelaFinal = pygame.image.load('TelaFinal.png')

    ponto = 0
    azul = (0, 0, 255)
    verde = (0, 155, 155)
    vermelho = (255, 0, 0)

    font = pygame.font.SysFont('arial black', 30)

    texto = font.render('               0', True, (0, 0, 0))

    pos_texto = texto.get_rect()
    pos_texto.center = (83, 40)

    class lixeiro(object):
        def __init__(self, x, y, velocidade, lix):
            self.x = x
            self.y = y
            self.velocidade = velocidade
            self.lix = lix

    class fase(object):
        def __init__(self):
            self.imagem = pygame.image.load('fundodojogo.png')
            self.numero = 1

    class objeto(object):
        def __init__(self, objetoImagem, pos_x, pos_y, objetoVelocidade):
            self.objetoImagem = objetoImagem
            self.pos_x = pos_x
            self.pos_y = pos_y
            self.objetoVelocidade = objetoVelocidade

    lixeira = lixeiro(350, 450, 30, pygame.image.load('LixeiraVerde.png'))

    fundo = fase()

    lixo = objeto(pygame.image.load('GarrafaPCA.png'), randint(1, 350), randint(-350, -100), randint(8, 11))
    lixo2 = objeto(pygame.image.load('GarrafaPCA.png'), randint(450, 600), randint(-800, -550), randint(8, 11))

    intro = True
    janela_aberta = True
    while janela_aberta:

        pygame.time.delay(35)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                janela_aberta = False

        comandos = pygame.key.get_pressed()

        if comandos[pygame.K_RIGHT] and lixeira.x <= 680:
            lixeira.x += lixeira.velocidade

        if comandos[pygame.K_LEFT] and lixeira.x >= 20:
            lixeira.x -= lixeira.velocidade

        if (lixo.pos_y >= 460):
            lixo.pos_y = randint(-350, -100)
            lixo.pos_x = randint(1, 350)

        if (lixo2.pos_y >= 460):
            lixo2.pos_y = randint(-800, -550)
            lixo2.pos_x = randint(450, 600)

        if (lixeira.x <= lixo.pos_x <= (lixeira.x + 110)) and (lixeira.y <= lixo.pos_y):
            ponto += 1
            texto = font.render('               ' + str(ponto), True, (0, 0, 0))

        if (lixeira.x <= lixo2.pos_x <= (lixeira.x + 100)) and (lixeira.y <= lixo2.pos_y):
            ponto += 1
            texto = font.render('               ' + str(ponto), True,(0, 0, 0))

        if ponto == 5:
            ponto = 0
            texto = font.render('               ' + str(ponto), True,(0, 0, 0))
            fundo.numero += 1

            if fundo.numero == 2:
                lixo.objetoImagem = pygame.image.load('Papel.png')
                lixo2.objetoImagem = pygame.image.load('Papel.png')
                lixeira.lix = pygame.image.load('LixeiraAzul.png')

            if fundo.numero == 3:
                lixo.objetoImagem = pygame.image.load('Metais.png')
                lixo2.objetoImagem = pygame.image.load('Metais.png')
                lixeira.lix = pygame.image.load('LixeiraAmarela.png')

            if fundo.numero == 4:
                lixo.objetoImagem = pygame.image.load('Plastico.png')
                lixo2.objetoImagem = pygame.image.load('Plastico.png')
                lixeira.lix = pygame.image.load('LixeiraVermelha.png')

            if fundo.numero == 5:
                lixo.objetoImagem = pygame.image.load('NaoRecicla.png')
                lixo2.objetoImagem = pygame.image.load('NaoRecicla.png')
                lixeira.lix = pygame.image.load('LixeiraCinza.png')

            if fundo.numero == 6:
                final = True

                while final:
                    ponto = 0
                    

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            quit()

                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_r:
                                intro = True

                                final = False

                                fundo.numero = 1
                                ponto = 0
                                lixeira = lixeiro(350, 450, 30, pygame.image.load('LixeiraVerde.png'))
                                lixo = objeto(pygame.image.load('GarrafaPCA.png'), randint(1, 350), randint(-350, -100),
                                              randint(8, 11))
                                lixo2 = objeto(pygame.image.load('GarrafaPCA.png'), randint(450, 600),
                                               randint(-800, -550),
                                               randint(8, 11))

                            if event.key == pygame.K_s:
                                pygame.quit()
                                quit()

                    janela.blit(TelaFinal, (0, 0))

                    myfont1 = pygame.font.SysFont("arial", 35)
                    myfont2 = pygame.font.SysFont("arial", 35)

                    nlabel1 = myfont1.render("Você conseguiu!!", 1, (255,255,0))
                    nlabel2 = myfont2.render("Toque R para recomeçar, ou S para sair!", 1, (255,255,0))

                    janela.blit(nlabel1, (315, 500))
                    janela.blit(nlabel2, (130, 520))

                    pygame.display.flip()
                    pygame.display.update()

        lixo.pos_y += lixo.objetoVelocidade
        lixo2.pos_y += lixo2.objetoVelocidade

        janela.blit(fundo.imagem, (0, 0))
        janela.blit(lixeira.lix, (lixeira.x, lixeira.y))
        janela.blit(lixo.objetoImagem, (lixo.pos_x, lixo.pos_y))
        janela.blit(lixo2.objetoImagem, (lixo2.pos_x, lixo2.pos_y))
        janela.blit(texto, pos_texto)
        pygame.display.update()
    pygame.quit()


menu()
