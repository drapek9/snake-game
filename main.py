# Importy
from turtle import Turtle, Screen
import random
import time

# List_připomínek
prip_list = ["Unlucky"]

# Definice random
def random_number(n1, n2):
    the_number = random.randint(n1, n2)
    return the_number

# Obrazovka, hlava a jablko a dva titulky
my_screen = Screen()
my_screen.bgcolor("green")
my_screen.setup(500, 500)
my_screen.tracer(False)

head = Turtle("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.speed(0)

apple = Turtle("circle")
apple.penup()
apple.color("red")
x = random_number(-230, 230)
y = random_number(-230, 230)
apple.goto(x, y)

titule = Turtle()
titule.penup()
titule.speed(0)
titule.color("white")
titule.hideturtle()
titule.goto(0, 225)
titule.write("Skóre: 0  Nejvyšší skóre: 0", align= "center", font=("arial", 10))

titule2 = Turtle()
titule2.penup()
titule2.speed(0)
titule2.color("black")
titule2.hideturtle()
titule2.goto(0, -225)

# Definice směru hry
head.direction = "stop"
def game():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

def move_up():
    if head.direction != "down":
        head.direction = "up"
def move_down():
    if head.direction != "up":
        head.direction = "down"
def move_left():
    if head.direction != "right":
        head.direction = "left"
def move_right():
    if head.direction != "left":
        head.direction = "right"

# 4ekání na zmáčknutí tlačítka
my_screen.listen()
my_screen.onkeypress(move_up, "w")
my_screen.onkeypress(move_down, "s")
my_screen.onkeypress(move_left, "a")
my_screen.onkeypress(move_right, "d")

# Proměnné pro hru
score = 0
highest_score = 0
list_body = []
ahoj = "No"

# While pro hru
while True:
    # Hlášky podmínka
    if head.xcor() < -235 or head.xcor() > 235 or head.ycor() < -235 or head.ycor() > 235 or ahoj == "Yes":
        ra = prip_list[random_number(0, len(prip_list)-1)]
        titule2.write(f"{ra}", align= "center", font= ("arial", 20))
    my_screen.update()
    # Podmínka pro smrt
    if head.xcor() < -235 or head.xcor() > 235 or head.ycor() < -235 or head.ycor() > 235 or ahoj == "Yes":
        time.sleep(2)
        titule2.clear()
        head.direction = "stop"
        ahoj = "No"
        x = random_number(-230, 230)
        y = random_number(-230, 230)
        apple.goto(x, y)
        head.goto(0, 0)

        score = 0
        titule.clear()
        titule.write(f"Skóre: {score}  Nejvyšší skóre: {highest_score}", align= "center", font=("arial", 10))

        for one_body in list_body:
            one_body.goto(1000, 1000)
        list_body.clear()
    # Snězení jablka
    if head.distance(apple) < 20:
        new_body = Turtle("square")
        new_body.color("grey")
        new_body.penup()
        new_body.speed(0)
        list_body.append(new_body)

        x = random_number(-230, 230)
        y = random_number(-230, 230)
        apple.goto(x, y)
        score += 1
        if score > highest_score:
            highest_score = score
        titule.clear()
        titule.write(f"Skóre: {score}  Nejvyšší skóre: {highest_score}", align= "center", font=("arial", 10))

    # Připojení těla (bez nultýho)
    for index in range(len(list_body)-1, 0, -1):
        x = list_body[index-1].xcor()
        y = list_body[index-1].ycor()
        list_body[index].goto(x, y)

    # Přípojení nultýho těla k hlavě
    if len(list_body) > 0:
        x = head.xcor()
        y = head.ycor()
        list_body[0].goto(x, y)
    game()
    # Narazení do sebe
    for one_body in list_body:
        if head.distance(one_body) < 20:
            ahoj = "Yes"
    time.sleep(0.1)

my_screen.onscreenclick()