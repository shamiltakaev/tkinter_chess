def bishop_move(event, tag, canvas):
    canvas.coords(tag, event.x, event.y)


def bishop_click(event, tag, tables_cell):
    print(event.x, event.y)
    x, y = event.x, event.y
    for key, value in tables_cell.items():
        if (value[0] <= x <= value[2]) and (value[1] <= y <= value[3]):
            row, col = key
    # white_b_1.set_position(row, col)