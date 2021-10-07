from turtle import Turtle, Screen
from colors import colors
from random import randint


unit_circle = 360
papa_emeritus_2 = Turtle()
papa_emeritus_2.shape("turtle")
turtle_screen = Screen()
distance = 100
i = 3

while i < 11:
    color_selection = randint(0, len(colors) - 1)
    papa_emeritus_2.color(colors[color_selection])
    j = 1
    while j <= i:
        angle_right = unit_circle / i
        papa_emeritus_2.forward(distance)
        papa_emeritus_2.right(angle_right)
        j += 1
    i += 1