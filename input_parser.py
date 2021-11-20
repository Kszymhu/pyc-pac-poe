"""Holds the InputParser class.
"""

class InputParser:
    """Holds methods for parsing the users' input.
    """

    @staticmethod
    def __is_valid_type(candidate: str, desired_type: type) -> bool:
        """Checks if a string represents a valid member of a desired type.
        """

        try:
            desired_type(candidate)
            return True
        except ValueError:
            return False

    @staticmethod
    def ask_for_int(prompt: str, failed_message: str) -> int:
        """Asks user for a valid integer until either the flesh, or the machine breaks.
        """

        candidate = input(prompt)
        if InputParser.__is_valid_type(candidate, int):
            return int(candidate)

        return InputParser.ask_for_int(prompt, failed_message)

    @staticmethod
    def ask_for_cs_int_pair(prompt: str, failed_message: str) -> list[int]:
        """Asks user for a valid integer pair until either the flesh, or the machine breaks.
        """

        candidate = input(prompt).split(", ")
        if len(candidate) == 2:
            is_first_valid = InputParser.__is_valid_type(candidate[0], int)
            is_second_valid = InputParser.__is_valid_type(candidate[1], int)
            if is_first_valid and is_second_valid:
                return [int(x) for x in candidate]

        print(failed_message)
        return InputParser.ask_for_cs_int_pair(prompt, failed_message)
