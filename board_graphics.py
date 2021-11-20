"""Holds the BoardGraphics class.
"""

from board_data import BoardData


class BoardChars:
    """Holds constants with unicode characters needed to draw the board.
    """
    HORIZONTAL_LINE     = "\u2500"
    VERTICAL_LINE       = "\u2502"
    UPPER_LEFT_CORNER   = "\u250C"
    UPPER_RIGHT_CORNER  = "\u2510"
    LOWER_LEFT_CORNER   = "\u2514"
    LOWER_RIGHT_CORNER  = "\u2518"
    RIGHT_JUNCTION      = "\u251C"
    LEFT_JUNCTION       = "\u2524"
    DOWN_JUNCTION       = "\u252C"
    UP_JUNCTION         = "\u2534"
    JUNCTION            = "\u253C"


class BoardGraphics:
    """Holds methods for displaying the game board from an object of board_data.
    """

    @staticmethod
    def __construct_column_number_line(data: BoardData) -> str:
        """Constructs a line containing numbers of columns.
        """

        max_digits = len(str(data.get_size() + 1))
        indent = " " * (max_digits + 1)

        numbers = list(range(1, data.get_size() + 1))

        line = indent + "".join(["  " + str(x) + " " for x in numbers])

        return line

    @classmethod
    def __construct_field_line(
            cls,
            fields: list[str],
            number: int,
            max_digits: int) -> str:

        """Constructs a line containing given values,
        separated by vertical lines.
        """

        padded_fields = [" " + x + " " for x in fields]

        digits = len(str(number))
        indent = " " * (max_digits - digits + 1)

        line = (indent
                + str(number)
                + BoardChars.VERTICAL_LINE
                + BoardChars.VERTICAL_LINE.join(padded_fields)
                + BoardChars.VERTICAL_LINE)

        return line

    @staticmethod
    def __construct_separator_line(
            data: BoardData,
            max_digits: int,
            junction: str,
            start: str,
            end: str) -> str:

        """Constructs a line of horizontal lines and junctions.
        """

        separator_list = [BoardChars.HORIZONTAL_LINE * 3 for _ in range(data.get_size())]

        indent = " " * (max_digits + 1)
        line = indent + start + junction.join(separator_list) + end

        return line

    @classmethod
    def __construct_lines(cls, data: BoardData) -> list[str]:
        """Constructs a list of lines based on data from the given BoardData object.
        """

        line_count = 2 * data.get_size() + 1

        lines = [cls.__construct_column_number_line(data)]

        field_line_counter = 0

        for i in range(line_count):
            line: str

            if i % 2 == 0: # separator line
                junction = BoardChars.JUNCTION
                start = BoardChars.RIGHT_JUNCTION
                end = BoardChars.LEFT_JUNCTION

                if i == 0: # topmost line
                    junction = BoardChars.DOWN_JUNCTION
                    start = BoardChars.UPPER_LEFT_CORNER
                    end = BoardChars.UPPER_RIGHT_CORNER

                elif i == line_count - 1: # bottommost line
                    junction = BoardChars.UP_JUNCTION
                    start = BoardChars.LOWER_LEFT_CORNER
                    end = BoardChars.LOWER_RIGHT_CORNER

                line = cls.__construct_separator_line(
                    data,
                    len(str(data.get_size())),
                    junction,
                    start,
                    end)

            else: #field line
                line = cls.__construct_field_line(
                    data.get_rows()[field_line_counter],
                    field_line_counter + 1,
                    len(str(data.get_size())))

                field_line_counter += 1

            lines.append(line)
        return lines

    @classmethod
    def print(cls, data: BoardData) -> None:
        """Creates lines from given board data, and prints them.
        """
        lines = cls.__construct_lines(data)
        print("\n".join(lines))
