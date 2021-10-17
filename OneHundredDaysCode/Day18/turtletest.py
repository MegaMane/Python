from turtle import Turtle,Screen
import random

colors = ["aquamarine", "magenta", "azure", "violet", "tan", "tomato",
          "violet", "plum", "pink", "orchid", "orange", "MintCream",
          "LimeGreen","HotPink","grey","ForestGreen", "CornflowerBlue",
          "chocolate", "black"]

timmy = Turtle()
timmy.shape("turtle")



# for t in range(4):
#     timmy.forward(100)
#     timmy.right(90)

shapes = {"Triangle": 3, "Square": 4, "Pentagon":5,
	      "Hexagon":6, "Heptagon":7, "Octagon": 8, 
          "Nonagon": 9, "Decagon": 10}

dict_items = sorted(shapes.items(),reverse=True)

for shape, sides in dict_items:
    angle = 360 / sides
    timmy.color(random.choice(colors))
    for s in range(sides):
        timmy.forward(100)
        timmy.right(angle)

#Dashed Line
timmy.penup()
timmy.left(90)
timmy.forward(20)
timmy.right(90)
timmy.pendown()

for t in range(15):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()

my_screen = Screen()
my_screen.exitonclick()
