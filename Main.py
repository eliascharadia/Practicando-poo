import pygame
from Class_personaje import *
from datos_imagenes import *
from pygame.locals import *
pygame.init()
H, W = 500,1000
pantalla = pygame.display.set_mode((W,H))
fondo = pygame.image.load("Imagenes\\fondo.jpg")
fondo = pygame.transform.scale(fondo, (W,H))
RELOJ = pygame.time.Clock()
FPS = 18#Para desacelerar la pantalla
#Creando un objeto personaje
mario = Personaje(diccionario_imagenes['Imagenes mario'],(40,40),60,390,10)

img = diccionario_imagenes['Imagenes mario']['Quieto'][0]
print(pantalla.get_width())  
rectangulo = img.get_rect()
print(rectangulo.width)

flag = True
while flag:
    RELOJ.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False
        elif event.type == MOUSEBUTTONDOWN:
            print(event.pos)

    teclas = pygame.key.get_pressed()#Obtengo las teclas que se matienen presionadas
    if teclas[pygame.K_RIGHT]:
        mario.que_hace = "Derecha"
    elif teclas[pygame.K_LEFT]:
        mario.que_hace = "Izquierda"
    elif teclas[pygame.K_SPACE] or teclas[pygame.K_UP]:
        mario.que_hace = "Saltar"
    else:
        mario.que_hace = "Quieto"

    pantalla.blit(fondo, (0,0))
    mario.actualizar(pantalla)



    
    pygame.display.update()

pygame.quit()

