from turtle import Turtle, Screen, delay
from Player import Player
from Car_Manager import Car_Manager
from LineDrawers import LineDrawer
import time

s = Screen()
s.setup(width=600, height=600)
s.bgcolor("#FFF")
s.title("Turtle Racer")
s.listen()
s.tracer(0)
LD = LineDrawer()
turtle = Player()
s.onkeypress(turtle.Move, "Up")
carArray = [Car_Manager()]


game_is_on = True
i = 0
while game_is_on:
    time.sleep(0.1)

    i+=1
    s.update()
    if(i>=6):
        i=0
        carArray.append(Car_Manager())

    for car in carArray:
        car.Move()
    

    
s.exitonclick()
