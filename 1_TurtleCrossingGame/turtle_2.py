# *** Die Autos müssen sich horizontal bewegen

# Entschuldigung für das Missverständnis. Hier ist das aktualisierte Skript,
# in dem sich die Schildkröte vertikal bewegt und die Autos sich horizontal bewegen:

import turtle
import random

# Fenster einrichten
window = turtle.Screen()
window.title("Turtle Crossing")
window.setup(width=800, height=600)
window.tracer(0)

# Schildkröte erstellen
player = turtle.Turtle()
player.shape("turtle")
player.color("green")
player.penup()
player.goto(0, -250)

# Spielerbewegungen
def move_up():
    y = player.ycor()
    if y < 250:
        y += 20
        player.sety(y)

# ***
# Spieler kann zurückgehen, was nicht den Voraussetzungen entspricht
# ***

def move_down():
    y = player.ycor()
    if y > -250:
        y -= 20
        player.sety(y)

# Autos erstellen
cars = []
colors = ["red", "blue", "orange", "purple", "pink", "yellow"]
for _ in range(10):
    car = turtle.Turtle()
    car.shape("square")
    car.color(random.choice(colors))
    car.penup()
    car.shapesize(stretch_wid=1, stretch_len=2)
    x = random.randint(-380, 380)
    y = random.randint(-200, 200)
    car.goto(x, y)
    cars.append(car)

# Spiel-Ende
def game_over():
    player.goto(0, -250)
    player.color("red")

# Tastatursteuerung
window.listen()
window.onkeypress(move_up, "Up")
window.onkeypress(move_down, "Down")

# Spiel-Loop
speed = 0.1
while True:
    window.update()

    # Autos bewegen
    # ****
    # Autos bewegen sich korrekt
    # ***
    for car in cars:
        x = car.xcor()
        x -= speed
        car.setx(x)

        # Kollision mit Spieler überprüfen
        if car.distance(player) < 20:
            game_over()
            speed = 0

        # Spieler hat die andere Seite erreicht
        # ***
        # Zürücksetzen Spiele funktioniert nicht
        # ***
        if player.ycor() > 250:
            player.goto(0, -250)
            speed += 0.01

        # Autos zurücksetzen
        if car.xcor() < -400:
            x = random.randint(400, 800)
            y = random.randint(-200, 200)
            car.goto(x, y)

# In dieser Version bewegt sich die Schildkröte vertikal mit den Pfeiltasten "Up" und "Down", während die Autos
# horizontal von rechts nach links über den Bildschirm fahren. Der Rest des Codes bleibt unverändert.