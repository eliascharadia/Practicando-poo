import pygame as py

def reescalar_imagenes(diccionario_animaciones, ancho, alto):
    for clave in diccionario_animaciones:
        for i in range(len(diccionario_animaciones[clave])):
            img = diccionario_animaciones[clave][i]
            diccionario_animaciones[clave][i] = py.transform.scale(img, (ancho,alto))

def rotar_imagen(imagenes:list):
    lista_imagenes = []
    for i in range(len(imagenes)):
        imagen_rotada = py.transform.flip(imagenes[i],True,False)
        lista_imagenes.append(imagen_rotada)
    
    return lista_imagenes

def crear_plataforma(visible, tamaño,  x,  y, path=""):
    plataforma = {}
    if visible:
        plataforma["superficie"] = py.image.load(path)
        plataforma["superficie"] = py.transform.scale(plataforma["superficie"], tamaño)
    else:
        plataforma["superficie"] = py.Surface(tamaño)

    plataforma["rectangulo"] = plataforma["superficie"].get_rect()
    plataforma["rectangulo"].x = x
    plataforma["rectangulo"].y = y
    return plataforma



