from turtle import Turtle
ALIGNMENT = 'center'
FONT = 'Courier'
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        # self.clear()
        self.score  =0 
        self.penup()
        self.color("#000")
        self.goto(0,260)

        self.pendown()
        self.write(f"Score : {self.score}",align=ALIGNMENT,font=(FONT,24,'normal'))
        self.hideturtle()
       
    def Success(self):
        self.clear()
        self.score+=1
        self.write(f"Score : {self.score}",align=ALIGNMENT,font=(FONT,24,'normal'))

    def Failure(self):
        self.clear()
        self.write(f"Oh No :( Score =  {self.score}",align=ALIGNMENT,font=(FONT,24,'normal'))
        self.score =0
