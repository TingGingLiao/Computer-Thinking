import turtle
shelly = turtle.Turtle()
shelly.shape("turtle")
shelly.position()
shelly.color("green", "red")
shelly.pencolor("black")
shelly.turtlesize(10,10,2)
shelly.resizemode("auto")
shelly.turtlesize(5,5,3)
shelly.forward(100)
shelly.left(90)
shelly.circle(250)
shelly.circle(250, 180, 30)
shelly.end_fill()
shelly.write("Turtle Rock")
import turtle
shelly = turtle.Turtle()
for i in range(4):
    shelly.forward(250)
    shelly.left(90)
    print (i)
import turtle
shelly = turtle.Turtle()
shelly.color("red")
for i in range(4):
    shelly.forward(250)
    shelly.left(90)
    