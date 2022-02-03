import turtle
 
pen = turtle.Turtle()
 
def eye(col, rad):
    pen.down()
    pen.fillcolor(col)
    pen.begin_fill()
    pen.circle(rad)
    pen.end_fill()
    pen.up()
 
 
pen.fillcolor('yellow')
pen.begin_fill()
pen.circle(100)
pen.end_fill()
pen.up()
 
pen.goto(-40, 120)
eye('green', 15)
pen.goto(-37, 125)
eye('red', 5)
pen.goto(40, 120)
eye('green', 15)
pen.goto(40, 125)
eye('red', 5)
 

 
pen.goto(-40, 85)
pen.down()
pen.right(90)
pen.circle(40, 180)
pen.right(90)
pen.forward(10)
pen.left(20)
pen.forward(10)
pen.up()
 

