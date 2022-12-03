from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
TOP = 270


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.speed("fastest")
        self.hideturtle()
        self.sety(TOP)
        self.score = 0
        with open("data.txt", mode="r") as file:
            str_num = file.read()
            if not str_num:
                self.high_score = 0
            else:
                int_num = int(str_num)
                self.high_score = int_num
        self.update_scoreboard()

    def increase(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} | High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    # def game_over(self):
    #     self.sety(0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()
