import pygame
import sys
import time

# Inicializar Pygame
pygame.init()

# Definir colores modernos
morado = (128, 0, 128)
naranja = (255, 165, 0)
blanco = (255, 255, 255)
gris_claro = (240, 240, 240)
negro = (0, 0, 0)
amarillo = (255, 223, 0)  # Color amarillo para botones
gris_oscuro = (169, 169, 169)

# Tamaño de la ventana
ANCHO = 800
ALTO = 600

# Configuración de pantalla
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juego con Login y Menú")

# Fuente
fuente = pygame.font.SysFont("Arial", 30)
fuente_grande = pygame.font.SysFont("Arial", 50)
fuente_extra_grande = pygame.font.SysFont("Arial", 70)

# Reloj para controlar los FPS
reloj = pygame.time.Clock()

# Variables para controlar el volumen
volumen = 0.5  # Volumen inicial (rango 0.0 a 1.0)

# Cargar música y reproducirla
pygame.mixer.music.load("Song1.mp3")  # Asegúrate de colocar el archivo MP3 en la ruta correcta
pygame.mixer.music.set_volume(volumen)
pygame.mixer.music.play(-1, 0.0)  # Reproduce música en bucle

# Función para dibujar texto con sombra difusa y borde 3D
def dibujar_texto_con_sombra(texto, fuente, color, sombra_color, x, y, sombra_offset=(5, 5)):
    sombra = fuente.render(texto, True, sombra_color)
    pantalla.blit(sombra, (x + sombra_offset[0], y + sombra_offset[1]))  # Sombra más difusa
    texto_renderizado = fuente.render(texto, True, color)
    pantalla.blit(texto_renderizado, (x, y))

# Función para crear un fondo con gradiente moderno
def fondo_difuminado():
    for i in range(ANCHO):
        r = int((naranja[0] - morado[0]) * (i / ANCHO) + morado[0])
        g = int((naranja[1] - morado[1]) * (i / ANCHO) + morado[1])
        b = int((naranja[2] - morado[2]) * (i / ANCHO) + morado[2])
        pygame.draw.line(pantalla, (r, g, b), (i, 0), (i, ALTO))

# Función para crear un botón 3D con color amarillo, borde y efectos
def dibujar_boton_3d(texto, x, y, ancho, alto, color_base, color_hover, color_click):
    mouse_x, mouse_y = pygame.mouse.get_pos()
    boton = pygame.Rect(x, y, ancho, alto)
    
    if boton.collidepoint(mouse_x, mouse_y):
        if pygame.mouse.get_pressed()[0]:
            pygame.draw.rect(pantalla, color_click, boton, border_radius=30)  # Efecto clic
        else:
            pygame.draw.rect(pantalla, color_hover, boton, border_radius=30)  # Efecto hover
    else:
        pygame.draw.rect(pantalla, color_base, boton, border_radius=30)

    # Sombra y relieve 3D
    pygame.draw.rect(pantalla, gris_claro, boton, 4)  # Borde difuso 3D
    texto_renderizado = fuente.render(texto, True, blanco)
    texto_rect = texto_renderizado.get_rect(center=boton.center)
    pantalla.blit(texto_renderizado, texto_rect.topleft)  # Centrado del texto

    return boton

# Función de transición con desvanecimiento
def transicion_desvanecimiento_suave():
    for alpha in range(0, 255, 15):  # Aumentamos la opacidad
        pantalla.fill(negro)
        pygame.draw.rect(pantalla, (0, 0, 0, alpha), (0, 0, ANCHO, ALTO))  # Transición de opacidad
        pygame.display.update()
        reloj.tick(60)
    time.sleep(0.3)  # Pausa para dar tiempo a que el efecto sea visible

def transicion_desvanecimiento_reversa():
    for alpha in range(255, 0, -15):  # Reducimos la opacidad
        pantalla.fill(negro)
        pygame.draw.rect(pantalla, (0, 0, 0, alpha), (0, 0, ANCHO, ALTO))
        pygame.display.update()
        reloj.tick(60)
    time.sleep(0.3)

# Función para iniciar la pantalla de Login
def pantalla_login():
    usuario = ""
    caja_usuario = pygame.Rect(300, 200, 200, 40)
    while True:
        fondo_difuminado()
        dibujar_texto_con_sombra("Ingrese Usuario", fuente_extra_grande, blanco, negro, 200, 120)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_BACKSPACE:
                    if len(usuario) > 0:
                        usuario = usuario[:-1]
                elif evento.key == pygame.K_RETURN:
                    return "menu_principal"  # No se valida el nombre de usuario, pasa al menú principal
                else:
                    if len(usuario) < 15:
                        usuario += evento.unicode

        pygame.draw.rect(pantalla, blanco, caja_usuario, 2)
        dibujar_texto_con_sombra("Usuario:", fuente, blanco, negro, 200, 200)
        dibujar_texto_con_sombra(usuario, fuente, blanco, negro, 310, 210)

        pygame.display.flip()
        reloj.tick(60)

# Pantalla de Menú Principal
def menu_principal():
    while True:
        fondo_difuminado()
        dibujar_texto_con_sombra("Menú Principal", fuente_extra_grande, blanco, negro, 250, 100)

        # Botones: Iniciar Juego, Opciones, Salir
        boton_jugar = dibujar_boton_3d("Iniciar Juego", 300, 200, 200, 50, amarillo, gris_claro, blanco)
        boton_opciones = dibujar_boton_3d("Opciones", 300, 270, 200, 50, amarillo, gris_claro, blanco)
        boton_salir = dibujar_boton_3d("Salir", 300, 340, 200, 50, amarillo, gris_claro, blanco)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if boton_jugar.collidepoint(evento.pos):
                    return "juego"
                elif boton_opciones.collidepoint(evento.pos):
                    return "opciones"
                elif boton_salir.collidepoint(evento.pos):
                    pygame.quit()
                    sys.exit()

            # Verificar si la tecla Esc fue presionada
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    return "menu_principal"  # Regresa al menú principal

        pygame.display.flip()
        reloj.tick(60)

# Pantalla de Opciones (ajuste de volumen)
def opciones():
    global volumen
    while True:
        fondo_difuminado()

        dibujar_texto_con_sombra(" Ajuste de Volumen", fuente_extra_grande, blanco, negro,100,90)

        # Botones de volumen
        boton_volumen_up = dibujar_boton_3d("Subir Volumen", 300, 200, 200, 50, amarillo, gris_claro, blanco)
        boton_volumen_down = dibujar_boton_3d("Bajar Volumen", 300, 270, 200, 50, amarillo, gris_claro, blanco)
        boton_volver = dibujar_boton_3d("Volver", 300, 340, 200, 50, amarillo, gris_claro, blanco)

        # Texto de volumen alineado
        dibujar_texto_con_sombra(f"Volumen: {int(volumen * 100)}%", fuente, blanco, negro, 310, 160)

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
                    return "menu_principal"  # Regresar al menú principal

            # Verificar si la tecla Esc fue presionada
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    return "menu_principal"  # Regresa al menú principal

        pygame.display.flip()
        reloj.tick(60)

# Función principal (para comenzar el juego)
def main():
    while True:
        transicion_desvanecimiento_suave()
        pantalla_login()
        transicion_desvanecimiento_reversa()
        opcion = menu_principal()
        transicion_desvanecimiento_suave()
        
        if opcion == "juego":
            print("Juego comenzando...")
            # Aquí agregarás la lógica para iniciar el juego.
            # Esto puede incluir la pantalla del juego con más interacción.
            break
        
        opciones()

if __name__ == "__main__":
    main()
    
