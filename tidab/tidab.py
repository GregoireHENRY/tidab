"""
tidab
AI Tower Defense Battle

Blue is left side, red is right side.
"""

import math
import random

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

    # Setup field if x or y iterator meet a border condition (outside limits, spawn, middle)
    field = [
        [BORDER_CHAR if (x in X_BORDERS or y in Y_BORDERS) else EMPTY_CHAR for x in range(WIDTH)]
        for y in range(HEIGHT)
    ]
    BLUE_RANDOM_SPAWN_POSITION_Y = random.randint(*SPAWN_AREA)
    RED_RANDOM_SPAWN_POSITION_Y = random.randint(*SPAWN_AREA)

    field[BLUE_RANDOM_SPAWN_POSITION_Y][BLUE_SPAWN_POSITION_X] = UNIT_CHAR
    field[RED_RANDOM_SPAWN_POSITION_Y][RED_SPAWN_POSITION_X] = UNIT_CHAR

    # Draw field
    for line in field:
        print("".join(line))
