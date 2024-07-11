from turtle import Screen, Turtle
import random

screen = Screen()
tim = Turtle()
'''
for e in range(5):
    tim.pendown()
    tim.forward(10)
    tim.penup()
    tim.forward(10)
'''

color = ["deep pink", "dark red", "medium slate blue", "orange", "yellow", "salmon", "lawn green", "spring green",
         "beige", "cyan", "aquamarine", "midnight blue", "navy"]

def draw_shape(num_sides):
    for x in range(num_sides, 10):
        tim.color(random.choice(color))
        for _ in range(num_sides):
            angle = 360 / num_sides
            tim.forward(100)
            tim.right(angle)
        num_sides += 1

draw_shape(3)
screen.exitonclick()