import pygame
from Configuraciones import crear_plataforma
H, W = 500,1000
plataformas = []
piso = crear_plataforma(True, (W,20), 0, H-60, r"Recursos\3.png")

plataformas.append(piso)