import random


class GameBoard:
    def __init__(self, board):
        self.board = board

    def change_letters_to_nums():
        change_letters = {"A":0 , "B":1, "C":2, "D":3, "E":4, "F":5, "G":6, "H":7}
        return change_letters

    def print_board(self):
        print("  A B C D E F G H")
        print("  ---------------")
        row_number = 1
        for row in self.board:
            print(f"  {row_number} |".join(row))
            row_number +=1


