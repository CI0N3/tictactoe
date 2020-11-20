import tictactoe as ttt


def game():

    board = ttt.initial_state()
    user = input("X or O? ")
    game_over = ttt.terminal(board)

    def print_board(board):
        print("")
        print(board[0])
        print(board[1])
        print(board[2])

    while game_over is False:
        """""
        If the user is X and the ai is O
        """""
        if user == "X":
            player = ttt.player(board)
            if player == "X":
                print_board(board)
                square = int(input("Which square (0-8)? "))
                if square < 3 and square > -1 and board[0][square] == None:
                    board = ttt.result(board, ("(0, " + str(square) + ")"))
                elif square > 5 and square < 9 and board[2][square - 6] == None:
                    board = ttt.result(board, (2, square - 6))
                elif square > 2 and square < 6 and board[1][square - 3] == None:
                    board = ttt.result(board, (1, square - 3))
                else:
                    print("Try again.\n")
                game_over = ttt.terminal(board)

            elif player == "O":
                board = ttt.result(board, ttt.minimax(board))
                game_over = ttt.terminal(board)

        """""
        If the user is O and the ai is X
        """""
        if user == "O":
            player = ttt.player(board)
            if player == "X":
                board = ttt.result(board, ttt.minimax(board))
                game_over = ttt.terminal(board)

            elif player == "O":
                print_board(board)
                square = int(input("Which square (0-8)? "))
                if square < 3 and square > -1 and board[0][square] == None:
                    board = ttt.result(board, ("(0, " + str(square) + ")"))
                elif square > 5 and square < 9 and board[2][square - 6] == None:
                    board = ttt.result(board, (2, square - 6))
                elif square > 2 and square < 6 and board[1][square - 3] == None:
                    board = ttt.result(board, (1, square - 3))
                else:
                    print("Try again.\n")
                game_over = ttt.terminal(board)

    """""
    Once the while loop is broken (when a terminal state of the board is reached) then it prints the results of the game
    """""
    print_board(board)
    if ttt.utility(board) != 0:
        if ttt.utility(board) == 1:
            print("X has won!")
        else:
            print("O has won!")
    else:
        print("Tie!")


game()

