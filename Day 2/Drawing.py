import turtle

my_pen=turtle.Pen()
my_pen.shapesize(0.1)
my_pen.color("green")
my_pen.width(5)
my_pen.speed(5)

for i in range(4):
    my_pen.forward(100)
    my_pen.left(90)
print("Done!")

my_pen.up()
my_pen.goto(150,150)
my_pen.down()

# Problem 1
my_pen.color("red")
for i in range(3):
    my_pen.forward(100)
    my_pen.left(120)

# Problem 2
my_pen.up()
my_pen.goto(-150,-150)
my_pen.down()
my_pen.color("purple")
for i in range(6):
    my_pen.forward(100)
    my_pen.left(60)

# Problem 3
my_pen.up()
my_pen.goto(-150,150)
my_pen.down()
my_pen.color("cyan")
for i in range(5):
    my_pen.forward(100)
    my_pen.left(180-108)

# Problem 4
my_pen.up()
my_pen.goto(150,-150)
my_pen.down()
my_pen.color("blue")
for i in range(5):
    my_pen.left(180-36)
    my_pen.forward(100)
turtle.mainloop()