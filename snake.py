from turtle import Turtle
from food import Food

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]

class Snake:

    def __init__(self):
       self.segment = []
       self.createte_snake()
       self.head = self.segment[0]

    def createte_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self , position):
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            # new_segment.speed("slowest")
            new_segment.goto(position)
            self.segment.append(new_segment)
    def increase_snake(self):
        self.add_segment(self.segment[-1].position())




    def move(self):
        for seg in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[seg - 1].xcor()
            new_y = self.segment[seg - 1].ycor()
            self.segment[seg].goto(new_x, new_y)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
             self.head.setheading(270)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != 0:
             self.head.setheading(180)


