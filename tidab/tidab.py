"""
tidab
"""

from pudb import set_trace as bp  # pylint: disable=unused-import

SIDE_WIDTH = 20
BORDER_THICKNESS = 1
SPAWN_WIDTH = 1
WIDTH = BORDER_THICKNESS + SIDE_WIDTH + BORDER_THICKNESS + SIDE_WIDTH + BORDER_THICKNESS
HEIGHT = 10
X_BORDERS = (
    0,
    SPAWN_WIDTH + BORDER_THICKNESS,
    SIDE_WIDTH + BORDER_THICKNESS,
    WIDTH - 1 - SPAWN_WIDTH - BORDER_THICKNESS,
    WIDTH - 1,
)
Y_BORDERS = (0, HEIGHT - 1)
BORDER_CHAR = "#"
EMPTY_CHAR = " "


def start() -> None:
    """tidab"""

    # Setup field if x or y iterator meet a border condition (outside limits, spawn, middle)
    field = [
        [BORDER_CHAR if (x in X_BORDERS or y in Y_BORDERS) else EMPTY_CHAR for x in range(WIDTH)]
        for y in range(HEIGHT)
    ]

    # Draw field
    for line in field:
        print("".join(line))
