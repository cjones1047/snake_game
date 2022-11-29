from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.speed("fastest")
        self.hideturtle()
        self.sety(270)
        self.score = 0
        self.show_scoreboard()

    def increase(self):
        self.score += 1
        self.show_scoreboard()

    def show_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Courier", 20, "normal"))
