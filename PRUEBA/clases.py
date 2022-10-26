import pygame

pygame.init()

class imagenes():
    def imagen(filename):
        fondo = pygame.image.load(filename)
        fondo = fondo.convert()
        return fondo

    def imagenPNG(filename):
        fondo = pygame.image.load(filename).convert_alpha()
        fondo = fondo.convert()
        return fondo

    def imagenPNGRevert (filename):
        fondo = pygame.image.load(filename).convert_alpha()
        fondo = fondo.convert()
        fondo = pygame.transform.flip(fondo,True,False)
        return fondo

#==================================ANIMACIONES GIF=============================================
class hojaSpriteRio():
    def __init__(self,image):
        self.archivo = image
    def obtener_rio(self, frame,largo, alto):
        rio = pygame.Surface((largo, alto))
        rio.blit(self.archivo,(0,0),((frame*largo),0,largo,alto))
        return rio
#==================================ANIMACIONES PNG==============================================
class hojaSpriteLlanta(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Image/LLANTAsprite.png")
        self.image.set_colorkey((255, 255, 255))
        self.image.convert_alpha()
        self.rect = self.image.get_rect()
        
class hojaSpritePez(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Image/PEZsprite.png")
        self.image.set_colorkey((255,255,255))
        self.image.convert_alpha()
        self.rect = self.image.get_rect()

class hojaSpritePez2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Image/PEZsprite.png")
        self.image.set_colorkey((255,255,255))
        self.image.convert_alpha()
        self.rect = self.image.get_rect()

class hojaSpriteBolsa(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Image/BOLSAsprite.png")
        self.image.set_colorkey((255,255,255))
        self.image.convert_alpha()
        self.rect = self.image.get_rect()

class hojaSpriteLata(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Image/LATASODAsprite.png")
        self.image.set_colorkey((0,0,0))
        self.image.convert_alpha()
        self.rect = self.image.get_rect()

class hojaSpriteBotella(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Image/BOTELLAsprite.png")
        self.image.set_colorkey((0,0,0))
        self.image.convert_alpha()
        self.rect = self.image.get_rect()