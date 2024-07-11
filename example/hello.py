from turtle import Screen, Turtle

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake")
blue_turtle = Turtle()
blue_turtle.shape("square")
blue_turtle.color("blue")

screen.exitonclick()