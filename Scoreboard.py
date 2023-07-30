from turtle import Turtle
ALIGNMENT = 'center'
FONT = 'Courier'
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        # self.clear()
        self.penup()
        self.color("#000")
        self.goto(0,0)

        self.pendown()
        self.write("Home",align=ALIGNMENT,font=(FONT,24,'normal'))
        # self.hideturtle()
       