from turtle import Turtle
class LineDrawer(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(300,-250)
        self.pendown()
        self.goto(-300,-250)
        self.penup()
        self.goto(300,250)
        self.pendown()
        self.goto(-300,250)