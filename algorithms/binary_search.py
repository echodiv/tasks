def binary_search(sorted_list: list[int], to_find: int) -> bool:
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
    return None


def test():
    assert binary_search([1,2,3,4,5], 5), 'not found'
    assert not(binary_search([1,2,3,4,5], 10)), 'found'


if __name__ == '__main__':
    test()
