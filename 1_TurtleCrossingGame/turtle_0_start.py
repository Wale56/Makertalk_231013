# Schreibe mir ein Skript für ein einfaches Spiel 'Turtle Crossing' in Python. Der Spieler steuert die Schildkröte,
# die nur vorwärts gehen kann, und es gibt eine ganze Reihe von zufällig generierten Autos,
# die horizontal über den Bildschirm fahren. Sobald der Spieler die andere Seite erreicht hat,
# beschleunigen die Autos leicht und der Spieler wird in die Ausgangsposition zurückgesetzt.
# Wenn die Schildkröte ein Auto streift, ist das Spiel vorbei.

# Natürlich! Hier ist ein Beispiel für ein einfaches Spiel namens "Turtle Crossing" in Python,
# das die von Ihnen beschriebenen Funktionen enthält:

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
def move_left():
    x = player.xcor()
    if x > -350:
        x -= 20
        player.setx(x)

def move_right():
    x = player.xcor()
    if x < 350:
        x += 20
        player.setx(x)

# Autos erstellen
cars = []
colors = ["red", "blue", "orange", "purple", "pink", "yellow"]
for _ in range(10):
    car = turtle.Turtle()
    car.shape("square")
# Demo Fehlersuche
    # CodeGPT -> Find Bugs
    # ausgeworfene Fehlermeldung in CodeGPT kopieren
    # Explain
    # car.color[random.choice(colors)]
    car.color(random.choice(colors))
    car.penup()
    car.shapesize(stretch_wid=1, stretch_len=2)
    y = random.randint(-200, 200)
    car.goto(400, y)
    cars.append(car)

# Spiel-Ende
def game_over():
    player.goto(0, -250)
    player.color("red")

# Tastatursteuerung
window.listen()
window.onkeypress(move_left, "Left")
window.onkeypress(move_right, "Right")

# Spiel-Loop
speed = 0.1
while True:
    window.update()

    # Autos bewegen
    for car in cars:
        x = car.xcor()
        x -= speed
        car.setx(x)

        # Kollision mit Spieler überprüfen
        if car.distance(player) < 20:
            game_over()
            speed = 0

        # Spieler hat die andere Seite erreicht
        if player.ycor() > 250:
            player.goto(0, -250)
            speed += 0.01

        # Autos zurücksetzen
        if car.xcor() < -400:
            y = random.randint(-200, 200)
            car.goto(400, y)

# Dieses Skript verwendet die Turtle-Grafikbibliothek, um das Spiel "Turtle Crossing" zu implementieren.
# Die Schildkröte wird mithilfe der Pfeiltasten gesteuert und muss Hindernissen (Autos) ausweichen,
# um die andere Seite zu erreichen. Das Spiel wird immer schneller, je öfter der Spieler die andere Seite erreicht.
# Wenn die Schildkröte ein Auto streift, ist das Spiel vorbei und die Schildkröte wird rot dargestellt.