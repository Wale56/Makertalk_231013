# *** Ist es möglich die 'Autos' realisitscher dazustellen (z.B. Sprites, 3d Klötze)?

# Ja, es ist möglich, die "Autos" realistischer darzustellen, zum Beispiel durch Verwendung von Sprites oder
# 3D-Modellen. Allerdings würde dies erheblich komplexere Grafikbibliotheken erfordern, die über die
# Standard-Turtle-Grafiken in Python hinausgehen.
#
# Eine Möglichkeit, realistischere Grafiken zu verwenden, besteht darin, eine Bibliothek wie Pygame oder Pyglet zu
# verwenden, die fortschrittlichere Grafik- und Spieleentwicklungsfunktionen bietet. Hier ist ein einfaches Beispiel
# mit Pygame:
#
# python

import pygame
import random

pygame.init()

# Fenster einrichten
window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Turtle Crossing")

# Farben
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Schildkröte erstellen
player_image = pygame.image.load("turtle.png")  # Laden Sie ein Bild für die Schildkröte
player_rect = player_image.get_rect()
player_rect.center = (400, 550)
player_speed = 5

# Autos erstellen
car_images = [pygame.image.load("car1.png"), pygame.image.load("car2.png"), pygame.image.load("car3.png")]
cars = []
car_speed = 3

for _ in range(10):
    car_image = random.choice(car_images)
    car_rect = car_image.get_rect()
    car_rect.x = random.randint(0, 800)
    car_rect.y = random.randint(100, 500)
    cars.append((car_image, car_rect))

# Spiel-Loop
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player_rect.y -= player_speed

    window.fill(WHITE)

    # Autos bewegen
    for car_image, car_rect in cars:
        car_rect.x -= car_speed
        if car_rect.right < 0:
            car_rect.x = 800
            car_rect.y = random.randint(100, 500)

        window.blit(car_image, car_rect)

    window.blit(player_image, player_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

# In diesem Beispiel verwenden wir Pygame, um ein einfaches Spiel zu erstellen, in dem die Schildkröte und die Autos
# realistischere Grafiken verwenden. Sie müssen Grafiken für die Schildkröte und die Autos erstellen und die
# Dateinamen entsprechend anpassen.
#
# Dies ist nur ein einfaches Beispiel, und die Integration von 3D-Modellen oder komplexeren Grafiken erfordert
# möglicherweise eine umfangreichere Entwicklung mit spezialisierten 3D-Grafikbibliotheken.
