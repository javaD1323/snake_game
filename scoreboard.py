import time
from turtle import Turtle

FONT = ("Verdana", 15, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        # self.speed = [0.6, 0.4, 0.2, 0.1, 0.09, 0.007, 0.005]
        self.hideturtle()
        self.score = 0
        self.penup()
        self.goto(x=0, y=270)
        self.color("deep pink")
        self.write(f"Score :  {self.score}", align="center", font=FONT)

    def update(self):
        self.clear()
        self.score += 1
        self.write(f"Score :  {self.score}", align="center", font=FONT)

    def gameover(self):
        self.goto(x=0, y=0)
        self.write("GAME OVER" , align="center" , font=FONT)

