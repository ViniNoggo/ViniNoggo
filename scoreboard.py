from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 15, 'normal')


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.setposition(0, 262)
        self.show_score()
        self.hideturtle()

    def show_score(self):
        self.write(arg=f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.setposition(0, 0)
        self.write(arg="Game Over.", move=False, align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1
        self.clear()
        self.show_score()
