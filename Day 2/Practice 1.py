import turtle

my_pen=turtle.Pen()
my_pen.shapesize(0.1)
my_pen.color("yellow")
my_pen.width(0.1)
my_pen.speed(5)

# Pattern 1
for i in range(5):
    my_pen.forward(25)
    my_pen.up()
    my_pen.forward(25)
    my_pen.down()

# Pattern 2
my_pen.up()
my_pen.goto(150,150)
my_pen.down()
my_pen.color("red")
my_pen.setheading(180)
for i in range(3):
    my_pen.left(90)
    my_pen.forward(100)
my_pen.color("green")
my_pen.goto(150,150)
my_pen.right(90)
for i in range(3):
    my_pen.forward(100)
    my_pen.left(120)

# Pattern 3
my_pen.up()
my_pen.goto (-150,-150)
my_pen.down()
for i in range(10):
    my_pen.color("purple")
    my_pen.setheading(0)
    my_pen.forward(25)
    my_pen.color("red")
    my_pen.left(90)
    my_pen.forward(25)
    my_pen.color("green")
    my_pen.right(90)
    my_pen.forward(25)
    my_pen.color("blue")
    my_pen.right(90)
    my_pen.forward(25)

turtle.mainloop()