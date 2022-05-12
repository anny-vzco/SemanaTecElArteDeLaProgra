"""
Juego: Cannon
Programador 1: Annya Paulina Verduzco Meza / A01650668
Programador 2: Diego Isunza Garciacano / A01652067
Fecha: 10 / mayo / 2022
"""

from random import randrange
from turtle import *

from freegames import vector

ball = vector(-200, -200)
speed = vector(0, 0)
targets = []


def tap(x, y):
    """Respond to screen tap."""
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        #Aqui se modifica para que la velocidad del projectil sea de acuerdo a tus preferencias en el eje X y Y
        speed.x = (x + 300) / 25
        speed.y = (y + 300) / 25


def inside(xy):
    """Return True if xy within screen."""
    return -200 < xy.x < 200 and -200 < xy.y < 200


def draw():
    """Draw ball and targets."""
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()


def move():
    """Move ball and targets."""
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    for target in targets:
        target.x -= 0.5

    if inside(ball):
        speed.y -= 0.35
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    draw()

    for target in targets:
        if not inside(target):
            target.x = 500
            #Modificar para que el juego no termine, que regrese mas targets 

    # Modificar el segundo parametro de esta funcion, permite que se recarge mas rapido la funcion move(), 
    # haciendo que los balones vayan mas rapido
    ontimer(move, 15)


setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()
