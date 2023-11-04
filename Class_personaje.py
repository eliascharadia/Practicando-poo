from Configuraciones import reescalar_imagenes
import pygame

class Personaje:
    def __init__(self,animaciones, tamaño, pos_x, pos_y, velocidad):
        self.animaciones = animaciones
        reescalar_imagenes(self.animaciones, *tamaño)
        self.rectangulo_principal = self.animaciones["Quieto"][0].get_rect()
        self.rectangulo_principal.x = pos_x
        self.rectangulo_principal.y = pos_y
        self.velocidad = velocidad

        self.que_hace = "Quieto"
        self.contador_pasos = 0
        self.animacion_actual = self.animaciones["Quieto"]


    def actualizar(self, pantalla):
        match self.que_hace:
            case "Derecha":
                self.animacion_actual  = self.animaciones["Caminar derecha"]
                self.animar(pantalla)
                self.caminar(pantalla)
            case "Izquierda":
                self.animacion_actual  = self.animaciones["Caminar izquierda"]
                self.animar(pantalla)
                self.caminar(pantalla)
            case "Saltar":
                self.animacion_actual  = self.animaciones["Saltar"]
                self.animar(pantalla)
            case "Quieto":
                self.animacion_actual  = self.animaciones["Quieto"]
                self.animar(pantalla)


    def animar(self, pantalla):
        largo = len(self.animacion_actual)
        if self.contador_pasos >= largo:
            self.contador_pasos = 0

        pantalla.blit(self.animacion_actual[self.contador_pasos], self.rectangulo_principal)
        self.contador_pasos += 1
    
    def caminar(self, pantalla):
        velocidad_actual = self.velocidad
        if self.que_hace == "Izquierda":
            velocidad_actual *= -1

        
        nueva_x = self.rectangulo_principal.x + velocidad_actual
        if nueva_x >= 0 and nueva_x <= pantalla.get_width() - self.rectangulo_principal.width:
            self.rectangulo_principal.x += velocidad_actual
                     