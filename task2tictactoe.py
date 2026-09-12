board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]


def reset_board():
    for i in range(3):
        for j in range(3):
            board[i][j] = " "


def print_board():
    print("\nCurrent Board:\n")

    for i in range(3):
        print(" " + board[i][0] + " | " + board[i][1] + " | " + board[i][2])

        if i < 2:
            print("---|---|---")

    print()


def print_box_guide():
    print("Box Number Guide:")
    print()
    print(" 1 | 2 | 3")
    print("---|---|---")
    print(" 4 | 5 | 6")
    print("---|---|---")
    print(" 7 | 8 | 9")
    print()

def check_winner(player):
    # Check rows
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True

    # Check columns
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True

    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False


def is_board_full():
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                return False

    return True


def minimax(depth, is_ai_turn, alpha, beta):
    # Base cases
    if check_winner("O"):
        return 10 - depth

    if check_winner("X"):
        return depth - 10

    if is_board_full():
        return 0

    # AI turn, so maximize score
    if is_ai_turn:
        best_score = -1000

        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"

                    score = minimax(depth + 1, False, alpha, beta)

                    board[i][j] = " "

                    best_score = max(best_score, score)
                    alpha = max(alpha, best_score)

                    # Alpha-Beta Pruning
                    if beta <= alpha:
                        return best_score

        return best_score

    # Human turn, so minimize score
    else:
        best_score = 1000

        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"

                    score = minimax(depth + 1, True, alpha, beta)

                    board[i][j] = " "

                    best_score = min(best_score, score)
                    beta = min(beta, best_score)

                    # Alpha-Beta Pruning
                    if beta <= alpha:
                        return best_score

        return best_score


def ai_move():
    best_score = -1000
    best_move = None

    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"

                score = minimax(0, False, -1000, 1000)

                board[i][j] = " "

                if score > best_score:
                    best_score = score
                    best_move = (i, j)

    if best_move is not None:
        row, col = best_move
        board[row][col] = "O"


def human_move():
    while True:
        try:
            box = int(input("Enter box number 1-9: "))

            if box < 1 or box > 9:
                print("Invalid box number. Please choose from 1 to 9.")
                continue

            # Convert box number into board index
            row = (box - 1) // 3
            col = (box - 1) % 3

            if board[row][col] != " ":
                print("This box is already filled. Choose another box.")
            else:
                board[row][col] = "X"
                break

        except ValueError:
            print("Invalid input. Please enter a number from 1 to 9.")


def ask_restart():
    print("\nTo restart the game, type Y and press Enter.")
    print("To exit the game, type N and press Enter.")

    while True:
        choice = input("Do you want to restart the game? (Y/N): ").lower()

        if choice == "y":
            return True
        elif choice == "n":
            return False
        else:
            print("Invalid choice. Please enter Y or N.")


def play_game():
    while True:
        reset_board()

        print("===================================")
        print("        TIC-TAC-TOE AI GAME        ")
        print("===================================")
        print("You are X")
        print("AI is O")
        print()

        print_box_guide()
        print_board()

        while True:
            print("Your Turn")
            human_move()
            print_board()

            if check_winner("X"):
                print("You won the game!")
                break

            if is_board_full():
                print("Game Draw!")
                print("No box is empty now.")
                break

            print("AI Turn")
            ai_move()
            print_board()

            if check_winner("O"):
                print("AI won the game!")
                break

            if is_board_full():
                print("Game Draw!")
                print("No box is empty now.")
                break

        restart = ask_restart()

        if restart:
            print("\nRestarting the game...\n")
        else:
            print("\nThank you for playing!")
            break


play_game()