"""
Generation and validation of retail keys.

Example: `185-0912225`
"""

import random

from .oem import OEMKey
from helpers import is_digits_length

REJECTED_FIRST: list[str] = ["333", "444", "555", "666", "777", "888", "999"]


class RetailKey:
    def __init__(self, key_first=None, key_second=None) -> None:
        """
        :param key_first: First part of the key
        :param key_second: Second part of the key
        """

        self.key_first = key_first
        self.key_second = key_second

    @staticmethod
    def check_first(key_part: str) -> bool:
        """
        Checks the first part of a retail key.

        Requirements:
            - 3 digits long
            - Not in `REJECTED_FIRST`

        :param key_part: First part of a retail key
        :return: Whether the key part is valid or not
        """

        if not is_digits_length(key_part, 3) or key_part in REJECTED_FIRST:
            return False

        return True

    @staticmethod
    def check_second(key_part: str) -> bool:
        """
        Checks the second part of a retail key.

        Requirements:
            - 7 digits long
            - Last digit is within 1-7
            - Sum of all digits is divisible by 7

        :param key_part: Second part of a retail key
        :return: Whether the key part is valid or not
        """

        return OEMKey.check_second(key_part)

    @staticmethod
    def generate_first() -> str:
        """
        Generates the first part of a retail 97 key.

        Example: `832`

        :return: First part of the key
        """

        while True:
            key_first = f"{random.randrange(1000):03}"
            if RetailKey.check_first(key_first):
                return key_first

    @staticmethod
    def generate_second() -> str:
        """
        Generates the second part of a retail 97 key.

        Example: `0264952`

        :return: Second part of the key
        """

        while True:
            key_second = f"{random.randrange(1000000):07}"
            if RetailKey.check_second(key_second):
                return key_second

    @classmethod
    def generate(cls) -> str:
        """
        Generates a valid retail key for use.

        :return: Valid retail key
        """

        key_first = cls.generate_first()
        key_second = cls.generate_second()
        return f"{key_first}-{key_second}"

    @classmethod
    def validate(cls, key: str) -> bool:
        """
        Validates a retail key for use.

        :param key: Key to validate
        :return: Whether the key is valid or not
        """

        key_split = key.split("-")
        return len(key_split) == 2 and cls.check_first(key_split[0]) and cls.check_second(key_split[1])
