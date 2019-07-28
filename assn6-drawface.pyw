# Assignment 6 - drawFace
# A program that draws several faces of varying sizes
# Kira Abell
# 7/28/19


from graphics import *

def drawFace(center, size, win):
    circ = Circle(center, size)
    circ.setFill("cyan")
    circ.draw(win)

    # mouth
    o1 = center.getX()
    o2 = center.getY()
    mo = Oval(Point(o1-(size/2),o2-(size/2.5)),
              Point(o1+(size/2),o2+(size/2.5)))
    mo.setFill("black")
    mo.draw(win)

    # overlay oval to create "smile" from 'mo'
    hide = mo.clone()
    hide.move(0, -3)
    hide.setFill("cyan")
    hide.setOutline("cyan")
    hide.draw(win)

    # eyes
    eye1 = Circle(center, size/12)
    eye1.move(-size/3, -size/3)
    eye1.setFill("black")
    eye1.draw(win)

    eye2 = Circle(center, size/12)
    eye2.move(size/3, -size/3)
    eye2.setFill("black")
    eye2.draw(win)

    # mouth as line
    # m1 = center.getX()
    # m2 = center.getY()
    # mo = Line(Point(m1-(size/3),m2+(size/3)),
    #           Point(m1+(size/3),m2+(size/3)))
    # mo.draw(win)
    
    
def main():
    win = GraphWin("Time to draw!", 400,400)
    message = Text(Point(200,20), "Click anywhere to draw.")
    message.draw(win)

    # creates a loop with a list in three sizes
    # loop iterates the drawFace function for each 'size' in the list
    # each face is created with user input mouse click as the center point
    # the list can be altered for different sizes, more faces, a range of faces

    # this option starts at size 10, ends at 100, iterates every 5 growths
    # for size in range(10,100,5):  

    # a simple list of three sizes
    for size in [20,40,60]:
        center = win.getMouse()
        drawFace(center, size, win)

    message.setText("Click to close.")
    win.getMouse()
    win.close()

main()
