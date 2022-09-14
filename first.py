

import turtle
turtle.pencolor("red")#color of the pen whic is making the figure
turtle.begin_fill()# it will start filing the inside
turtle.fillcolor("cyan")# the inside color          
turtle.pensize(5)
turtle.forward(100)                 #'''we can also write the this as turtle.color("red","cyan")
                                   #so the first color will be the pen and the secons color will be
                                   # #theinside of the color'''
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.end_fill()# the end where the color must be filled inside

turtle.penup()# takes te pointer up at the desired point
turtle.forward(100)
turtle.pendown()#takes the pointer down at that desired point
turtle.pencolor("red")
turtle.begin_fill()
turtle.fillcolor("cyan")          
turtle.pensize(5)
turtle.forward(100)                 
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.end_fill()


turtle.penup()#drawing a circle useing the circle function

turtle.forward(150)
turtle.pendown()
turtle.circle(-50,180)#(radius , extent(hhow muxh we want eg semi,step()))
turtle.pencolor("green")

turtle.done()