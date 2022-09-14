import turtle
turtle.getscreen().bgcolor("red")
turtle.speed(100)
turtle.bgcolor("black")

for i in range(240):
    turtle.color("cyan")
    turtle.circle(i)
    turtle.left(5)
turtle.done()