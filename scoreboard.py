from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 10, 'bold')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.setposition(0, 282)
        self.score = 0
        self.score_points(self.score)

    def score_points(self, score):
        self.color("white")
        self.write(arg=f"Score: {score}", align=ALIGNMENT, font=FONT)

    def game_over(self, score):
        self.clear()
        self.hideturtle()
        self.setposition(0, 282)
        self.color("white")
        self.write(arg=f"GAME OVER! Your score is: {score}", align=ALIGNMENT, font=FONT)

