class Board_class:
    def __init__(self) -> None:
        self.board_state = ["*", "*", "*", "*", "*", "*", "*", "*", "*"]

    def change_board_state(self, number: int, string: str):
        """change board state
        args:
        number(int): coordinates
        string(str): x or o"""
        rows = 3
        columns = 3
        row = (number - 1) // columns
        column = (number - 1) % columns
        self.board_state[row * columns + column] = string
        self.print_board()

    def print_board(self):
        rows = 3
        columns = 3
        for row in range(rows):
            for column in range(columns):
                print(self.board_state[row * columns + column], end=" ")
            print()


    def get_free_slots(self):
        free_slots = []
        for index, value in enumerate(self.board_state):
            if value == "*":
                free_slots.append(index+1)
        return free_slots







if __name__ == "__main__":
    b = Board_class()
    b.change_board_state(3, "x")
    b.change_board_state(5, "o")
    b.print_board()