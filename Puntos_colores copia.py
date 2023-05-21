
import random
import turtle as turtle_module

colour_list = ["green", "pink", "yellow", "blue", "brown"]
rgb_values = [
    (255, 0, 0),   # Rojo
    (0, 255, 0),   # Verde
    (0, 0, 255),   # Azul
    (255, 255, 0), # Amarillo
    (255, 0, 255), # Magenta
    (0, 255, 255)  # Cian
]
lapiz = turtle_module.Turtle()
lapiz.pensize(20)


def linea_recta():
    for x in range(10):
        color_random = random.choice(rgb_values)
        lapiz.pencolor((color_random[0] / 255, color_random[1] / 255, color_random[2] / 255))
        lapiz.forward(1)
        lapiz.penup()
        lapiz.forward(50)
        lapiz.down()


def subir():
    lapiz.penup()
    lapiz.back(510)
    lapiz.left(90)
    lapiz.forward(50)
    lapiz.right(90)
    lapiz.down()

lapiz.penup()
lapiz.back(250)
lapiz.right(90)
lapiz.forward(250)
lapiz.left(90)
lapiz.down()

for x in range(10):
    linea_recta()
    subir()


screen = turtle_module.Screen()
screen.exitonclick()


