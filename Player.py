from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("#000")
        self.penup()
        self.left(90)
        self.goto(0,-280)

    def Move(self):
        self.goto(self.xcor(),self.ycor() + 4)

    def Reposition(self):
        self.goto(0,-280)