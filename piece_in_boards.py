from pieces import Bishop, Rook, Knight, Queen, King, Pawn
from vars import canvas
white_r_1 = Rook("white")
white_b_1 = Bishop("white")
white_n_1 = Knight("white")
white_q_1 = Queen("white")
white_k_1 = King("white")
white_b_2 = Bishop("white")
white_n_2 = Knight("white")
white_r_2 = Rook("white")
white_p_1 = Pawn("white")
white_p_2 = Pawn("white")
white_p_3 = Pawn("white")
white_p_4 = Pawn("white")
white_p_5 = Pawn("white")
white_p_6 = Pawn("white")
white_p_7 = Pawn("white")
white_p_8 = Pawn("white")

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

def set_pieces(board, list):
    board[7][0] = list[0]
    board[7][1] = list[1]
    board[7][2] = list[2]
    board[7][3] = list[3]
    board[7][4] = list[4]
    board[7][5] = list[5]
    board[7][6] = list[6]
    board[7][7] = list[7]
    board[6][0] = list[8]
    board[6][1] = list[9]
    board[6][2] = list[10]
    board[6][3] = list[11]
    board[6][4] = list[12]
    board[6][5] = list[13]
    board[6][6] = list[14]
    board[6][7] = list[15]