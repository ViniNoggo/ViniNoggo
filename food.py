from turtle import Turtle
from random import choice


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.color("blue")
        self.shape("circle")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.penup()

    def refresh_position(self):
        x_axis = choice(range(-250, 251))
        y_axis = choice(range(-250, 251))
        self.setposition(x_axis, y_axis)
