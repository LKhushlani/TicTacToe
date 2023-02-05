import os

os.system('clear')


class Board:
    def __init__(self):
        self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

    def display(self):
        print(" %s | %s | %s " % (self.cells[1], self.cells[2], self.cells[3]))
        print("--------------")
        print(" %s | %s | %s " % (self.cells[4], self.cells[5], self.cells[6]))
        print("--------------")
        print(" %s | %s | %s " % (self.cells[7], self.cells[8], self.cells[9]))

    def update_cell(self, cell_no, player):
        if self.cells[cell_no] == ' ':
            self.cells[cell_no] = player

    def is_winner(self, player):
        winning_combos = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
        result = True
        for combo in winning_combos:
            for cell_num in combo:
                if self.cells[cell_num] != player:
                    return False

            if result == True:
                return True

    def reset_board(self):
        self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

    def ai_move(self, player):

        if player == 'X':
            enemy = 'O'
        else:
            enemy = 'X'

        #occupy center
        if self.cells[5] == " ":
            self.update_cell(5,player)

        #AI Wins

        #AI Blocks

        #Random Move
        for i in range(1,10):
            if self.cells[i] != ' ':
                self.update_cell(i,player)
                break

    def is_tie(self):
        used_cells = 0
        for cell in self.cells:
            if cell != ' ':
                used_cells += 1
        if used_cells == 9:
            return True
        else:
            return False


board = Board()


def print_header():
    print('Welcome to tic - tac - toe')


def refresh_screen():
    # clear the screen
    os.system("clear")

    # print header
    print_header()

    # Show the board
    board.display()


while True:

    refresh_screen()

    # Get X input
    x_choice = int(input("\n X) Please choose 1-9. > "))
    # update board
    board.update_cell(x_choice, 'X')
    # refresh screen
    refresh_screen()

    if board.is_winner('X'):
        print('\n X Wins \n')
        play_again = input("Would you like to play again ? (Y/N)").upper()
        if play_again == 'Y':
            board.reset_board()
            continue
        else:
            break

    if board.is_tie():
        print('\n Tie \n')
        play_again = input("Would you like to play again ? (Y/N)").upper()
        if play_again == 'Y':
            board.reset_board()
            continue
        else:
            break

    # Get O input
    x_choice = int(input("\n O) Please choose 1-9. > "))
    # update board
    board.update_cell(x_choice, 'O')

    # refresh screen
    refresh_screen()

    # Check for O win
    if board.is_winner('O'):
        print('\n O Wins \n')
        play_again = input("Would you like to play again ? (Y/N)").upper()
        if play_again == 'Y':
            board.reset_board()
            continue
        else:
            break

    if board.is_tie():
        print('\n  Tie \n')
        play_again = input("Would you like to play again ? (Y/N)").upper()
        if play_again == 'Y':
            board.reset_board()
            continue
        else:
            break
