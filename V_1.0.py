import pygame, sys, random, time

# Inicializar Pygame
pygame.init()

# Definir colores modernos
morado = (128, 0, 128)
naranja = (255, 165, 0)
WHITE = (255, 255, 255)
gris_claro = (240, 240, 240)
BLACK = (0, 0, 0)
amarillo = (255, 223, 0)  # Color amarillo para botones
gris_oscuro = (169, 169, 169)

# Fuente
font = pygame.font.Font(None, 36)


# Tamaño de la ventana
ancho = 800
alto = 800

# Configuración de screen
screen = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption('Juego con Login y Menú')

# Fuente
fuente = pygame.font.SysFont('Arial', 30)
fuente_grande = pygame.font.SysFont('Arial', 50)
fuente_extra_grande = pygame.font.SysFont('Arial', 70)

# clock para controlar los FPS
clock = pygame.time.Clock()

# Variables para controlar el volumen
volumen = 0.3

# Cargar música y reproducirla
songs = ['Song1.mp3', 'Song2.mp3']
song_ind = 0
pygame.mixer.music.load('Song1.mp3')
pygame.mixer.music.set_volume(volumen)
pygame.mixer.music.play(-1, 0.0)
# Funciónes para cambiar de cancion
def siguiente_song():
    global song_ind
    song_ind += 1
    pygame.mixer.music.load(songs[song_ind])
    pygame.mixer.music.play()
def anterior_song():
    global song_ind
    if (song_ind > 0):
        song_ind -= 1
        pygame.mixer.music.load(songs[song_ind])
        pygame.mixer.music.play()


# Variables del juego
f_obj = []
pts = 0
vel = 4
mult = 1
multm = 0
keys = [pygame.K_LEFT, pygame.K_UP, pygame.K_DOWN, pygame.K_RIGHT]
key_positions = [100, 200, 300, 400]
p_icombo = (585, 187) 
# Cargar imágenes personalizadas
image_paths = ['f1.png', 'f2.png', 'f3.png', 'f4.png']
img_combos = ['c1.png', 'c2.png', 'c3.png']
# lista con localizacion de imagenes
images = [pygame.image.load(path) for path in image_paths]
x_combos = [pygame.image.load(path) for path in img_combos]
#recursos
#sonidos
sonido1= pygame.mixer.Sound('fail3.ogg')
sonido2= pygame.mixer.Sound('fail2.mp3')
#imagenes
fondo= pygame.image.load('Fondo.jpg').convert()
fondo1= pygame.image.load('Fondo1.jpg').convert()
fondo3= pygame.image.load('Fondo3.jpg').convert()

# Función para dibujar texto con sombra difusa y borde 3D
def dibujar_texto_con_sombra(texto, fuente, color, sombra_color, x, y, sombra_offset=(5, 5)):
    sombra = fuente.render(texto, True, sombra_color)
    screen.blit(sombra, (x + sombra_offset[0], y + sombra_offset[1]))
    texto_renderizado = fuente.render(texto, True, color)
    screen.blit(texto_renderizado, (x, y))


# Función para crear un botón 3D con color amarillo, borde y efectos
def dibujar_boton_3d(texto, x, y, ancho, alto, color_base, color_hover, color_click):
    mouse_x, mouse_y = pygame.mouse.get_pos()
    boton = pygame.Rect(x, y, ancho, alto)
    
    if boton.collidepoint(mouse_x, mouse_y):
        if pygame.mouse.get_pressed()[0]:
            pygame.draw.rect(screen, color_click, boton, border_radius=30)  # Efecto clic
        else:
            pygame.draw.rect(screen, color_hover, boton, border_radius=30)  # Efecto hover
    else:
        pygame.draw.rect(screen, color_base, boton, border_radius=30)

    # Sombra y relieve 3D
    pygame.draw.rect(screen, gris_claro, boton, 4)  # Borde difuso 3D
    texto_renderizado = fuente.render(texto, True, WHITE)
    texto_rect = texto_renderizado.get_rect(center=boton.center)
    screen.blit(texto_renderizado, texto_rect.topleft)  # Centrado del texto

    return boton


# screen de Menú Principal
def menu_principal():
    while True:
        screen.blit(fondo1, [0, 0])
        dibujar_texto_con_sombra('Menú Principal', fuente_extra_grande, WHITE, BLACK, 250, 100)

        # Botones: Iniciar Juego, Opciones, Salir
        boton_jugar = dibujar_boton_3d('Iniciar Juego', 300, 200, 200, 50, amarillo, gris_claro, WHITE)
        boton_opciones = dibujar_boton_3d('Opciones', 300, 270, 200, 50, amarillo, gris_claro, WHITE)
        boton_salir = dibujar_boton_3d('Salir', 300, 340, 200, 50, amarillo, gris_claro, WHITE)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if boton_jugar.collidepoint(evento.pos):
                    return 'juego'
                elif boton_opciones.collidepoint(evento.pos):
                    return 'opciones'
                elif boton_salir.collidepoint(evento.pos):
                    pygame.quit()
                    sys.exit()

            # Verificar si la tecla Esc fue presionada
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    return 'menu_principal'  # Regresa al menú principal

        pygame.display.flip()
        clock.tick(60)

# Pantalla de Opciones (ajuste de volumen)
def opciones():
    global volumen
    while True:
        screen.blit(fondo3, [0, 0])

        dibujar_texto_con_sombra('Ajuste de Volumen', fuente_extra_grande, WHITE, BLACK, 100, 90)

        # Botones de volumen
        boton_volumen_up = dibujar_boton_3d('Subir Volumen', 300, 200, 200, 50, amarillo, gris_claro, WHITE)
        boton_volumen_down = dibujar_boton_3d('Bajar Volumen', 300, 270, 200, 50, amarillo, gris_claro, WHITE)
        boton_volver = dibujar_boton_3d('Volver al Menú', 300, 340, 200, 50, amarillo, gris_claro, WHITE)

        # Texto de volumen alineado
        dibujar_texto_con_sombra(f'Volumen: {int(volumen * 100)}%', fuente, WHITE, BLACK, 310, 160)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if boton_volumen_up.collidepoint(evento.pos):
                    if volumen < 1.0:
                        volumen += 0.1
                        pygame.mixer.music.set_volume(volumen)
                elif boton_volumen_down.collidepoint(evento.pos):
                    if volumen > 0.0:
                        volumen -= 0.1
                        pygame.mixer.music.set_volume(volumen)
                elif boton_volver.collidepoint(evento.pos):
                    return 'menu_principal'  # Regresar al menú principal

            # Verificar si la tecla Esc fue presionada
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    return 'menu_principal'  # Regresa al menú principal

        pygame.display.flip()
        clock.tick(60)
def pantalla_final():
    end= True
    while True:
        screen.blit(fondo3, [0, 0])
        f_score_text = font.render(f'Puntaje final: {pts}', True, WHITE)
        combo_text = font.render(f'Combo Maximo: x{multm}', True, WHITE)
        screen.blit(f_score_text, (ancho // 2, alto // 2-100))
        screen.blit(combo_text, (ancho // 2, alto // 2))
        pygame.display.flip()
        pygame.time.wait(5000)

    
# Función para crear un nuevo bloque
def crear_obj():
    key_index = random.randint(0, 3)
    obj = {
        'img': images[key_index],
        'pos': [key_positions[key_index], 0],
        'key': keys[key_index]
    }
    f_obj.append(obj)

# Función para dibujar los bloques
def dbj_obj():
    for obj in f_obj :
        screen.blit(obj['img'], obj['pos'])

# Función para dibujar la línea de llegada
def dbj_linea():
    pygame.draw.line(screen, BLACK, (0, 700), (550, 700), 5)

# Función para mostrar el puntaje
def dbj_pts():
    score_text = font.render(f'Puntaje: {pts}', True, WHITE)
    combo_text = font.render(f'Combo: x{mult}', True, WHITE)
    screen.blit(score_text, (600, 550))
    screen.blit(combo_text, (600, 600))
def img_combo():
    global mult
    if(mult<10):
        c = 0
    if(mult>9) and (mult<20):
        c = 1
    elif (mult==20):
        c = 2

    screen.blit(x_combos[c], p_icombo)
    
def iniciar_juego():
    global pts, mult, multm, combo
    jugando= True
    while jugando:
        screen.blit(fondo, [0, 0])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                anterior_song()
                jugando= False
            if event.type == pygame.KEYDOWN:
                combo = False
                for obj in f_obj[:]:
                    if abs(obj['pos'][1] - 680) <= 40:
                        if event.key == obj['key']:
                                pts += 1 * mult
                                if(mult<20):
                                    mult += 1
                                    multm += 1
                                f_obj.remove(obj)
                                hit = True
                                combo= True
                        if not combo:
                            mult = 1
                            pygame.mixer.Sound.set_volume
                            sonido1.play()
                
        # Crear nuevos bloques
        if pygame.mixer.music.get_busy():
            if random.randint(0, 100) < 3:  
                crear_obj()
        if not pygame.mixer.music.get_busy():
            screen.blit(fondo3, [0, 0])
            f_score_text = font.render(f'Puntaje final: {pts}', True, WHITE)
            combo_text = font.render(f'Combo Maximo: x{multm}', True, WHITE)
            screen.blit(f_score_text, (ancho // 2, alto // 2-100))
            screen.blit(combo_text, (ancho // 2, alto // 2))
            pygame.display.flip()
            anterior_song()
            pygame.time.wait(5000)
            jugando= False
                
        # Mover los bloques hacia abajo
        for obj in f_obj:
            obj['pos'][1] += vel 
            if obj['pos'][1] > alto:
                f_obj.remove(obj)
                mult = 1
                sonido2.play()
                
        # Dibujar todo
        img_combo()
        dbj_obj()
        dbj_linea()
        dbj_pts()
        # Actualizar la pantalla
        pygame.display.flip()
        clock.tick(60)
        

# Función principal
while True: 
    opcion = menu_principal()
    if opcion == 'juego':
        siguiente_song()
        iniciar_juego()
    elif opcion == 'opciones':
            opciones()
    # Actualizar la pantalla
    pygame.display.flip()
    clock.tick(60)


