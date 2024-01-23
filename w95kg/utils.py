def sum_total(n: str | int) -> int:
    """Sum all digits in a integer or string.

    :param n: Number to sum.
    :return: Summed value.
    """
    if isinstance(n, int):
        n = str(n)
    return sum(int(x) for x in str(n))


def is_digits_length(key: str, length: int):
    """Check for a specific key length as well as if the key is all digits.

    :param key: Key to check.
    :param length: Length to check for.
    :return: Whether the key length and desired length matches or not.
    """
    return len(key) == length and key.isdigit()
