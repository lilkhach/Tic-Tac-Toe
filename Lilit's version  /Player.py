
from abc import abstractmethod
from Board import Board_class
import random

class Player:
    def __init__(self, value: str, board: Board_class) -> None:
        self.value = value
        self.board = board


@abstractmethod
def move(self):
    pass

class HumanPlayer(Player):
    def move(self):
        while True: 
            number = input("Please, enter the number from 1-9: ")
            if number.isdigit():
                number = int(number)
            else:
                print("Type integer from 1 - 9")
                continue

            if number not in list(range(1, 10)):
                print("Integer should be from 1 to 9")
                continue

            if number not in self.board.get_free_slots():
                print(f"Choosen slot is not available! Choose another number from {self.board.get_free_slots()} this options!")
                continue

            break
        print("number = ", number)
        self.board.change_board_state(number, self.value)




class ComputerPlayer(Player):
    def move(self):
        number = random.choice(self.board.get_free_slots())
        print("number = ", number)
        self.board.change_board_state(number, self.value)



if __name__ == "__main__":
    board = Board_class()
    human = HumanPlayer("X", board)
    computer = ComputerPlayer("O", board)

    human.move()
    computer.move()
    board.print_board()
