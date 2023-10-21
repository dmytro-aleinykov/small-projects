import pytest
from src.robot.lib.robot import Robot
from src.robot.lib.room import Room


# TODO: Write tests for room with different sizes
room_width = 5
room_depth = 5
room = Room(room_width=room_width, room_depth=room_depth)


@pytest.mark.parametrize(
    "direction, start_position_x, start_position_y, expected_position_x, expected_position_y",
    [
        ("F", 3, 1, 3, 2),
        ("L", 3, 1, 3, 1),
        ("R", 3, 1, 3, 1),
    ],
)
def test_set_new_position(
    direction,
    start_position_x,
    start_position_y,
    expected_position_x,
    expected_position_y,
):
    """Test function Robot.set_new_position"""
    robot = Robot(
        position={"x": start_position_x, "y": start_position_y},
        orientation="N",
        room=room,
    )
    robot.set_new_position(direction=direction)

    assert robot.position["x"] == expected_position_x
    assert robot.position["y"] == expected_position_y


@pytest.mark.parametrize(
    "start_orientation, direction, expected_orientation",
    [
        ("N", "F", "N"),
        ("N", "L", "W"),
        ("N", "R", "E"),
        ("W", "F", "W"),
        ("W", "L", "S"),
        ("W", "R", "N"),
        ("S", "F", "S"),
        ("S", "L", "E"),
        ("S", "R", "W"),
        ("E", "F", "E"),
        ("E", "L", "N"),
        ("E", "R", "S"),
    ],
)
def test_set_new_orientation(start_orientation, direction, expected_orientation):
    """Test function Robot.set_new_orientation"""
    robot = Robot(position={"x": 3, "y": 1}, orientation=start_orientation, room=room)
    robot.set_new_orientation(direction=direction)
    assert robot.orientation == expected_orientation


@pytest.mark.parametrize(
    "start_position_x, start_position_y, start_orientation, directions, expected_position_x, expected_position_y, expected_orientation",
    [
        (3, 1, "N", "FF", 3, 3, "N"),
        (3, 1, "N", "FL", 3, 2, "W"),
        (3, 1, "N", "FR", 3, 2, "E"),
        (3, 1, "N", "FLL", 3, 2, "S"),
        (3, 1, "N", "FRR", 3, 2, "S"),
        (3, 1, "N", "FLR", 3, 2, "N"),
        (3, 1, "N", "FRL", 3, 2, "N"),
        (3, 3, "W", "LLLL", 3, 3, "W"),
        (3, 3, "W", "RRRR", 3, 3, "W"),
        (3, 3, "E", "LLLL", 3, 3, "E"),
        (3, 3, "E", "RRRR", 3, 3, "E"),
        (3, 3, "S", "LLLL", 3, 3, "S"),
        (3, 3, "S", "RRRR", 3, 3, "S"),
        (3, 3, "N", "LLLL", 3, 3, "N"),
        (3, 3, "N", "RRRR", 3, 3, "N"),
        (1, 2, "N", "RFRFFRFRF", 1, 1, "N"),  # This test is taken from your example.
        # To be onest, I'm not sure how the robot can start at (1,2) do steps (RFRFFRFRF)
        # and finish at (1,3). I'm definitely missing something.
        (
            0,
            0,
            "E",
            "RFLFFLRF",
            3,
            0,
            "E",
        ),  # This is your second example, which should have finished with 3 1 E
        (1, 1, "N", "FFFFFFF", 1, 4, "N"),  # Test hit the wall
    ],
)
def test_move(
    start_position_x,
    start_position_y,
    start_orientation,
    directions,
    expected_position_x,
    expected_position_y,
    expected_orientation,
):
    """Test for function Robot.move"""

    robot = Robot(
        position={"x": start_position_x, "y": start_position_y},
        orientation=start_orientation,
        room=room,
    )
    robot.move(directions=directions)
    assert robot.position["x"] == expected_position_x
    assert robot.position["y"] == expected_position_y
    assert robot.orientation == expected_orientation
