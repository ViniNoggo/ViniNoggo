import turtle as t
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self):
        self.snake_length = []
        self.create_snake((0, 0))
        self.head = self.snake_length[0]
        self.tail = self.snake_length[-1]

    def create_snake(self, position):
        bit = t.Turtle(shape="square")
        bit.color("white")
        bit.penup()
        bit.goto(position)
        self.snake_length.append(bit)

    def extend_snake(self):
        self.create_snake(self.tail.position())

    def move_snake(self):
        for bits in range(len(self.snake_length) - 1, 0, -1):
            bit_of_snake = self.snake_length[bits]
            bit_of_snake_snake_before = self.snake_length[bits - 1]
            bit_of_snake.setposition(bit_of_snake_snake_before.pos())
        self.head.forward(20)

    def go_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def go_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def go_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def go_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
