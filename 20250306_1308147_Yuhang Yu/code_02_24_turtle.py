import turtle
turtle.setup(640,480)
# drawing a rectangle
turtle.forward(100)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(50)
turtle.reset()

# box with pause
turtle.forward(20)
turtle.penup()
turtle.forward(10)
turtle.pendown()
turtle.forward(20)
turtle.penup()
turtle.forward(10)
turtle.pendown()
turtle.forward(20)
turtle.right(90)
turtle.forward(20)
turtle.penup()
turtle.forward(10)
turtle.pendown()
turtle.forward(20)
turtle.penup()
turtle.forward(10)
turtle.pendown()
turtle.forward(20)
turtle.penup()
turtle.forward(10)
turtle.pendown()
turtle.reset()

#drawing a circle
turtle.circle(50)
turtle.forward(10)
turtle.pencolor("red")
turtle.circle(60)
turtle.forward(10)
turtle.pencolor("blue")
turtle.width(5)
turtle.circle(70)
turtle.forward(10)
turtle.pencolor("green")
turtle.width(7)
turtle.fillcolor("purple")
turtle.begin_fill()
turtle.circle(80)
turtle.end_fill()
turtle.reset()

#drawing circles with goto function
turtle.circle(30)
turtle.penup()
turtle.goto(130,130)
turtle.pendown()
turtle.circle(20)
turtle.reset()

#plympic flag. blue yellow black green red
turtle.width(5)
turtle.penup()
turtle.goto(-100,0)
turtle.pencolor("blue")
turtle.pendown()
turtle.circle(40)
turtle.penup()
turtle.goto(0,0)
turtle.pencolor("black")
turtle.pendown()
turtle.circle(40)
turtle.penup()
turtle.goto(100,0)
turtle.pencolor("red")
turtle.pendown()
turtle.circle(40)
turtle.penup()
turtle.goto(-50,-40)
turtle.pencolor("yellow")
turtle.pendown()
turtle.circle(40)
turtle.penup()
turtle.goto(50,-40)
turtle.pencolor("green")
turtle.pendown()
turtle.circle(40)

turtle.done()