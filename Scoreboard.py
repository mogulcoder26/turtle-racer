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
        try:
            f = open("highscore.txt","r")
            self.highscore = int(f.read())
            f.close()
        except:
            f = open("highscore.txt","w")
            self.highscore = 0
            f.write("0")
            f.close()
        self.write(f"Score : {self.score} , HighScore : {self.highscore}",align=ALIGNMENT,font=(FONT,24,'normal'))
        self.hideturtle()
       
    def Success(self):
        self.clear()
        self.score+=1
        f = open("highscore.txt","r")
        highscore = int(f.read())
        if(highscore <= self.score):
            self.highscore = self.score
            x = open("highscore.txt",'w')
            x.write(f"{self.highscore}")
        f.close()
        self.write(f"Score : {self.score} HighScore:{self.highscore}",align=ALIGNMENT,font=(FONT,24,'normal'))

    def Failure(self):
        self.clear()
        self.write(f"Oh No :( Score =  {self.score}",align=ALIGNMENT,font=(FONT,24,'normal'))
        self.penup()
        self.goto(0,0)
        self.pendown()
        self.write(f"GAME OVER",align=ALIGNMENT,font=(FONT,24,'normal'))
        self.score =0
