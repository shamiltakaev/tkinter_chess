import os
import tkinter
from PIL import ImageTk, Image
root = tkinter.Tk()

root.geometry("800x800+0+0")


canvas = tkinter.Canvas()
tables_cell = {

}
for row in range(8):
    color = "white" if row % 2 == 0 else "gray"
    for col in range(8):
        y = col * 100
        x = row * 100
        canvas.create_rectangle(y, x, y + 100, x + 100, fill=color)
        color = "gray" if color == "white" else "white"
        tables_cell[(row, col)] = y, x, y + 100, x + 100

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
    tag = f"white{char}{i // 8 + 6}{i % 8}"
    print(tag, end=" ")

    if char in ids:
        for j in range(2, 9):
            if char in ids:
                char = f"{char[:1]}{j}"
    ids[char] = canvas.create_image(x, y, image=white_pieces[i], tags=(tag))
    
print()

canvas.place(x=0, y=0, width=800, height=800)
def bishop_move(event, tag):
    canvas.coords(tag, event.x, event.y)
    
canvas.tag_bind("whiteb75", "<B1-Motion>", lambda e, b="": bishop_move(e, "whiteb75"))
def canvas_click(event):
    x, y = event.x, event.y
    for key, value in tables_cell.items():
        if (value[0] <= x <= value[2]) and (value[1] <= y <= value[3]):
            pass


canvas.bind("<Button-1>", canvas_click)

root.mainloop()
