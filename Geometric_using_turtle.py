import turtle
t = turtle.Turtle()
turtle.bgcolor("black")
t.speed(0)
colors = ["yellow", "red", "blue", "green", "purple", "orange"]
for i in range(200):
    t.pencolor(colors[i % 6])
    t.forward(i * 2)
    t.right(61)
turtle.done()