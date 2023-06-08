
from abc import abstractmethod
from Board import Board_class
import random
from Player import Player



class ComputerPlayer(Player):
    def move(self):
        number = random.choice(self.board.get_free_slots())
        print("number = ", number)
        self.board.change_board_state(number, self.value)


