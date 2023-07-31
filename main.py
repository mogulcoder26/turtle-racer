from turtle import Turtle, Screen, delay
from Player import Player
from Car_Manager import Car_Manager
from LineDrawers import LineDrawer
from Scoreboard import Scoreboard
import time

s = Screen()
s.setup(width=600, height=600)
s.bgcolor("#fff")
s.title("Turtle Racer")
s.listen()
s.tracer(0)
LD = LineDrawer()
turtle = Player()
turtle.color("black")
s.onkeypress(turtle.Move, "Up")
carArray = [Car_Manager()]
score = Scoreboard()

game_is_on = True
i = 0
while game_is_on:
    time.sleep(0.1)

    i += 1
    s.update()
    if i >= 10:
        i = 0
        carArray.append(Car_Manager())

    for car in carArray:
        car.Move()
        if(car.distance(turtle) <25):
            score.Failure()
            game_is_on = False
    
    if turtle.ycor() > 250:
        turtle.Reposition()
        score.Success()
    


s.exitonclick()
