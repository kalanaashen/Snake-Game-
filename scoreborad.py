from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.goto(0,250)
        self.update_scoreborad()

    def defeat_logo(self):
        self.goto(0,0)
        self.write("Game Over",align="center" ,font=("arial", 10, "normal"))

    def update_scoreborad(self):
        self.write(f"SCORE:{self.score}", False, "center", font=("arial", 20, "bold"))
    def marks(self):
        self.score+=1
        self.clear()
        self.write(f"SCORE:{self.score}",False,"center",font=("arial",20,"bold"))