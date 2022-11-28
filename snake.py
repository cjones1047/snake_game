from turtle import Turtle
MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.snake = []
        self.create_snake()

    def create_snake(self):
        for i in range(3):
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(0 - (i * MOVE_DISTANCE), 0)
            self.snake.append(new_segment)

    def move(self):
        for segment in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[segment - 1].xcor()
            new_y = self.snake[segment - 1].ycor()
            self.snake[segment].goto(new_x, new_y)

        self.snake[0].forward(MOVE_DISTANCE)

    def up(self):
        self.snake[0].setheading(90)

    def down(self):
        self.snake[0].setheading(270)

    def left(self):
        self.snake[0].setheading(180)

    def right(self):
        self.snake[0].setheading(0)
