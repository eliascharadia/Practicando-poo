import pygame
from Configuraciones import crear_plataforma
H, W = 500,1000
plataformas = []
piso = crear_plataforma(True, (219,20), 0, H-60, r"Recursos\3.png")
piso2 = crear_plataforma(True, (219,20), 447, H-60, r"Recursos\3.png")

plataformas.append(piso)
plataformas.append(piso2)