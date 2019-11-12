import board
import keyboard
from os import system, name


class Game:
    def __init__(self):
        self._board = board.Board()
        self._exit = False

    def run(self):
        self._board.initialize_board()
        while self._exit is False:
            self._draw()
            self._check_input()

    def _check_input(self):
        input_key = input("Move: ")
        if input_key is Key.up:
            self._board.move_and_generate(board.Move.up)
        elif input_key is Key.down:
            self._board.move_and_generate(board.Move.down)
        elif input_key is Key.left:
            self._board.move_and_generate(board.Move.left)
        elif input_key is Key.right:
            self._board.move_and_generate(board.Move.right)
        elif input_key is Key.exit:
            self._exit = True

    def _draw(self):
        clear()
        print(self._board)


class Key:
    up = 'w'
    down = 's'
    left = 'a'
    right = 'd'
    exit = 'esc'


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
