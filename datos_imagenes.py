import json
import pygame
from Configuraciones import rotar_imagen
# with open("imagenes_objetos.json") as archivo:
#     diccionario_animaciones = json.load(archivo)


diccionario_imagenes = {}

diccionario_imagenes["Imagenes mario"] = {}
diccionario_imagenes["Imagenes mario"]['Quieto'] = [pygame.image.load('Recursos\\0.png')]
diccionario_imagenes["Imagenes mario"]['Caminar derecha'] = [pygame.image.load('Recursos\\1.png'), pygame.image.load('Recursos\\2.png')]
diccionario_imagenes["Imagenes mario"]['Caminar izquierda'] = rotar_imagen(diccionario_imagenes["Imagenes mario"]['Caminar derecha'])
diccionario_imagenes["Imagenes mario"]['Saltar'] = [pygame.image.load('Recursos\\3.png')]



