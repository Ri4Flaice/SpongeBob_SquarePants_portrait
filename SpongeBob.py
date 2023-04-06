import turtle

Yellow = 'yellow'
White = 'White'
Skyblue = 'skyblue'
Black = 'black'
Red = 'red'
Pink = 'pink'

t = turtle.Turtle()
t.screen.setup(1300, 850)
t.screen.bgcolor('yellow')
t.speed(20)

def Nose():
    t.pensize(5)
    t.fillcolor(Yellow)
    t.begin_fill()
    
    t.left(70)
    t.forward(60)
    t.circle(20, 90)
    t.circle(100, 20)
    t.circle(20, 40)
    t.circle(20, 40)
    t.circle(20, 40)
    t.right(10)
    t.forward(60)
    
    t.end_fill()

def GlassLeft():
    t.up()
    t.backward(120)
    t.left(90)
    t.right(5)
    t.down()
    
    t.fillcolor(White)
    t.begin_fill()
    
    t.left(90)
    t.circle(100, 360)
    
    t.end_fill()

def PupilLeft():
    t.up()
    t.left(60)
    t.forward(70)
    t.right(10)
    t.down()
    
    t.fillcolor(Skyblue)
    t.begin_fill()
    
    t.circle(30, 360)
    
    t.end_fill()
    
    t.fillcolor(Black)
    t.begin_fill()
    
    t.up()
    t.left(90)
    t.forward(30)
    t.down()
    
    t.left(90)
    t.circle(10, 360)
    
    t.end_fill()
    
    t.up()
    t.forward(5)
    t.left(90)
    t.forward(15)
    t.down()

    t.fillcolor(White)
    t.begin_fill()
    
    t.circle(6, 360)
    
    t.end_fill()

def GlassRight():
    t.up()
    t.right(70)
    t.forward(170)
    t.right(90)
    t.forward(10)
    t.down()
    
    t.fillcolor(White)
    t.begin_fill()
    
    t.circle(100, 360)
    
    t.end_fill()

def PupilRight():
    t.up()
    t.left(90)
    t.forward(50)
    t.right(90)
    t.backward(20)
    t.down()

    t.fillcolor(Skyblue)
    t.begin_fill()
    
    t.circle(30, 360)
    
    t.end_fill()
    
    t.up()
    t.left(90)
    t.forward(15)
    t.right(90)
    t.backward(10)
    t.down()
    
    t.fillcolor(Black)
    t.begin_fill()
    
    t.circle(10, 360)
    
    t.end_fill()
    
    t.up()
    t.left(90)
    t.forward(15)
    t.left(90)
    t.forward(3)
    t.down()
    
    t.fillcolor(White)
    t.begin_fill()
    
    t.circle(6, 360)
    
    t.end_fill()

def CheekRight():
    t.up()
    t.backward(140)
    t.right(90)
    t.forward(200)
    t.left(120)
    t.right(20)
    t.down()
    
    t.pencolor('red')
    t.circle(50, 180)
    
    t.up()
    t.left(120)
    t.forward(40)
    t.down()
    
    t.circle(3, 360)
    
    t.up()
    t.forward(30)
    t.down()
    
    t.circle(3,360)
    
    t.up()
    t.right(80)
    t.forward(30)
    t.down()
    
    t.circle(3, 360)
    
    t.up()
    t.forward(30)
    t.right(135)
    t.forward(540)
    t.right(90)
    t.down()
    
    t.circle(50, 180)
    
    t.up()
    t.left(130)
    t.forward(40)
    t.down()
    
    t.circle(3, 360)
    
    t.up()
    t.right(40)
    t.forward(30)
    t.down()
    
    t.circle(3, 360)
    
    t.up()
    t.right(50)
    t.forward(20)
    t.down()
    
    t.circle(3, 360)
    
def Mouth():
    t.pencolor('black')
    
    t.up()
    t.right(90)
    t.forward(40)
    t.left(90)
    t.down()
    
    t.fillcolor(Red)
    t.begin_fill()
    
    t.circle(370, 100)
    t.left(130)
    t.forward(565)
    
    t.end_fill()

def TeethLeft():
    t.up()
    t.left(180)
    t.forward(270)
    t.right(90)
    t.down()
    
    t.fillcolor(White)
    t.begin_fill()
    
    t.forward(65)
    t.right(90)
    t.forward(30)
    t.right(90)
    t.forward(65)
    
    t.end_fill()
    
def TeethRight():
    t.up()
    t.right(90)
    t.forward(90)
    t.down()
    
    t.fillcolor(White)
    t.begin_fill()
    t.right(90)
    t.forward(65)
    t.right(90)
    t.forward(30)
    t.right(90)
    t.forward(65)
    
    t.end_fill()
    
def Language():
    t.pencolor('black')
    
    t.up()
    t.right(180)
    t.forward(127)
    t.left(90)
    t.forward(30)
    t.left(70)
    t.down()
    
    t.fillcolor(Pink)
    t.begin_fill()
    t.circle(20, 120)
    t.forward(50)
    t.circle(10, 130)
    t.end_fill()
    
    

Nose()
GlassLeft()
PupilLeft()
GlassRight()
PupilRight()
CheekRight()
Mouth()
TeethLeft()
TeethRight()
Language()
turtle.done()