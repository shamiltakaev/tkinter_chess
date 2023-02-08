from piece_in_boards import (white_b_1, white_b_2, white_k_1, white_n_1, 
                             white_n_2, white_p_1, white_p_2, white_p_3, 
                             white_p_4, white_p_5, white_p_6, white_p_7, 
                             white_p_8, white_q_1, white_r_1, white_r_2,
                             set_pieces)
# import os
import tkinter
# from PIL import ImageTk, Image
# from board import Board
# root = tkinter.Tk()
# board_cl = Board()
# board = board_cl.board
# root.geometry("800x800+0+0")
# x_how, y_how = 0, 0
# x_much, y_much = 0, 0
# root.resizable = False
# canvas = tkinter.Canvas()
# tables_cell = {

# }
from vars import root, board, board_cl, x_how, y_how, x_much, y_much, canvas, tables_cell
from PIL import Image, ImageTk
for row in range(8):
    color = "white" if row % 2 == 0 else "gray"
    for col in range(8):
        y = col * 100
        x = row * 100
        canvas.create_rectangle(y, x, y + 100, x + 100, fill=color)
        tables_cell[(row, col)] = y, x, y + 100, x + 100
        color = "gray" if color == "white" else "white"

# region Load Figures
black_src = [
    "blackr", "blackn", "blackb", "blackq", "blackk", "blackb", "blackn", "blackr",
    *["blackp"] * 8
]
black_src = [f"img/{url}.png" for url in black_src]

black_pieces = [
    ImageTk.PhotoImage(Image.open(url)) for url in black_src
]
black_pieces_id = []
for i in range(len(black_pieces)):
    x = i % 8 * 100 + 50
    y = i // 8 * 100 + 50
    char = black_src[i][-5]
    print(f"white{char}{i // 8}{i % 8 }", end=" ")
    black_pieces_id.append(canvas.create_image(x, y, image=black_pieces[i]))
print()
# endregion

white_src = [
    *["whitep"] * 8,
    "whiter", "whiten", "whiteb", "whiteq", "whitek", "whiteb", "whiten", "whiter"
]

white_src = [f"img/{url}.png" for url in white_src]

white_pieces = [
    ImageTk.PhotoImage(Image.open(url)) for url in white_src
]
ids = {}
for i in range(len(white_pieces)):
    x = i % 8 * 100 + 50
    y = i // 8 * 100 + 650
    char = white_src[i][-5]
    tag = f"white{char}{i % 8}"
    print(tag, end=" ")

    if char in ids:
        for j in range(2, 9):
            if char in ids:
                char = f"{char}{j}"
    ids[char] = canvas.create_image(x, y, image=white_pieces[i], tags=(tag))

print()

canvas.place(x=0, y=0, width=800, height=800)


def piece_move(event, tag):
    if 0 < event.x < 800 and 0 < event.y < 780:
        canvas.coords(tag, event.x, event.y)


def piece_click(event, tag, piece):
    x, y = event.x, event.y
    for key, value in tables_cell.items():
        if (value[0] <= x <= value[2]) and (value[1] <= y <= value[3]):
            row, col = key
    piece.set_position(row, col)


def piece_unclick(event, tag, piece):
    x, y = event.x, event.y
    for key, value in tables_cell.items():
        if (value[0] <= x <= value[2]) and (value[1] <= y <= value[3]):
            row, col = key
            break
    canvas.moveto(tag, col * 100 + 18, row * 100 + 18)
    if board_cl.move_piece(piece, row, col) is False:
        canvas.moveto(tag, piece.col * 100 + 18, piece.row * 100 + 18)

white_r_1_tag = canvas.gettags("whiter0")
white_n_1_tag = canvas.gettags("whiten1")
white_b_1_tag = canvas.gettags("whiteb2")
white_q_1_tag = canvas.gettags("whiteq3")
white_k_1_tag = canvas.gettags("whitek4")
white_b_2_tag = canvas.gettags("whiteb5")
white_n_2_tag = canvas.gettags("whiten6")
white_r_2_tag = canvas.gettags("whiter7")
white_p_1_tag = canvas.gettags("whitep0")
white_p_2_tag = canvas.gettags("whitep1")
white_p_3_tag = canvas.gettags("whitep2")
white_p_4_tag = canvas.gettags("whitep3")
white_p_5_tag = canvas.gettags("whitep4")
white_p_6_tag = canvas.gettags("whitep5")
white_p_7_tag = canvas.gettags("whitep6")
white_p_8_tag = canvas.gettags("whitep7")
set_pieces(board, [white_r_1, white_n_1, white_b_1, white_q_1, white_k_1, white_b_2, white_n_2, white_r_2,
white_p_1, white_p_2, white_p_3, white_p_4, white_p_5, white_p_6, white_p_7, white_p_8])

board_cl.print_board()
# region Bind_events
canvas.tag_bind(white_r_1_tag, "<B1-Motion>", lambda e,
                tag="": piece_move(e, white_r_1_tag))
canvas.tag_bind(white_r_1_tag, "<Button-1>", lambda e,
                tag="": piece_click(e, white_r_1_tag, white_r_1))
canvas.tag_bind(white_r_1_tag, "<ButtonRelease>", lambda e,
                tag="": piece_unclick(e, white_r_1_tag, white_r_1))
canvas.tag_bind(white_n_1_tag, "<B1-Motion>", lambda e,
                tag="": piece_move(e, white_n_1_tag))
canvas.tag_bind(white_n_1_tag, "<Button-1>", lambda e,
                tag="": piece_click(e, white_n_1_tag, white_n_1))
canvas.tag_bind(white_n_1_tag, "<ButtonRelease>", lambda e,
                tag="": piece_unclick(e, white_n_1_tag, white_n_1))
canvas.tag_bind(white_b_1_tag, "<B1-Motion>", lambda e,
                tag="": piece_move(e, white_b_1_tag))
canvas.tag_bind(white_b_1_tag, "<Button-1>", lambda e,
                tag="": piece_click(e, white_b_1_tag, white_b_1))
canvas.tag_bind(white_b_1_tag, "<ButtonRelease>", lambda e,
                tag="": piece_unclick(e, white_b_1_tag, white_b_1))
canvas.tag_bind(white_q_1_tag, "<B1-Motion>", lambda e,
                tag="": piece_move(e, white_q_1_tag))
canvas.tag_bind(white_q_1_tag, "<Button-1>", lambda e,
                tag="": piece_click(e, white_q_1_tag, white_q_1))
canvas.tag_bind(white_q_1_tag, "<ButtonRelease>", lambda e,
                tag="": piece_unclick(e, white_q_1_tag, white_q_1))
canvas.tag_bind(white_k_1_tag, "<B1-Motion>", lambda e,
                tag="": piece_move(e, white_k_1_tag))
canvas.tag_bind(white_k_1_tag, "<Button-1>", lambda e,
                tag="": piece_click(e, white_k_1_tag, white_k_1))
canvas.tag_bind(white_k_1_tag, "<ButtonRelease>", lambda e,
                tag="": piece_unclick(e, white_k_1_tag, white_k_1))
canvas.tag_bind(white_b_2_tag, "<B1-Motion>", lambda e,
                tag="": piece_move(e, white_b_2_tag))
canvas.tag_bind(white_b_2_tag, "<Button-1>", lambda e,
                tag="": piece_click(e, white_b_2_tag, white_b_2))
canvas.tag_bind(white_b_2_tag, "<ButtonRelease>", lambda e,
                tag="": piece_unclick(e, white_b_2_tag, white_b_2))
canvas.tag_bind(white_n_2_tag, "<B1-Motion>", lambda e,
                tag="": piece_move(e, white_n_2_tag))
canvas.tag_bind(white_n_2_tag, "<Button-1>", lambda e,
                tag="": piece_click(e, white_n_2_tag, white_n_2))
canvas.tag_bind(white_n_2_tag, "<ButtonRelease>", lambda e,
                tag="": piece_unclick(e, white_n_2_tag, white_n_2))
canvas.tag_bind(white_r_2_tag, "<B1-Motion>", lambda e,
                tag="": piece_move(e, white_r_2_tag))
canvas.tag_bind(white_r_2_tag, "<Button-1>", lambda e,
                tag="": piece_click(e, white_r_2_tag, white_r_2))
canvas.tag_bind(white_r_2_tag, "<ButtonRelease>", lambda e,
                tag="": piece_unclick(e, white_r_2_tag, white_r_2))

canvas.tag_bind(white_p_1_tag, "<B1-Motion>", lambda e,
                tag="": piece_move(e, white_p_1_tag))
canvas.tag_bind(white_p_1_tag, "<Button-1>", lambda e,
                tag="": piece_click(e, white_p_1_tag, white_p_1))
canvas.tag_bind(white_p_1_tag, "<ButtonRelease>", lambda e,
                tag="": piece_unclick(e, white_p_1_tag, white_p_1))
canvas.tag_bind(white_p_2_tag, "<B1-Motion>", lambda e,
                tag="": piece_move(e, white_p_2_tag))
canvas.tag_bind(white_p_2_tag, "<Button-1>", lambda e,
                tag="": piece_click(e, white_p_2_tag, white_p_2))
canvas.tag_bind(white_p_2_tag, "<ButtonRelease>", lambda e,
                tag="": piece_unclick(e, white_p_2_tag, white_p_2))
canvas.tag_bind(white_p_3_tag, "<B1-Motion>", lambda e, tag="": piece_move(e, white_p_3_tag))
canvas.tag_bind(white_p_3_tag, "<Button-1>", lambda e, tag="": piece_click(e, white_p_3_tag, white_p_3))
canvas.tag_bind(white_p_3_tag, "<ButtonRelease>", lambda e, tag="": piece_unclick(e, white_p_3_tag, white_p_3))
canvas.tag_bind(white_p_4_tag, "<B1-Motion>", lambda e, tag="": piece_move(e, white_p_4_tag))
canvas.tag_bind(white_p_4_tag, "<Button-1>", lambda e, tag="": piece_click(e, white_p_4_tag, white_p_4))
canvas.tag_bind(white_p_4_tag, "<ButtonRelease>", lambda e, tag="": piece_unclick(e, white_p_4_tag, white_p_4))
canvas.tag_bind(white_p_5_tag, "<B1-Motion>", lambda e, tag="": piece_move(e, white_p_5_tag))
canvas.tag_bind(white_p_5_tag, "<Button-1>", lambda e, tag="": piece_click(e, white_p_5_tag, white_p_5))
canvas.tag_bind(white_p_5_tag, "<ButtonRelease>", lambda e, tag="": piece_unclick(e, white_p_5_tag, white_p_5))
canvas.tag_bind(white_p_6_tag, "<B1-Motion>", lambda e, tag="": piece_move(e, white_p_6_tag))
canvas.tag_bind(white_p_6_tag, "<Button-1>", lambda e, tag="": piece_click(e, white_p_6_tag, white_p_6))
canvas.tag_bind(white_p_6_tag, "<ButtonRelease>", lambda e, tag="": piece_unclick(e, white_p_6_tag, white_p_6))
canvas.tag_bind(white_p_7_tag, "<B1-Motion>", lambda e, tag="": piece_move(e, white_p_7_tag))
canvas.tag_bind(white_p_7_tag, "<Button-1>", lambda e, tag="": piece_click(e, white_p_7_tag, white_p_7))
canvas.tag_bind(white_p_7_tag, "<ButtonRelease>", lambda e, tag="": piece_unclick(e, white_p_7_tag, white_p_7))
canvas.tag_bind(white_p_8_tag, "<B1-Motion>", lambda e, tag="": piece_move(e, white_p_8_tag))
canvas.tag_bind(white_p_8_tag, "<Button-1>", lambda e, tag="": piece_click(e, white_p_8_tag, white_p_8))
canvas.tag_bind(white_p_8_tag, "<ButtonRelease>", lambda e, tag="": piece_unclick(e, white_p_8_tag, white_p_8))
# endregion
root.mainloop()
