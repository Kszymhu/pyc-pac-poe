"""Holds the BoardLogic class.
"""

from board_data import BoardData

class BoardLogic:
    """Holds methods for manipulating the data inside of an object of BoardData.
    """

    @staticmethod
    def is_move_valid(data: BoardData, row: int, column: int) -> bool:
        """Checks if it's possible to insert a character into the given field.
        """
        is_row_invalid = row < 0 or row >= data.get_size()
        is_column_invalid = column < 0 and column >= data.get_size()
        if is_row_invalid or is_column_invalid:
            return False

        is_field_empty = data.get_field(row, column) == " "
        if not is_field_empty:
            return False

        return True

    @staticmethod
    def execute_move(data: BoardData, row: int, column: int, character: str) -> None:
        """Executes a given move.
        """
        data.set_field(row, column, character)

    @staticmethod
    def is_board_full(data: BoardData) -> bool:
        """Checks if there's any empty field left.
        """
        rows_flat = [x for row in data.get_rows() for x in row]
        return rows_flat.count(" ") == 0

    @staticmethod
    def look_for_winner(data: BoardData) -> str:
        """Checks if there's a winner, and returns it. If there isn't any, returns " ".
        """
        for row in data.get_rows():
            if row.count(row[0]) == data.get_size():
                return row[0]

        for column in data.get_columns():
            if column.count(column[0]) == data.get_size():
                return column[0]

        for diagonal in data.get_diagonals():
            if diagonal.count(diagonal[0]) == data.get_size():
                return diagonal[0]

        return " "
