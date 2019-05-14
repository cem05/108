#Write a graphics program to display (draw) a simple building (but NOT a house)
#using at least 4 shapes and 3 different colors.
from graphics import *

win =GraphWin('Simple Building', 500 ,500)
win.setBackground('LightBlue')

#attempt at a castle
## think xy axis(x,y  x,y)

#main structure
frame = Rectangle(Point(350, 225), Point (100, 425))
frame.draw(win)
frame.setWidth(3)
frame.setFill('DimGray')
frame.setOutline('black')

#set up the turrets
turret1 = Rectangle(Point(40, 125), Point (140, 225))
turret1.draw(win)
turret1.setWidth(3)
turret1.setFill('yellow')
turret1.setOutline('black')

turret2 = Rectangle(Point(280, 225), Point (380, 125))
turret2.draw(win)
turret2.setWidth(3)
turret2.setFill('green')
turret2.setOutline('black')

#create a door
door = Rectangle(Point(200, 325), Point (255, 420))
door.draw(win)
door.setWidth(3)
door.setFill('tan')
door.setOutline('black')

#doorknob
knob = Circle(Point(255, 375), 5)
knob.draw(win)
knob.setFill('red')

# set up flagpole
flagP = Line(Point(380, 150), Point(380, 35))
flagP.draw(win)
flagP.setWidth(3)
flagP.setOutline('blue')

#raise your flag
direc = Text(Point(170, 30), 'Click 4X in a flag shape near flag pole\n to raise your castles flag ')
direc.setTextColor('red')
direc.setStyle('italic')
direc.setSize(10)
direc.draw(win)

p1 = win.getMouse()
p1.draw(win)
p2 = win.getMouse()
p2.draw(win)
p3 = win.getMouse()
p3.draw(win)
p4 = win.getMouse()
p4.draw(win)

flag = Polygon(p1,p2,p3,p4)
flag.setFill('white')
flag.setOutline('black')
flag.setWidth(4)
flag.draw(win)
direc.setText('Click HERE to close') 
win.getMouse()
win.close()
