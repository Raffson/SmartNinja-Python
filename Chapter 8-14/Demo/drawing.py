"""
Playing around with a turtle
"""
import turtle


window = turtle.Screen()  # create a Tk root window

window.setup(width=1.0, height=1.0)  # define starting size

canvas = window.getcanvas()  # get the canvas, we'll need it to create a turtle

t = turtle.RawTurtle(canvas)  # create the turtle and attach it to the canvas
t.pencolor("#ff0000")  # Red

# creating a spiral
dist = 1
diff = 0.01
for i in range(360):
    t.forward(dist)
    dist += diff
    diff += 0.001
    t.left(10)

window.exitonclick()  # if we don't do this, window will close when turtle is done...
