import typing as t

from collections import defaultdict, Counter

def print_without_reapeat():
    prev_data = None
    with open('files/some.txt') as f:
        for i in f:
            if i == prev_data:
                continue
            print(i, end="")
            prev_data = i


def max_unos(unos: t.List) -> int:
    best = 0
    counter: int = 0
    for i in unos:
        if i == 1:
            counter += 1
            best = max(best, counter)
        else:
            counter = 0
    
    return best

def dict_from_str(s):
    d = defaultdict(int)
    for c in s:
        d[c] += 1
    return d

def is_annagram(one: str, two: str) -> bool:
    # return dict_from_str(one) == dict_from_str(two)
    return sorted(list(one)) == sorted(list(two))


def test_is_annagram():
    assert is_annagram("aabbaabb", "aabababb")


def test_max_unos():
    assert max_unos([1,0,0,1,1,1]) is 3
    assert max_unos([]) is 0


if __name__ == "__main__":
    print_without_reapeat()
    
