import random

from w95kg.utils import is_digits_length, sum_total


class OfficeKey:
    def __init__(self, key_first=None, key_second=None):
        self.key_first = key_first
        self.key_second = key_second

    @staticmethod
    def check_first(key_part: str) -> bool:
        """Checks the first part of an Office 97 key.

        Requirements:
            - 4 digits long
            - Within 1-9991
            - 4th digit is 3rd digit + 1 or 2

        :param key_part: First part of an Office 97 key.
        :return: Whether the key part is valid or not.
        """
        if not is_digits_length(key_part, 4):
            return False

        key_int = int(key_part)
        if key_int < 1 or key_int > 9991:
            return False

        digit_third = int(key_part[2])
        digit_fourth = int(key_part[3])

        third_plus_1 = (digit_third + 1) % 10
        third_plus_2 = (digit_third + 2) % 10

        return digit_fourth in (third_plus_1, third_plus_2)

    @staticmethod
    def check_second(key_part: str) -> bool:
        """Checks the second part of an Office 97 key.

        Requirements:
            - 7 digits long
            - Last digit is within 1-7
            - Sum of all digits is divisible by 7

        :param key_part: Second part of an OEM key.
        :return: Whether the key part is valid or not.
        """
        if not is_digits_length(key_part, 7):
            return False

        key_int = int(key_part)
        key_last = key_int % 10

        if key_last == 0 or key_last > 7 or sum_total(key_int) % 7 != 0:
            return False

        return True

    @staticmethod
    def generate_first() -> str:
        """Generates the first part of an Office 97 key.

        :return: First part of the key.
        """
        while True:
            key_first = f"{random.randrange(10000):04}"
            if OfficeKey.check_first(key_first):
                return key_first

    @staticmethod
    def generate_second() -> str:
        """Generates the second part of an Office 97 key.

        :return: Second part of the key.
        """
        while True:
            key_second = f"{random.randrange(1000000):07}"
            if OfficeKey.check_second(key_second):
                return key_second

    @classmethod
    def generate(cls) -> str:
        """Generates a valid Office 97 key for use.

        :return: Valid Office 97 key.
        """
        key_first = cls.generate_first()
        key_second = cls.generate_second()
        return f"{key_first}-{key_second}"

    @classmethod
    def validate(cls, key: str) -> bool:
        """Validates an Office 97 key for use.

        :param key: Key to validate.
        :return: Whether the key is valid or not.
        """
        key_split = key.split("-")
        return (
            len(key_split) == 2
            and cls.check_first(key_split[0])
            and cls.check_second(key_split[1])
        )
