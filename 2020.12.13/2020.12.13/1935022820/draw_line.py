import turtle
import document


class Drawline(document.Document):

    def __init__(self, pos_x, pos_y, des_pos_x, des_pos_y):
        super.__init__(pos_x, pos_y)
        self.__des_pos_x = des_pos_x
        self.__des_pos_y = des_pos_y

    def show(self):
        turtle.tracer(False)
        turtle.penup()
        turtle.goto(self._pos_x, self._pos_y)
        turtle.pendown()
        turtle.goto(self.__des_pos_x, self.__des_pos_y)
        turtle.penup()
        turtle.update()

    def setDes(self, des_pos_x, des_pos_y):
        self.__des_pos_x = des_pos_x
        self.__des_pos_y = des_pos_y
