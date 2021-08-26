import typing as t


def bubble_sort(data: t.List[int]) -> t.List[int]:
    data = data.copy()
    for i in range(len(data)):
        for j in range(len(data)):
            if data[i] < data[j]:
                data[i], data[j] = data[j], data[i]
    return data


def test_bubble_sort() -> None:
    data = [4, 3, 7, 5, 1, 2]
    assert bubble_sort(data) == [1, 2, 3, 4, 5, 7]


def test_bubble_sort_with_sorted() -> None:
    data = [1, 2, 3]
    assert bubble_sort(data) == [1, 2, 3]


def test_bubble_sort_with_reverse_sorted_data() -> None:
    data = [3, 2, 1]
    assert bubble_sort(data) == [1, 2, 3]
