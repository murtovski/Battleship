import random


class GameBoard:
    """
    This class will create the board and the surrounds of the board.
    """
    def __init__(self, board):
        self.board = board

    def change_letters_to_nums():
        change_letters = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5,
                          "G": 6, "H": 7}
        return change_letters

    def print_board(self):
        print("  A  B  C  D  E  F  G  H")
        print("  ---------------")
        row_number = 1
        for row in self.board:
            print(row_number, " |".join(row))
            row_number += 1


class Ship:
    """
    This class is to create the ships and apply them to the board.
    This class also makes sure the locations of the ships are validated
    so they do not land on the same location.
    """

    def __init__(self, board):
        self.board = board

    def create_ships(self):
        # this loop will validate the ship locations and
        # apply the ship to a random spot on the board
        for i in range(5):
            self.x_row, self.y_column = random.randint(0, 7), random.randint(0, 7)
            while self.board[self.x_row][self.y_column] == "X":
                self.x_row, self.y_column = random.randint(0, 7), random.randint(0, 7)
            self.board[self.x_row][self.y_column] = "X"
        return self.board

    def create_computer_ships():
        locations = []
        lat = []
        long = []
        while len(locations) < 5:
            row = random.randint(0, 7)
            col = random.randint(0, 7)
            lat.append(row)
            long.append(col)
            locations = list(dict.fromkeys(locations))
            locations = list(zip(lat, long))
        return locations

    def user_input(self):
        try:
            x_row = input("Enter the row of the ship: \n")
            while x_row not in '12345678' or x_row == "":
                print("not an appropriate choice, please select a row between 1 and 8")
                x_row = input("Enter the row of the ship: \n")

            y_column = input("Enter the column letter of the ship: \n").upper()
            while y_column not in "ABCDEFGH" or y_column == "":
                print("Not an appropriate range, please select a letter from A to G")
                y_column = input("Enter the column letter of the ship: \n").upper()
            return int(x_row) - 1, GameBoard.change_letters_to_nums()[y_column]
        except ValueError and KeyError:
            print("Not a valid input")
            return self.user_input()

    def computer_input(self):
        computer_x_row = random.randint(0, 7)
        computer_y_col = random.randint(0, 7)
        return int(computer_x_row) - 1, int(computer_y_col) - 1

    def hit_ships(self):
        hit_ships = 0
        for row in self.board:
            for column in row:
                if column == "X":
                    hit_ships += 1
        return hit_ships


def player_move(row, col, board, score, location):
    split = list(map(list, zip(*location)))
    lat, long = split
    # Checks for duplicate
    while board.board[row][col] == "-" or board.board[row][col] == "@":
        print("You have made that guess already")
        row, col = Ship.user_input(object)
    if row in lat and col in long:
        print("You sunk a Battleship!")
        board.board[row][col] = "@"
        score += 1
        return score
    else:
        print("You missed my Battleship")
        board.board[row][col] = "-"
        return score


def computer_move(row, col, board, score):
    # Checks for duplicate
    while board.board[row][col] == "-" or board.board[row][col] == "@":
        row, col = Ship.user_input(object)
    # checks for hits
    if board.board[row][col] == "X":
        print("The computer sunk a Battleship!")
        board.board[row][col] = "@"
        score += 1
        return score
    else:
        print("The computer missed my Battleship")
        board.board[row][col] = "-"
        return score


def RunGame():
    computer_board = GameBoard([[" "] * 8 for i in range(8)])
    player_board = GameBoard([[" "] * 8 for i in range(8)])
    Ship.create_ships(player_board)
    computer_location = Ship.create_computer_ships()
    player_score = 0
    computer_score = 0
    print("\n")
    print("WELCOME TO BATTLESHIP!")
    print("Make your move and wait for the computer to make their move")
    print("First to score five hits wins!")
    print("\n")

    # Starts turns
    while player_score < 5 and computer_score < 5:
        GameBoard.print_board(computer_board)
        print("COMPUTER'S BOARD")
        print(f"The computer's score is {computer_score}")
        print("----------------------------------------")
        GameBoard.print_board(player_board)
        print("PLAYER'S BOARD")
        print(f"Your score is {player_score}")
        print("----------------------------------------")
        print("\n")
        computer_row, computer_col = Ship.user_input(object)
        player_score = player_move(computer_row, computer_col, computer_board, player_score, computer_location)

        player_row, player_col = Ship.computer_input(object)
        computer_score = computer_move(player_row, player_col, player_board, computer_score)

    if computer_score == 5:
        print("The computer sank all your ships")
    else:
        print("You have won the game!!!!")


RunGame()
