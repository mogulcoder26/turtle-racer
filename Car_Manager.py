from turtle import Turtle,delay
from random import randint
colorArray = ["Red", "Purple", "Blue", "Turquoise", "Green",
    "Yellow", "Orange", "Crimson", "Salmon", "MediumAquamarine",
    "MediumSpringGreen", "SteelBlue", "CornflowerBlue", "MediumOrchid",
    "LightCoral", "Gold", "OrangeRed", "FireBrick", "IndianRed",
    "MediumPurple"]

class Car_Manager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color(colorArray[randint(0,19)])
        self.penup()
        self.shapesize(stretch_len=2.5)
        self.goto(randint(50,290),randint(-250,250))
        self.speed(0)

        delay(10)
    
    def Move(self):
        self.goto(self.xcor() - randint(1,2),self.ycor())
