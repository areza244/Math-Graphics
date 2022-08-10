# Amirreza Pazira
# 25 Nov 2020
# Assignment - 4 - Analytical Geometry

# Importing our packages for turtle and math equations
import turtle
import math
# Defining our constants
WIDTH = 800
HEIGHT = 600
MIDDLEX = WIDTH/2
MIDDLEY = HEIGHT/2
# Defining our variables
alpha1 = False
alpha2 = False
# Set our screen size 
pen = turtle.Turtle()
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT, 0, 0)
screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)
pen.hideturtle()
# Getting the coordinates from the user
xc = int(input('Enter the middle x coordinate of the circle: '))
yc = int(input('Enter the middle y coordinate the circle: '))
r = float(input('Enter the radius of the circle: '))
x1 = int(input('Enter the start x coordinate of the line: '))
y1 = int(input('Enter the start y coordinate of the line: '))
x2 = int(input('Enter the end x coordinate of the line: '))
y2 = int(input('Enter the end y coordinate of the line: '))
# Drawing the axis lines 
pen.color('black')
pen.speed(0)
pen.up()
pen.setpos(0, 300)
pen.down()
pen.setpos(800, 300)
pen.up()
pen.setpos(400, 0)
pen.down()
pen.setpos(400, 600)
pen.up()
# Drawing the circle
pen.color('red')
pen.setpos(xc, yc-r)
pen.down()
pen.circle(r)
pen.up()
# Drawing the line
pen.color('blue')
pen.setpos(x1, y1)
pen.down()
pen.setpos(x2, y2)
pen.up()
# Calculating the 3 intermediate calculations
a = (x2 - x1)**2 + (y2 - y1)**2
b = 2*((x1 - xc)*(x2 - x1) + (y1 - yc)*(y2 - y1))
c = (x1 - xc)**2 + (y1 - yc)**2 - (r**2)
B2 = (b**2) - (4*a*c)
# By looking at the value under the root we can find the number of intersections
# Then we calculate the Alpha and the condition of intersections only between two endpoints of our line
if B2 > 0:
    alphaFirst = (-1 * b + math.sqrt(B2)) / (2 * a)
    int1x = (1 - alphaFirst) * x1 + alphaFirst * x2
    int1y = (1 - alphaFirst) * y1 + alphaFirst * y2
    alpha1 = alphaFirst >= 0 and alphaFirst <= 1
    alphaSecond = (-1 * b - math.sqrt(B2)) / (2 * a)
    int2x = (1 - alphaSecond) * x1 + alphaSecond * x2
    int2y = (1 - alphaSecond) * y1 + alphaSecond * y2
    alpha2 = alphaSecond >= 0 and alphaSecond <= 1
if B2 == 0:
    alphaFirst = (-1 * b + math.sqrt(B2)) / (2 * a)
    alpha1 = (-1 * b - math.sqrt(B2)) / (2 * a)
    int1x = (1 - alphaFirst) * x1 + alphaFirst * x2
    int1y = (1 - alphaFirst) * y1 + alphaFirst * y2
    alpha1 = alphaFirst >= 0 and alphaFirst <= 1
pen.color('green')
# Drawing a circle around our intersections 
if alpha1:
    pen.setpos(int1x, int1y-5)
    pen.down()
    pen.circle(5)
    pen.up()
if alpha2:
    pen.setpos(int2x, int2y-5)
    pen.down()
    pen.circle(5)
pen.up()
# Writing the amount of intersections in the middle of our screen
if alpha1 and alpha2:
    pen.setpos(MIDDLEX - 68, MIDDLEY)
    pen.write("Two intersect!", font=("Arial", 16, "normal"))
elif alpha1 or alpha2:
    pen.setpos(MIDDLEX - 68, MIDDLEY)
    pen.write("One intersect!", font=("Arial", 16, "normal"))
else:
    pen.setpos(MIDDLEX - 68, MIDDLEY)
    pen.write("No intersect!", font=("Arial", 16, "normal"))
# Closing the screen on click
screen.exitonclick()