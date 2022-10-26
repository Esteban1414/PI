import sys, pygame, random, clases
pygame.init()
pygame.mixer.init()
#Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#Puntuacion del juego
puntuation = 0

#Dibujar texto, la puntuacion.
def draw_text(surface, text, size, x, y):
    font = pygame.font.SysFont("serif", size)
    text_surface = font. render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surface.blit(text_surface, text_rect)

#constantes
largoX = 700
altoY = 394
pygame.display.set_caption("FARWATER")
ventana = pygame.display.set_mode((largoX,altoY))

#constantes Rio
rioList = []
rioTimer = pygame.time.get_ticks()
rioCooldown = 200
rioFrame = 0

#constantes Pez2
pez2Timer = pygame.time.get_ticks()
pez2Cooldown = 470

#constantes Pez
pezTimer = pygame.time.get_ticks()
pezCooldown = 450

#constantes Llanta
llantaTimer = pygame.time.get_ticks()
llantaCooldown = 550

#constantes Bolsa
bolsaTimer = pygame.time.get_ticks()
bolsaCooldown = 500

#constantes Lata
lataTimer = pygame.time.get_ticks()
lataCooldown = 530

#constantes Botella
botellaTimer = pygame.time.get_ticks()
botellaCooldown = 500

#===============================IMAGEN RIO================================
rioImagen = clases.imagenes.imagen("Image/FONDOsprite.png")
rio = clases.hojaSpriteRio(rioImagen)

for i in range (20):
   rioList.append(clases.hojaSpriteRio.obtener_rio(rio,i,largoX,altoY))
#===============================IMAGEN PEZ2=============================
pez2List = pygame.sprite.Group()
pez2TodaListsprite = pygame.sprite.Group()
for i in range(1):
    pez2 = clases.hojaSpritePez2()
    pez2.rect.x = -32
    pez2.rect.y = random.randint(215,350)
    pez2List.add(pez2)
    pez2TodaListsprite.add(pez2)
#===============================IMAGEN BOLSA=============================
bolsaList = pygame.sprite.Group()
bolsaTodaListsprite = pygame.sprite.Group()
for i in range(1):
    bolsa = clases.hojaSpriteBolsa()
    bolsa.rect.x = -32
    bolsa.rect.y = random.randint(215,350)
    bolsaList.add(bolsa)
    bolsaTodaListsprite.add(bolsa)

#===============================IMAGEN SODA=============================
sodaList = pygame.sprite.Group()
sodaTodaListsprite = pygame.sprite.Group()
for i in range(1):
    soda = clases.hojaSpriteLata()
    soda.rect.x = -32
    soda.rect.y = random.randint(215,350)
    sodaList.add(soda)
    sodaTodaListsprite.add(soda)

#===============================IMAGEN BOTELLA=============================
botellaList = pygame.sprite.Group()
botellaTodaListsprite = pygame.sprite.Group()
for i in range(1):
    botella = clases.hojaSpriteBotella()
    botella.rect.x = -32
    botella.rect.y = random.randint(215,350)
    botellaList.add(soda)
    botellaTodaListsprite.add(botella)

#===============================IMAGEN PEZ=============================
pezList = pygame.sprite.Group()
pezTodaListsprite = pygame.sprite.Group()
for i in range(1):
    pez = clases.hojaSpritePez()
    pez.rect.x = -32
    pez.rect.y = random.randint(215,350)
    pezList.add(pez)
    pezTodaListsprite.add(pez)

#===============================IMAGEN LLANTA=============================
llantaList = pygame.sprite.Group()
llantaTodaListsprite = pygame.sprite.Group()
for i in range(1):
    llanta = clases.hojaSpriteLlanta()
    llanta.rect.x = -32
    llanta.rect.y = random.randint(215,350)
    llantaList.add(pez)
    llantaTodaListsprite.add(llanta)


#MUSICA DEL JUEGO
pygame.mixer.music.load('Music/musica1.mp3')
#SONIDOS
Sonido_Basura=pygame.mixer.Sound('Music/Basura.mp3')
Sonido_Pez=pygame.mixer.Sound('Music/Peces.mp3')
pygame.mixer.music.play(loops=-1)

#===============================MAIN WHILE================================
while_1 = False
while not while_1:
    #Valores de Tiempo
    tempo=pygame.time.get_ticks()//1000 #Muestra segundos
    tiempo_paso = pygame.time.get_ticks()
    ventana.fill((255,255,255))

    #====================RIO====================
    if tiempo_paso - rioTimer >= rioCooldown:
        rioFrame += 1
        rioTimer = tiempo_paso
        if rioFrame >= len(rioList):
            rioFrame = 0
    ventana.blit(rioList[rioFrame], (0,0))

    #===================PEZ===================
    if tiempo_paso - pezTimer >= pezCooldown:
        pez.rect.x += 34
        pezTimer = tiempo_paso
        if pez.rect.x >= 740:
            pez.rect.x =-34
            pez.rect.y = random.randint(215,350)
    pezTodaListsprite.draw(ventana)

#====================PEZ 2====================
    if tiempo_paso - pez2Timer >= pez2Cooldown:
        pez2.rect.x += 34
        pez2Timer = tiempo_paso
        if pez2.rect.x >= 740:
            pez2.rect.x =-34
            pez2.rect.y = random.randint(215,350)
    pez2TodaListsprite.draw(ventana)

    #===================BOLSA===================
    if tiempo_paso - bolsaTimer >= bolsaCooldown:
        bolsa.rect.x += 34
        bolsaTimer = tiempo_paso
        if bolsa.rect.x >= 740:
            bolsa.rect.x =-34
            bolsa.rect.y = random.randint(215,350)
    bolsaTodaListsprite.draw(ventana)

 #===================LLANTA==================
    if tiempo_paso - llantaTimer >= llantaCooldown:
        llanta.rect.x += 34
        llantaTimer = tiempo_paso
        if llanta.rect.x >= 740:
            llanta.rect.x =-34
            llanta.rect.y = random.randint(215,350)
    llantaTodaListsprite.draw(ventana)

    #===================LATA===================
    if tiempo_paso - lataTimer >= lataCooldown:
        soda.rect.x += 34
        lataTimer = tiempo_paso
        if soda.rect.x >= 740:
            soda.rect.x =-34
            soda.rect.y = random.randint(215,350)
    sodaTodaListsprite.draw(ventana)

    #===================BOTELLA===================
    if tiempo_paso - botellaTimer >= botellaCooldown:
        botella.rect.x += 34
        botellaTimer = tiempo_paso
        if botella.rect.x >= 740:
            botella.rect.x =-34
            botella.rect.y = random.randint(215,350)
    botellaTodaListsprite.draw(ventana)  

    #Mostrar puntuacion en pantalla
    Score= pygame.font.SysFont("Times New Roman", 24)
    contador = Score.render("Score: "+str(puntuation),100,(255,255,255))
    ventana.blit(contador,(300,-1))

    #Mostrar tiempo en pantalla
    letra= pygame.font.SysFont("Times New Roman", 23)
    let = letra.render("Tiempo: "+str(tempo),100,(255,255,255))
    ventana.blit(let,(590,-1))

    #Imagen del bote de basura
    botbasura=pygame.image.load("Image/botbasura.png").convert_alpha()
    ventana.blit(botbasura,(625,80))

#Condicion del tiempo
    if tempo==90:
        while_1 = True
    for event in pygame.event.get():
        #Posicion del mouse
        mouse_pos = pygame.mouse.get_pos()
        x = mouse_pos[0]
        y = mouse_pos[1]
        r1= pygame.draw.rect(ventana, WHITE, (x, y, 1, 1))
        #Creamos un rectangulo
#=========================COLISIONES=============================
    if event.type==pygame.MOUSEBUTTONDOWN:
        if r1.colliderect(soda):
                Sonido_Basura.play()
                puntuation+=1
                if puntuation==10:
                    while_1 = True
                soda.rect.x=500
                soda.rect.y=500
        if event.type==pygame.MOUSEBUTTONDOWN:
            if r1.colliderect(bolsa):      
                Sonido_Basura.play()
                puntuation+=1
                if puntuation>=10:
                    while_1 = True
                bolsa.rect.x=500
                bolsa.rect.y=500
        if event.type==pygame.MOUSEBUTTONDOWN:
            if r1.colliderect(botella):
                Sonido_Basura.play()
                puntuation+=1
                if puntuation==10:
                    while_1 = True
                botella.rect.x=500
                botella.rect.y=500
        if event.type==pygame.MOUSEBUTTONDOWN:
            if r1.colliderect(llanta):
                Sonido_Basura.play()
                puntuation+=1
                if puntuation==10:
                    while_1 = True
                llanta.rect.x=500
                llanta.rect.y=500
        if event.type==pygame.MOUSEBUTTONDOWN:
            if r1.colliderect(pez):
                Sonido_Pez.play()
                puntuation-=1
                if puntuation<0:
                    while_1 = True
                pez.rect.x=550
                pez.rect.y=550       
        if event.type==pygame.MOUSEBUTTONDOWN:
            if r1.colliderect(pez2):
                Sonido_Pez.play()
                puntuation-=1
                if puntuation<0:
                    while_1 = True
                pez2.rect.x=550
                pez2.rect.y=550       
    if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit()
    pygame.display.flip()