# *** Die Schildkröte soll sich vertikal bewegen, nicht horizontal

# Entschuldigung für das Missverständnis. Hier ist das aktualisierte Skript,
# in dem sich die Schildkröte vertikal bewegt:

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

# ***
# Korrektur move_up / move_down anstatt move_left  / move_right
# ***
def move_up():
    y = player.ycor()
    if y < 250:
        y += 20
        player.sety(y)

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
    car.goto(x, 250)
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
    # ***
    # Fälschlicherweise werden nun die Autos in der y-Aches bewegt!
    # ***
    for car in cars:
        y = car.ycor()
        y -= speed
        car.sety(y)

        # Kollision mit Spieler überprüfen
        if car.distance(player) < 20:
            game_over()
            speed = 0

        # Spieler hat die andere Seite erreicht
        if player.ycor() > 250:
            player.goto(0, -250)
            speed += 0.01

        # Autos zurücksetzen
        if car.ycor() < -260:
            x = random.randint(-380, 380)
            car.goto(x, 250)

# In dieser Version bewegt sich die Schildkröte vertikal mit den Pfeiltasten "Up" und "Down".
# Die Autos werden horizontal generiert und bewegen sich von oben nach unten über den Bildschirm.
# Der Rest des Codes bleibt unverändert.

