
from abc import abstractmethod
from Board import Board_class
from Player import Player


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





