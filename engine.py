import logging
import time

logging.getLogger()


class Engine:
    def __init__(self, starting_position='default', depth=10, time_per_move_in_seconds=0):
        logging.basicConfig(filename="mychessenginelog.log", level=logging.DEBUG)
        logging.info(msg=f"[{time.localtime()}]\nEngine initiated with arguments: {starting_position, depth, time_per_move_in_seconds}")
        if depth == 0 and time_per_move_in_seconds == 0:
            logging.critical(msg="No endpoint specified!")
            raise RecursionError(
                "No depth or time per move specified, engine doesn't have a stop condition.\nProbable cause: both depth=0 and time_per_move_in_seconds=0 in engine init.")

        self.starting_position = starting_position
        self.depth = depth
        self.time_per_move_in_seconds = time_per_move_in_seconds

    def engine_mode(self):
        pass

    def load_position(self, position):
        pass

    def run(self):
        pass
