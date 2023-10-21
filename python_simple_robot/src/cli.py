"""CLI interface for robot project.
"""
import logging
import argparse
from robot.lib.robot import Robot
from robot.lib.room import Room
from robot.config import LOG_LEVEL


logging.basicConfig(level=LOG_LEVEL)
logger = logging.getLogger()
parser = argparse.ArgumentParser()




def main():
    """
    The main function executes on commands:
    `python cli.py `.

    This is the program's entry point.
    """
    try:
        parser.add_argument("-rw", "--room_width", default=5, type=int)
        parser.add_argument("-rd", "--room_depth", default=5, type=int)
        parser.add_argument("-spx", "--start_position_x", default=1, type=int)
        parser.add_argument("-spy", "--start_position_y", default=3, type=int)
        parser.add_argument("-so", "--start_orientation", default="N", type=str)
        parser.add_argument("-nc", "--navigation_commands", default="FFFL", type=str)

        args = parser.parse_args()
        room_width = args.room_width
        room_depth = args.room_depth
        start_position_x = args.start_position_x
        start_position_y = args.start_position_y
        start_orientation = args.start_orientation
        navigation_commands = args.navigation_commands

    except Exception as err: #TODO write a more precise exception
        logger.error(err)
        logger.info("Couldn't get all required arguments. Let's try interactive mode")
        # Get input from user:
        # TODO: implement input validation for user input
        room_width, room_depth = input("Room size, [default: 5 7] :- ").split() or (5, 7)  #
        start_position_x, start_position_y, start_orientation = input("Starting position and orientation  [default: 1 3 W]:- ").split() or (1, 3, "N")
        navigation_commands = (input("Navigation commands, [default: FFFL] :- ").upper() or "FFFL")

    # Initialize a room:
    room = Room(room_width=int(room_width), room_depth=int(room_depth))

    # Initialize a Robot
    robot = Robot(
        position={"x": int(start_position_x), "y": int(start_position_y)},
        orientation=start_orientation,
        room=room,
    )

    logger.info(f"Robot's start position:{robot}")
    robot.move(directions=navigation_commands)
    logger.info(f"Robot's finish position:{robot}")


if __name__ == "__main__":
    main()
