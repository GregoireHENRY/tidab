"""
tidab
AI Tower Defense Battle

Blue is left side, red is right side.
"""

import math
import random
import sys
from typing import List, Tuple

from pudb import set_trace as bp  # pylint: disable=unused-import

SIDE_WIDTH = 20
BORDER_THICKNESS = 1
SPAWN_WIDTH = 1
MIDDLE_WIDTH = 3
MIDDLE_POSITION_X = SIDE_WIDTH + math.ceil(MIDDLE_WIDTH / 2)
WIDTH = BORDER_THICKNESS + SIDE_WIDTH + MIDDLE_WIDTH + SIDE_WIDTH + BORDER_THICKNESS
HEIGHT = 10
X_BORDERS = (
    0,
    SPAWN_WIDTH + BORDER_THICKNESS,
    MIDDLE_POSITION_X,
    WIDTH - 1 - SPAWN_WIDTH - BORDER_THICKNESS,
    WIDTH - 1,
)
Y_BORDERS = (0, HEIGHT - 1)
SPAWN_AREA = (1, HEIGHT - 2)
BLUE_SPAWN_POSITION_X = MIDDLE_POSITION_X - 1
RED_SPAWN_POSITION_X = MIDDLE_POSITION_X + 1
EMPTY_CHAR = " "
BORDER_CHAR = "#"
UNIT_CHAR = "*"


def start() -> None:
    """tidab"""

    # setup field if x or y iterator meet a border condition (outside limits, spawn, middle)
    field = [
        [BORDER_CHAR if (x in X_BORDERS or y in Y_BORDERS) else EMPTY_CHAR for x in range(WIDTH)]
        for y in range(HEIGHT)
    ]
    BLUE_SPAWN_POSITION_Y = random.randint(*SPAWN_AREA)
    RED_SPAWN_POSITION_Y = random.randint(*SPAWN_AREA)

    blue_position_x = BLUE_SPAWN_POSITION_X
    red_position_x = RED_SPAWN_POSITION_X
    blue_position_y = BLUE_SPAWN_POSITION_Y
    red_position_y = RED_SPAWN_POSITION_Y

    while True:
        # aove units toward bases
        new_blue_position_x, new_blue_position_y = simple_pathfinding(
            field, blue_position_x, blue_position_y, 0
        )
        new_red_position_x, new_red_position_y = simple_pathfinding(
            field, red_position_x, red_position_y, 1
        )

        # apply new position changes
        field[new_blue_position_y][new_blue_position_x] = UNIT_CHAR
        field[new_red_position_y][new_red_position_x] = UNIT_CHAR

        # redraw previous cell state
        field[blue_position_y][blue_position_x] = EMPTY_CHAR
        field[red_position_y][red_position_x] = EMPTY_CHAR

        # draw field
        for line in field:
            print("".join(line))

        # save new position for next turn
        blue_position_x, blue_position_y = new_blue_position_x, new_blue_position_y
        red_position_x, red_position_y = new_red_position_x, new_red_position_y

        # wait user to press Enter to go next frame
        if "pytest" in sys.modules:
            break
        input()


def simple_pathfinding(
    _field: List[List[str]], position_x: int, position_y: int, side_target: int
) -> Tuple[int, int]:
    """
    Implement a simple pathfinding before implementing A* algo.
    From the field state, current position and targeted side, decide next position.
    If target is blue, side_target is 0, else if it is red, side_target is 1.
    """
    SIDE_SIGN = -1 + side_target * 2
    _X_OBJECTIVE = side_target * WIDTH
    position_x += SIDE_SIGN
    return position_x, position_y
