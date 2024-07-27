import turtle,random
def make_cloumn(height):
    p.setheading(90)
    for i in range(height):
        p.stamp()
        p.forward(15)
p=turtle.Pen()
p.speed(0)
p.color("green")
p.shape("square")
p.shapesize(0.5)
p.up()
x=-150
y=-100
col_height=0
p.goto(x,y)
for i in range(10):
    r=random.random()
    g=random.random()
    b=random.random()
    p.color(r,g,b)
    col_height=col_height+1
    make_cloumn(col_height)
    x=x+15
    p.goto(x,y)
for i in range(9):
    r=random.random()
    g=random.random()
    b=random.random()
    p.color(r,g,b)
    col_height=col_height-1
    make_cloumn(col_height)
    x=x+15
    p.goto(x,y)
turtle.mainloop()