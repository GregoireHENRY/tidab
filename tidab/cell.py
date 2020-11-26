"""
Cell module
"""

from enum import Enum


class CellState(Enum):
    """All different possible states for a cell."""

    EMPTY = " "
    BORDER = "#"
    UNIT = "*"


class Cell:
    """Cell"""

    def __init__(self, state: CellState):
        self.state = state
        self.previous_state = CellState.EMPTY

    def __repr__(self) -> str:
        return self.__str__()

    def __str__(self) -> str:
        return self.state.value

    def change_state(self, new_state: CellState):
        """Change state of the cell and keep in memory the previous state."""
        self.previous_state = self.state
        self.state = new_state

    def revert(self):
        """Revert the previous state of a cell."""
        self.state = self.previous_state
        self.previous_state = CellState.EMPTY
