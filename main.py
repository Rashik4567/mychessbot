# Main file - just for running and keep my trash code hidden in an organized manner
from engine import Engine


class Game:
    def __init__(self):
        pass
    def next_move(self, move):
        pass
    def _is_finished(self):
        return False


def play_game():
    new_game = Game()
    while not new_game._is_finished():
        input_move = input("Your turn > ")
        new_game.next_move(input_move)

def main():
    """Main method of running the engine"""
    current_engine = Engine()
    # current_engine.run()
    play_game()


if __name__ == '__main__':
    main()