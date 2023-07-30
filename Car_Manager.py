from turtle import Turtle,delay
from random import randint
colorArray = ['red','blue','magenta','grey','black','brown','yellow']

class Car_Manager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color(colorArray[randint(0,6)])
        self.penup()
        self.shapesize(stretch_len=2.5)
        self.goto(randint(20,290),randint(-250,250))
        self.speed(0)
        delay(10)
    
    def Move(self):
        self.goto(self.xcor() - randint(1,2),self.ycor())

    def Reposition(self):
        self.goto(randint(-250,290),self.ycor())