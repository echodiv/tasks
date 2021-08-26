import typing as t


def binary_search(sorted_list: t.List[int], to_find: int) -> bool:
    """
    O = log(n)
    """
    low = 0
    high = len(sorted_list) - 1

    while low <= high:
        current = (low + high) // 2
        if to_find == sorted_list[current]:
            return True
        if to_find > current:
            low = current + 1
            continue
        if to_find < current:
            high = current - 1
            continue
    return False


def recursive_binary_search(sorted_list: t.List[int], to_find: int) -> bool:
    index = len(sorted_list) // 2
    if not index:
        return False
    if to_find > sorted_list[index]:
        return recursive_binary_search(sorted_list[index:], to_find)
    elif to_find < sorted_list[index]:
        return recursive_binary_search(sorted_list[:index + 1], to_find)
    elif to_find == sorted_list[index]:
        return True
    return False


def test_recursive_binary_search():
    assert recursive_binary_search([1, 2, 3, 4, 5], 5), 'not found'
    assert not (recursive_binary_search([1, 2, 3, 4, 5], 10)), 'found'


def test_binary_search():
    assert binary_search([1,2,3,4,5], 5), 'not found'
    assert not(binary_search([1,2,3,4,5], 10)), 'found'
