import random

from w95kg.utils import is_digits_length, sum_total


class OEMKey:
    VALID_YEARS = ["95", "96", "97", "98", "99", "00", "01", "02", "03"]

    def __init__(
        self, key_first=None, key_second=None, key_third=None
    ) -> None:
        self.key_first = key_first
        self.key_second = key_second
        self.key_third = key_third

    @staticmethod
    def check_first(key_part: str) -> bool:
        """Checks the first part of an OEM key.

        Requirements:
            - 5 digit long
            - First 3 digits are within 000-366
            - Last 2 digits are inside of `VALID_YEARS`

        :param key_part: First part of an OEM key
        :return: Whether the key part is valid or not
        """
        if not is_digits_length(key_part, 5):
            return False

        key_day = int(key_part[:3])
        key_year = key_part[-3:]

        if key_day < 0 or key_day > 366:
            return False
        if key_year in OEMKey.VALID_YEARS:
            return False

        return True

    @staticmethod
    def check_second(key_part: str) -> bool:
        """Checks the second part of an OEM key.

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
    def check_third(key_part: str) -> bool:
        """Checks the third part of an OEM key.

        Requirements:
            - 5 digits long

        :param key_part: Third part of an OEM key.
        :return: Whether the key part is valid or not.
        """
        return is_digits_length(key_part, 5)

    @staticmethod
    def generate_first() -> str:
        """Generates the first part of an OEM key.

        :return: First part of the key.
        """
        rand_day = f"{random.randrange(367):03}"
        rand_year = random.choice(OEMKey.VALID_YEARS)
        return rand_day + rand_year

    @staticmethod
    def generate_second() -> str:
        """Generates the second part of an OEM key.

        :return: Second part of the key.
        """
        while True:
            key_second = f"{random.randrange(1000000):07}"
            if OEMKey.check_second(key_second):
                return key_second

    @staticmethod
    def generate_third() -> str:
        """Generates the third part of an OEM key.

        :return: Third part of the key.
        """
        return f"{random.randrange(100000):05}"

    @classmethod
    def generate(cls) -> str:
        """Generates a valid OEM key for use.

        :return: Valid OEM key.
        """
        key_first = cls.generate_first()
        key_second = cls.generate_second()
        key_third = cls.generate_third()
        return f"{key_first}-OEM-{key_second}-{key_third}"

    @classmethod
    def validate(cls, key: str) -> bool:
        """Validates an OEM key for use.

        :param key: Key to validate.
        :return: Whether the key is valid or not.
        """
        key_split = key.split("-")
        return (
            len(key_split) == 4
            and cls.check_first(key_split[0])
            and cls.check_second(key_split[2])
            and cls.check_third(key_split[3])
        )
