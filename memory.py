"""
Juego: Memory
Programador 1: Annya Paulina Verduzco Meza / A01650668
Programador 2: Diego Isunza Garciacano / A01652067
Fecha: 10 / mayo / 2022
"""

from random import *
from tkinter import CENTER
from turtle import * 
from freegames import path


car = path('car.gif')
tiles = list(range(32)) * 2
state = {'mark': None}
hide = [True] * 64
Clicks = 0
completado = 0
colores = ['#FFEBEE', '#F8BBD0', '#E1BEE7',  '#D1C4E9', '#C5CAE9', 
	   '#BBDEFB', '#B3E5FC', '#B2EBF2', '#B2DFDB', '#C8E6C9',
	   '#DCEDC8', '#EA6FA6', '#FFF9C4', '#FFECB3', '#FFE0B2',
	   '#FFCCBC', '#D7CCC8', '#B0FF33', '#D81B60', '#8E24AA',
	   '#33FFBD', '#3949AB', '#1E88E5', '#039BE5', '#00ACC1',
	   '#33F1FF', '#EA6FD6', '#7CB342', '#C5DA73', '#7DEA6F',
	   '#6F83EA', '#EA6F80', '#F4511E']
       #lista de colores 




def square(x, y, txt):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', txt)
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    #Aqui se definen las variables para que sean globales
    global Clicks
    global completado

    Clicks += 1 #Se suma un click 
    spot = index(x, y)
    mark = state['mark']
    

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
        completado+=1 #Aqui se suma un par de cuadros


def draw():
    """Draw image and tiles."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y, 'white')

    mark = state['mark']

#centrar el numero en el recuadro 
    if mark is not None and hide[mark]:
        x, y = xy(mark)
        square(x, y, colores[tiles[mark]])#añadir colores a las tiles
        up()
        goto(x + 27, y)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'), align='center')

    penup()
    goto(-200,200)
    write(Clicks, font=20)
    if completado == 32:
        goto(-100,200)
        write("El juego ha terminado", font=20) #Aqui se imprime que el juego ha terminado
    
    update()
    ontimer(draw, 100)


shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
