from turtle import Turtle,Screen
from Player import Player
from Car_Manager import Car_Manager
import time
s = Screen()
s.setup(width=600,height=600)
s.bgcolor("#FFF")
s.title("Turtle Racer")
s.listen()
s.tracer(0)

turtle = Player()

carArray = []

game_is_on = True
i = 0
        
carArray = [Car_Manager() for _ in range(0,10)]

i = 0

def update(): 
    time.sleep(0.01)
    s.onkeypress(turtle.Move,"Up")
    s.update()
    i = 0
    while i<10:
        carArray[i].Move()
        i+=1
    s.ontimer(update,10)
    
    if(turtle.ycor()>290):
        exit()
        # game_is_on = False

update()

s.exitonclick()