import turtle
import document


class DrawRect(document.Document):

    def __init__(self, length, width, pos_x, pos_y):
        super.__init__(pos_x, pos_y)
        self.__length = length
        self.__width = width

    def show(self):
        turtle.tracer(False)
        turtle.penup()
        turtle.goto(self._pos_x, self._pos_y)
        turtle.pendown()
        turtle.setheading(0)
        turtle.forward(self.__length)
        turtle.right(90)
        turtle.forward(self.__width)
        turtle.right(90)
        turtle.forward(self.__length)
        turtle.right(90)
        turtle.forward(self.__width)
        turtle.right(90)
        turtle.penup()
        turtle.update()

    def setLength(self, length):
        self.__length = length

    def setWidth(self, width):
        self.__width = width
