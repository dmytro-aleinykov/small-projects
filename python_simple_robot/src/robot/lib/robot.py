"""
File: robot.py
Description: class for controling the robot
"""
import logging
from dataclasses import dataclass
from dataclasses import field
from .room import Room
from ..config import LOG_LEVEL


logging.basicConfig(level=LOG_LEVEL)
logger = logging.getLogger()


@dataclass
class Robot:
    """
    This class describes the robot, what it can do

    Parameters:
        position(dict):         the current position of the robot in a room.
                                Example: position={'x': 2, 'y': 2}, where x - room width, y - room deepness

        orientation(str):       the current orientation of the robot.
                                Example: N|W|S|E, where N - North, W - West, S - South, E - East

        steps_history(dict):    all steps done by robot
    """

    position: dict
    orientation: str
    room: Room = field(default_factory=Room, repr=False)
    steps_history: dict = field(default_factory=dict, repr=False)

    def set_new_position(self, direction: str) -> None:
        """
        Takes in a new direction for the robot and moves it to a new position

        Parameters:
            direction(str): allowed values: "R"-right, "L"-left, "F"-forward

        Returns: None
        """
        if direction == "F":
            if self.orientation == "N" and not self.room.hit_a_wall(
                x=self.position["x"], y=self.position["y"] + 1
            ):
                self.position["y"] = self.position["y"] + 1
            elif self.orientation == "S" and not self.room.hit_a_wall(
                x=self.position["x"], y=self.position["y"] - 1
            ):
                self.position["y"] = self.position["y"] - 1
            elif self.orientation == "W" and not self.room.hit_a_wall(
                x=self.position["x"] - 1, y=self.position["y"]
            ):
                self.position["x"] = self.position["x"] - 1
            elif self.orientation == "E" and not self.room.hit_a_wall(
                x=self.position["x"] + 1, y=self.position["y"]
            ):
                self.position["x"] = self.position["x"] + 1

    def set_new_orientation(self, direction: str) -> None:
        """
        Takes in a new direction for the robot and calculates its new position

        Parameters:
            direction(str): allowed values: "R"-right, "L"-left, "F"-forward

        Returns: None
        """
        orientations = ["N", "W", "S", "E"]
        indx = orientations.index(self.orientation)
        if direction == "R":
            indx = indx - 1
        elif direction == "L":
            indx = indx + 1 if indx < len(orientations) - 1 else 0
        elif direction == "F":
            pass

        self.orientation = orientations[indx]

    def move(self, directions: str) -> None:
        """
        Takes in all movements, which robot should do and moves it one step a time until all movements are done

        Parameters:
            direction(str): allowed values: "R"-right, "L"-left, "F"-forward

        Returns: None
        """
        for direction in directions:
            state_before_step = {
                "x": self.position["x"],
                "y": self.position["y"],
                "orientation": self.orientation,
            }
            self.set_new_position(direction=direction)
            self.set_new_orientation(direction=direction)
            state_after_step = {
                "x": self.position["x"],
                "y": self.position["y"],
                "orientation": self.orientation,
            }
            self.log_step(old_state=state_before_step, new_state=state_after_step)

    def log_step(self, old_state: dict, new_state: dict) -> None:
        """
        Takes in old and new robot's states and saves them to history of all steps

        Parameters:
            old_state(dict): robot's state before step
            new_state(dict): robot's state after step

        Returns: None
        """
        step_no: str = "Step" + str(len(self.steps_history) + 1)
        entry = {
            step_no: {
                "old_state": old_state,
                "new_state": new_state,
            }
        }
        self.steps_history.update(entry)
        logger.debug(
            f"{step_no}: X:{old_state['x']}, Y:{old_state['y']}, O: {old_state['orientation']} --> X:{new_state['x']}, Y:{new_state['y']}, O: {new_state['orientation']} "
        )
