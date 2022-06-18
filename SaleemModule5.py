
# Allows the use of the Point() function to define x and y coordinates.
from graphics import*

class Point:
    """Point class for storing mathematical points"""
    def __init__(self, x, y):
        """Initialize rectangle at posn, with width w, height h"""
        self.x = x
        self.y = y

class Rectangle:
    """ A class to manufacture rectangle objects """
    def __init__(self, posn, w, h):
        """ Initialize rectangle at posn, with width w, height h """
        self.corner = posn
        self.width = w
        self.height = h

    def __str__(self):
        return "({0}, {1}, {2})".format(self.corner, self.width, self.height)

#To create_rectangle()
#create a new instance of Rectangle
def create_rectangle(x, y, width, height):
    posn = Point(x,y)
    rect = Rectangle(posn, width, height)
    return rect

# To str_rectangle()
# Convert given Rectangle instance into string of form (x, y, width, height)
def str_rectangle(rect):
    return (rect.corner.x, rect.corner.y, rect.width, rect.height)

# To shift_rectangle()
# Change the x and y coordinates of the given Rectangle instance
def shift_rectangle(rect, dx, dy):
    rect.corner.x += dx
    rect.corner.y += dy

# To offset_rectangle
# Create a new Rectangle instance which is offset from the given instance
# in x and y coordinates by dx and dy respectively
def offset_rectangle(rect, dx, dy):
    x = rect.corner.x + dx
    y = rect.corner.y + dy
    return(create_rectangle(x, y, rect.width, rect.height))

# testing code below

# first line
r1 = create_rectangle(10, 20, 30, 40)
print(str_rectangle(r1))

# second line
shift_rectangle(r1, -10, -20)
print(str_rectangle(r1))

# third line
print(str_rectangle(r1)) #should be same as previous

# fourth line
r2 = offset_rectangle(r1, 100, 100)
print(str_rectangle(r2))