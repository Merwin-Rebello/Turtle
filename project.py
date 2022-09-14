import turtle
turtle.bgcolor("black")
turtle.pencolor("light green")
turtle.speed(300)
for i in range(150):
  turtle.forward(20)
  turtle.circle(i)
  turtle.right(15)
# turtle.pencolor("cyan")

#def star():
for item in range(150):
  turtle.pencolor("cyan")
  turtle.forward(item)
  turtle.left(227)
  turtle.forward(item)
  turtle.left(15)
  turtle.penup()
  turtle.forward(20)
  #turtle.right(10)
  turtle.pendown()
for item in range(150):
      turtle.pencolor("cyan")
      turtle.forward(item)
      turtle.left(227)
      turtle.forward(item)
      turtle.left(15)

#star()



turtle.done()