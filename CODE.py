import random


Player_1 = ""
Player_2 = ""

def create_board(box):
    k = 1
    for i in range(0, 3):
        row = []
        for j in range(0, 3):
            row.append(" ")
            k += 1
        box.append(row)

def get_board(box):
    for i in range(0, 3):
        for j in range(0, 3):
            if j < 2:
                print(box[i][j], " | ", end=" ")
            else:
                print(box[i][j])
                if i < 2:
                    print("---------------")

def toss():
    global Player_1, Player_2
    while True:
        x = input("\nEnter 'TOSS' to start the game: ")

        if x == 'TOSS':
            toss_choice = random.choice(['Player-1', 'Player-2'])
            print(toss_choice, "won the toss")
            selection(toss_choice)
            break
        else:
            print("Invalid input. Please enter 'TOSS' to start the game.")

def selection(toss_choice):
    global Player_1, Player_2
    if (toss_choice == 'Player-1'):
        Player_1 = input("Player-1, enter your choice either 'X' or 'O': ")
        if Player_1 == 'X':
            Player_2 = 'O'
        elif Player_1 == 'O':
            Player_2 = 'X'
        else:
            print("Select the option within given choices only")
            selection(toss_choice)

        print(toss_choice, "selected option", Player_1, "and Player-2 got the option", Player_2)
    else:
        Player_2 = input("Player-2, enter your choice either 'X' or 'O': ")
        if Player_2 == 'X':
            Player_1 = 'O'
        elif Player_2 == 'O':
            Player_1 = 'X'
        else:
            print("Select the option within given choices only")
            selection(toss_choice)

        print(toss_choice, "selected the option", Player_2, "and Player-1 got the option", Player_1)

def is_winner(board, player):

    for i in range(3):
        row_win = True
        for j in range(3):
            if board[i][j] != player:
                row_win = False
                break
        if row_win:
            return True


    for j in range(3):
        col_win = True
        for i in range(3):
            if board[i][j] != player:
                col_win = False
                break
        if col_win:
            return True


    diagonal1_win = True
    diagonal2_win = True

    for i in range(3):
        if board[i][i] != player:
            diagonal1_win = False
        if board[i][2 - i] != player:
            diagonal2_win = False

    if diagonal1_win or diagonal2_win:
        return True

    return False

def is_board_full(board):
    for row in board:
        if " " in row:
            return False
    return True

def make_move(board, player):
    while True:
        row,col = eval(input(f"{player}, enter your co-ordinates (0-2): "))
        if 0 <= row <= 3 and 0<=col <=3:
            if board[row][col] == " ":
                board[row][col] = player
                break
            else:
                print("That position is already taken. Try again.")
        else:
            print("Invalid input. Please enter a number between 1 and 9.")


def play_game():
    box = []
    create_board(box)
    get_board(box)
    toss()
    current_player = Player_1

    while True:
        make_move(box, current_player)
        get_board(box)

        if is_winner(box, current_player):
            print(current_player, "wins!")
            break
        elif is_board_full(box):
            print("It's a tie!")
            break

        if current_player == Player_2:
            current_player=Player_1
        else:
            current_player=Player_2

play_game()
