import random


class GameBoard:
    """
    This class will create the board and the surrounds of the board.
    """
    def __init__(self, board):
        self.board = board

    def change_letters_to_nums(self):
        change_letters = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7}
        return change_letters

    def print_board(self):
        print("  A B C D E F G H")
        print("  ---------------")
        row_number = 1
        for row in self.board:
            print(f"  {row_number} |".join(row))
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
        for i in range(5):
            self.x_row, self.y_column = random.randint(0, 7), random.randint(0, 7)
            while self.board[self.x_row][self.y_column]== "X":
                self.x_row, self.y_column = random.randint(0, 7), random.randint(0, 7)
            self.board[self.x_row][self.y_column] = "X"
        return self.board
    

    def user_input(self):
        try:
            x_row = input("Enter the row of the ship: ")
            while x_row not in '12345678':
                print("not an appropriate choice, please select a row between 1 and 8")
                x_row = input("Enter the row of the ship: ")
            