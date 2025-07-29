# Main file - just for running and keep my trash code hidden in an organized manner
# from engine import Engine
from game import Game



def play_game():
    new_game = Game()
    test_counter = 6
    while not new_game.is_finished() and not test_counter < 1:
        input_move = input("Your turn (use algebric notations) > ")
        new_game.next_move(input_move)
        test_counter -= 1

# This is the main run file if you want to run the engine standalone in a terminal.
def main():
    """Main method of running the engine"""
    # current_engine = Engine()
    # current_engine.run()
    play_game()


if __name__ == '__main__':
    main()
