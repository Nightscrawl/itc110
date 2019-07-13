# 'Tis the Season
# Assignment 3 Graphics

from graphics import *

def main():
    win = GraphWin("'Tis the Season", 420,400)
    win.setBackground(color_rgb(138,221,255))

# snowman
    man1 = Circle(Point(100,320),80)
    man1.setFill("white")
    man1.setOutline("white")
    man1.draw(win)

    man2 = Circle(Point(100,200),60)
    man2.setFill("white")
    man2.setOutline("white")
    man2.draw(win)

    man3 = Circle(Point(100,110),40)
    man3.setFill("white")
    man3.setOutline("white")
    man3.draw(win)

    hat1 = Rectangle(Point(80,30),Point(120,80))
    hat1.setFill("black")
    hat1.setOutline("black")
    hat1.draw(win)

    hat2 = Rectangle(Point(60,70),Point(140,80))
    hat2.setFill("black")
    hat2.setOutline("black")
    hat2.draw(win)

    eye1 = Circle(Point(85,100),5)
    eye1.setFill("black")
    eye1.setOutline("black")
    eye1.draw(win)

    eye2 = eye1.clone()
    eye2.move(30,0)
    eye2.draw(win)

    nose = Polygon(Point(100,112),Point(100,122),Point(115,117))
    nose.setFill("orange")
    nose.setOutline("orange")
    nose.draw(win)

    mo1 = Circle(Point(80,130),1)
    mo1.setFill("black")
    mo1.setOutline("black")
    mo1.draw(win)

    mo2 = mo1.clone()
    mo2.move(40,0)
    mo2.draw(win)

    mo3 = Circle(Point(89,137),1)
    mo3.setFill("black")
    mo3.setOutline("black")
    mo3.draw(win)

    mo4 = mo3.clone()
    mo4.move(22,0)
    mo4.draw(win)

    mo5 = Circle(Point(100,140),1)
    mo5.setFill("black")
    mo5.setOutline("black")
    mo5.draw(win)

    coal1 = Circle(Point(100,175),5)
    coal1.setFill("black")
    coal1.setOutline("black")
    coal1.draw(win)

    coal2 = coal1.clone()
    coal2.move(0,20)
    coal2.draw(win)

    coal3 = coal2.clone()
    coal3.move(0,20)
    coal3.draw(win)

# tree
    trunk = Rectangle(Point(285,340),Point(315,400))
    trunk.setFill("brown")
    trunk.setOutline("brown")
    trunk.draw(win)

    tree1 = Polygon(Point(200,360),Point(300,270),Point(400,360))
    tree1.setFill("green")
    tree1.setOutline("green")
    tree1.draw(win)

    tree2 = Polygon(Point(220,300),Point(300,220),Point(380,300))
    tree2.setFill("green")
    tree2.setOutline("green")
    tree2.draw(win)

    tree3 = Polygon(Point(240,240),Point(300,180),Point(360,240))
    tree3.setFill("green")
    tree3.setOutline("green")
    tree3.draw(win)

    tree4 = Polygon(Point(260,195),Point(300,150),Point(340,195))
    tree4.setFill("green")
    tree4.setOutline("green")
    tree4.draw(win)

    tree5 = Polygon(Point(280,160),Point(300,125),Point(320,160))
    tree5.setFill("green")
    tree5.setOutline("green")
    tree5.draw(win)

# ornaments
    star = Polygon(Point(300,100),
                   Point(305,115),
                   Point(320,120),
                   Point(305,125),
                   Point(300,140),
                   Point(295,125),
                   Point(280,120),
                   Point(295,115))
    star.setFill("gold")
    star.setOutline("gold")
    star.draw(win)

    o1 = Circle(Point(300,155),4)
    o1.setFill("gold")
    o1.setOutline("orange")
    o1.draw(win)

    o2 = o1.clone()
    o2.move(0,75)
    o2.draw(win)

    o3 = o2.clone()
    o3.move(0,120)
    o3.draw(win)

    o4 = Circle(Point(270,195),4)
    o4.setFill("gold")
    o4.setOutline("orange")
    o4.draw(win)

    o5 = o4.clone()
    o5.move(60,0)
    o5.draw(win)

    o6 = o4.clone()
    o6.move(0,85)
    o6.draw(win)

    o7 = o6.clone()
    o7.move(60,0)
    o7.draw(win)

    o8 = Circle(Point(230,300),4)
    o8.setFill("gold")
    o8.setOutline("orange")
    o8.draw(win)

    o9 = o8.clone()
    o9.move(140,0)
    o9.draw(win)

    o10 = Polygon(Point(300,185),
                  Point(303,188),
                  Point(300,191),
                  Point(297,188))
    o10.setFill("red")
    o10.setOutline("gold")
    o10.draw(win)

    o11 = o10.clone()
    o11.move(0,100)
    o11.draw(win)

    o12 = Polygon(Point(282,160),
                  Point(285,163),
                  Point(282,166),
                  Point(279,163))
    o12.setFill("red")
    o12.setOutline("gold")
    o12.draw(win)

    o13 = o12.clone()
    o13.move(36,0)
    o13.draw(win)

    o14 = Polygon(Point(250,240),
                  Point(253,243),
                  Point(250,246),
                  Point(247,243))
    o14.setFill("red")
    o14.setOutline("gold")
    o14.draw(win)

    o15 = o14.clone()
    o15.move(100,0)
    o15.draw(win)

    o16 = Polygon(Point(210,360),
                  Point(213,363),
                  Point(210,366),
                  Point(207,363))
    o16.setFill("red")
    o16.setOutline("gold")
    o16.draw(win)

    o17 = o16.clone()
    o17.move(180,0)
    o17.draw(win)

    o18 = Polygon(Point(255,335),
                  Point(258,338),
                  Point(255,341),
                  Point(252,338))
    o18.setFill("red")
    o18.setOutline("gold")
    o18.draw(win)

    o19 = o18.clone()
    o19.move(90,0)
    o19.draw(win)

# dialogue
    line = Line(Point(150,130),Point(180,95))
    line.draw(win)

    greet = Text(Point(182,75), "Merry \nChristmas!")
    greet.setSize(12)
    greet.draw(win)

main()
