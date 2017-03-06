import turtle

def drawsporadic():
    window = turtle.Screen()
    window.bgcolor("yellow")
    
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.speed(10)
    brad.color("purple")
    
    for x in range(36):
        for i in range(2):
            brad.forward(50)
            brad.right(45)
            brad.forward(50)
            brad.right(135)
        brad.right(10)

    for x in range(36):
        for i in range(2):
            brad.forward(80)
            brad.right(45)
            brad.forward(80)
            brad.right(135)
        brad.right(10)

    brad.speed(5)
    brad.color("green")
    brad.right(90)
    brad.forward(250)

    window.exitonclick()
    
drawsporadic()
