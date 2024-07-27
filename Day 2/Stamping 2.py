import turtle,random
p=turtle.Pen()
p.speed(0)
p.color("green")
p.shapesize(0.1)
p.up()
for i in range(1000):
    x=random.randint(-200,200)
    y=random.randint(-200,200)
    p.goto(x,y)
    if x<=0:
        p.color("green")
    if x>=0:
        p.color("red")
    p.stamp()
turtle.mainloop()