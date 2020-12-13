import turtle
import document


class DrawCircle(document.Document):

    def __init__(self, radius, pos_x, pos_y):
        super(pos_x, pos_y)
        self.__radius = radius

    def show(self):
        turtle.tracer(False)
        turtle.penup()
        turtle.goto(self._pos_x, self._pos_y)
        turtle.pendown()
        turtle.circle(self.__radius)
        turtle.exitonclick()
        turtle.penup()
        turtle.update()

    def setRadius(self, radius):
        self.__radius = radius

    def getRadius(self):
        return self.__radius


a=document(DrawCircle(100))
a.show()

