"""
File: room.py
Description: contains methods for the room class
"""
from dataclasses import dataclass


@dataclass
class Room:
    """
    This class describes the room size and can check if robot did hit the wall.

    Parameters:
        room_width(int): room width.
        room_depth(int): room depth.
    """

    room_width: int
    room_depth: int

    def hit_a_wall(self, x: int, y: int) -> True | False:
        """
        Takes in the robot's position and checks if it did not hit the wall

        Parameters:
            x(int):    the X position of the robot.
            y(int):    the Y position of the robot.

        Returns:
            True - in case the robot hit the wall
            False - in case the robot did not hit the wall
        """
        return (
            True
            if x < 0 or x > self.room_width - 1 or y < 0 or y > self.room_depth - 1
            else False
        )
