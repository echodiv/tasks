def quick_sort(data: list[int]) -> list[int]:
    if len(data) < 2:
        return data
    index: int = len(data) // 2
    currrent: int = data[index]
    left = [i for i in data[:index]+data[index+1:] if i <= currrent]
    right = [i for i in data[:index]+data[index+1:] if i > currrent]

    return quick_sort(left) + [currrent] + quick_sort(right)


def test():
    assert [1] == quick_sort([1])
    assert [1,2] == quick_sort([1,2])
    assert [5,10,12,22,34,55] == quick_sort([10,22,55,34,12,5])


if __name__ == "__main__":
    test()
