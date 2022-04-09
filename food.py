import random
from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.makeing_food()

    def makeing_food(self):
        self.shape("circle")
        self.color("blue")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.penup()
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.random_x = random.randint(-280, 280)
        self.random_y = random.randint(-280, 280)
        self.goto(x=self.random_x, y=self.random_y)