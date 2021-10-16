import re


def is_poly_str(s: str):
    s = re.sub("[^a-zA-Z0-9]", "", s).lower()
    return s == s[::-1]


def convert_to_title(column_number: int) -> str:
    if not column_number:
        return ""
    column_number, m = divmod(column_number - 1, 26)
    return convert_to_title(column_number) + chr(ord("A") + m)


def convert_to_decimal(columnTitle):
    l = len(columnTitle) - 1
    res = 0
    for i, char in enumerate(columnTitle):
        res += (26 ** (l - i)) * (ord(char) - ord("A") + 1)
    return res


def reverse_bits(n: int) -> int:
    return int(bin(n)[2:].zfill(32)[::-1], 2)


def test_reverse_bits():
    assert reverse_bits(43261596) == 964176192


def test_convert_to_decimal():
    assert convert_to_decimal("A") == 1
    assert convert_to_decimal("AA") == 27
    assert convert_to_decimal("AZ") == 52


def test_convert_to_title():
    assert convert_to_title(1) == "A"
    assert convert_to_title(27) == "AA"
    assert convert_to_title(52) == "AZ"


def test_is_poly_str():
    assert is_poly_str("A man, a plan, a canal: Panama")
    assert not is_poly_str("0P")
    assert is_poly_str("  ")
