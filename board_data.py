"""Holds the BoardData class.
"""


class BoardData:
    """Holds data about the game board, and methods for accessing it.
    """

    def __init__(self, size: int) -> None:
        self.__size = size
        row = [" " for _ in range(self.get_size())]
        self.__rows = [row.copy() for _ in range(self.get_size())]

    def get_size(self) -> int:
        """Returns the size of the board.
        """
        return self.__size

    def get_rows(self) -> list[list[str]]:
        """Returns a list of rows.
        """
        return self.__rows

    def get_field(self, row: int, column: int) -> str:
        """Returns the value from given row and column.
        """
        return self.get_rows()[row][column]

    def get_columns(self) -> list[list[str]]:
        """Returns a list of columns.
        """

        columns = []
        for column_index in range(self.get_size()):
            column = []
            for row_index in range(self.get_size()):
                column.append(self.get_field(row_index, column_index))
            columns.append(column)
        return columns

    def get_diagonals(self) -> list[list[str]]:
        """Returns a list of diagonals.
        """

        diagonals = [[], [], [], []]
        last_index = self.get_size() - 1
        for index in range(self.get_size()):
            diagonals[0].append(self.get_field(index, index))
            diagonals[1].append(self.get_field(last_index - index, index))
            diagonals[2].append(self.get_field(index, last_index - index))
            diagonals[3].append(self.get_field(last_index - index, last_index - index))
        return diagonals

    def set_field(self, row: int, column: int, value: str) -> None:
        """Changes the value of at given row and column.
        """

        self.__rows[row][column] = value
