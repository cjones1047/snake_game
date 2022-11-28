from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

all_turtles = []
starting_position = (0, 0)

for i in range(3):
    new_turtle = Turtle(shape="square")
    new_turtle.color("white")
    new_turtle.goto(starting_position[0] - (i * 20), starting_position[1])
    all_turtles.append(new_turtle)

screen.exitonclick()
