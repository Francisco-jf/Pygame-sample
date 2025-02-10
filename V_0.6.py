import pygame, sys, random

pygame.init()
pygame.mixer.init()

# Configuración de la pantalla
alto, ancho = 800, 800
screen = pygame.display.set_mode((alto, ancho))
pygame.display.set_caption("Muevelo BB")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (210, 0, 0)
GREEN = (0, 210, 0)
BLUE = (0, 175, 255)
ORANGE = (255, 145, 0)
# Fuente
font = pygame.font.Font(None, 36)

# Reloj
clock = pygame.time.Clock()

# Variables del juego
f_obj = []
pts = 0
vel = 4
mult= 1
keys = [pygame.K_LEFT, pygame.K_UP, pygame.K_DOWN, pygame.K_RIGHT]
key_positions = [100, 200, 300, 400]
# Cargar imágenes personalizadas
image_paths = ["f1.png", "f2.png", "f3.png", "f4.png"]
# Reemplaza con tus rutas de imágenes
images = [pygame.image.load(path) for path in image_paths]

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
    score_text = font.render(f"Puntaje: {pts}", True, WHITE)
    combo_text = font.render(f"Combo: x{mult}", True, WHITE)
    screen.blit(score_text, (600, 550))
    screen.blit(combo_text, (600, 600))

#recursos
#sonidos
sonido1= pygame.mixer.Sound('fail3.ogg')
sonido2= pygame.mixer.Sound('fail2.mp3')
#musica
pygame.mixer.music.load('Song1.mp3')
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play()
#imagenes
fondo= pygame.image.load('Fondo.jpg').convert()
#gif1= pygame.image.load('gif1.gif')
#juego
jugando = True
while jugando:
    screen.blit(fondo, [0, 0])
    #screen.blit(gif1, [590, 170])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando= False
        if event.type == pygame.KEYDOWN:
            combo = False
            for obj in f_obj[:]:
                if abs(obj['pos'][1] - 680) <= 40:
                    if event.key == obj['key']:
                        pts += 1 * mult
                        mult += 1 
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
    # Mover los bloques hacia abajo
    for obj in f_obj:
        obj['pos'][1] += vel 
        if obj['pos'][1] > alto:
            f_obj.remove(obj)
            mult = 1
            sonido2.play()
    
    # Dibujar todo
    dbj_obj()
    dbj_linea()
    dbj_pts()
    
    # Actualizar la pantalla
    pygame.display.flip()
    clock.tick(60)
    #verificar cancion

# Salir del juego
pygame.quit()
sys.exit()
