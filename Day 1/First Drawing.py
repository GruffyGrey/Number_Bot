import turtle

my_pen=turtle.Pen()
my_pen.shapesize(0.1)
my_pen.color("green")
my_pen.width(1)
my_pen.speed(0)

# An image of a circle with triangles gets made with only straight lines
for i in range(10000):
    my_pen.forward(100)
    my_pen.left(132)


turtle.mainloop()