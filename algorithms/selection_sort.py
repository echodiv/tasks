from copy import copy


def minimum(unsorted_list: list[int]) -> int:
    min_value = unsorted_list[0]
    min_id = 0
    for element_id, value in enumerate(unsorted_list):
        if value < min_value:
            min_value = value
            min_id = element_id
    return min_id


def selection_sort(unsorted_list: list[int]) -> list[int]:
    sorted_list = []
    unsorted_list = copy(unsorted_list)
    for element in range(len(unsorted_list)):
        sorted_list.append(unsorted_list.pop(minimum(unsorted_list)))
    
    return sorted_list


def test():
    assert [1,2,3] == selection_sort([3,2,1])
    assert [0,0,12] == selection_sort([0,12,0])


if __name__ == '__main__':
    test()
