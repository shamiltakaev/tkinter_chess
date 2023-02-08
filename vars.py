import tkinter
from PIL import ImageTk, Image
from board import Board

root = tkinter.Tk()
board_cl = Board()
board = board_cl.board
root.geometry("800x800+0+0")
x_how, y_how = 0, 0
x_much, y_much = 0, 0
root.resizable = False
canvas = tkinter.Canvas()
tables_cell = {

}
