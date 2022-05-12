"""
Juego: Snake
Programador 1: Annya Paulina Verduzco Meza / A01650668

Programador 2: Diego Isunza Garciacano / A01652067

Fecha: 10 / mayo / 2022
"""

from turtle import *
from random import randrange
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

#Creacion de lista de paleta de colores disponibles
colors=['green','blue','yellow','orange','purple']
#Numero aleatorio entre el 0 y el 4
random_number = randrange(0,5)
#Creacion del color del snake
random_color_snake=colors[random_number]
#Se quita el color del sanke en la lista para que no afecte a la comida
colors.remove(colors[random_number])
#Creacion del color de la comida
random_color_food = colors[random_number]


def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    

    for body in snake:
        square(body.x, body.y, 9, random_color_snake)

    square(food.x, food.y, 9, random_color_food)
    update()
    ontimer(move, 100)


#La comida podrá moverse al azar un paso a la vez y no deberá de salirse de la ventana,modificación hecha por Annya Verduzco
def movingFood():
    option = randrange(0,5)
    if(option == 0):
        if (food.x == -200): #se establecen los parametros en x en los que la cómida se moverá dentro del tablero 
            food.x += 10
        elif (food.x == 200):
            food.x -= 10
        else:
            food.x += randrange(-10, 10, 20)
    else:
        if(food.y == -200):#se establecen los parametros en y en los que la cómida se moverá dentro del tablero
            food.y += 10
        elif(food.y == 190):
            food.y -= 10
        else:
            food.y += randrange(-10, 10, 20)

    ontimer(movingFood, 700) #Velocidad de movimeinto de la comida 

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
movingFood()
done()
