
# *** Wenn die Schildkröte auf der andern Seite angekommen ist, soll sie wieder in die Ausgangsstellung versetzt werden
# für die nächste Runde.

# Entschuldigung für das Missverständnis. Hier ist das aktualisierte Skript, in dem sich die Schildkröte vertikal
# bewegt, die Autos sich horizontal bewegen und die Schildkröte nach dem Erreichen der anderen Seite in die
# Ausgangsposition zurückgesetzt wird:

# ```python
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
            for car in cars:
                car.goto(random.randint(-380, 380), random.randint(-200, 200))

        # Autos zurücksetzen
        if car.xcor() < -400:
            car.goto(random.randint(400, 800), random.randint(-200, 200))
# ```

# In dieser Version wird die Schildkröte nach dem Erreichen der anderen Seite in die Ausgangsposition zurückgesetzt,
# indem ihre Y-Koordinate auf -250 gesetzt wird. Zudem werden die Autos ebenfalls zufällig neu positioniert,
# indem sie an zufällige X- und Y-Koordinaten gesetzt werden.