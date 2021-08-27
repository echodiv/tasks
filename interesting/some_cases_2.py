import typing as t
from functools import reduce


def cut_lines_int(start: int, end: int, *sublines: t.List[int]) -> int:
    """Задача «Отрезки»
    Есть произвольно задаваемый основной отрезок A-B,
    и есть N — количество произвольно задаваемых дополнительных отрезков.
    Необходимо вычислить длину основного отрезка, на который не происходит
    наложения дополнительных отрезков.

    Пример:
    A=15, B=165 (основной)
    N1 37 — 68
    N2 52 — 74
    N3 118 — 146
    N4 35 — 44
    N5 37 — 65
    N6 46 — 74
    Ответ: 83
    """
    sublines = list(sublines)
    sublines.insert(0, set())
    main_line = set(range(start, end+1))

    return len(main_line - reduce(
        lambda a, b: a.union(set(range(b[0], b[1]+1))),
        sublines
    )) + 1


def cut_lines_with_float(
        start: float, end: float, *sublines: t.List[float]
) -> float:
    """Вариация задачи "Отрезки". Входные данные с плавающей точкой
    """
    sublines = sorted(list(sublines), key=lambda x: (x[0], x[1]))
    active_line = None
    size = end - start

    for line in sublines:
        if not active_line:
            active_line = line
        if line[0] > active_line[1]:
            size -= active_line[1] - active_line[0]
            active_line = line.copy()

        if line[1] > active_line[1] >= line[0] >= active_line[0]:
            active_line[1] = line[1]
    if active_line:
        size -= active_line[1] - active_line[0]

    return round(size, 2)


def byte_sum(this: int, new: int) -> int:
    """Напишите функцию суммирования двух целых чисел без использования
    «+» и других арифметических операторов."""
    if not new:
        return this
    summary = this ^ new
    carry = (this & new) << 1
    return byte_sum(summary, carry)


def intersection_of_many(one: t.List[int], two: t.List[int]) -> t.List[int]:
    """Нужно вернуть пересечение множеств, но с повторением элементов."""
    one = one.copy()
    two = two.copy()
    res = []
    for element in one:
        if element in two:
            two.pop(two.index(element))
            res.append(element)
    return res


def zip_list_of_int(data: t.List[int]) -> str:
    """Дан список целых чисел, повторяющихся элементов в списке нет.
    Нужно преобразовать это множество в строку, сворачивая соседние по
    числовому ряду числа в диапазоны.
    Примеры:
    [1,4,5,2,3,9,8,11,0] => "0-5,8-9,11"
    [1,4,3,2] => "1-4"
    [1,4] => "1,4" """
    pass


def max_line_of_int(data: t.List[int]) -> int:
    """Дан массив из нулей и единиц. Нужно определить, какой максимальный по
    длине подинтервал единиц можно получить, удалив ровно один элемент массива.
    [1, 1, 0] """
    pass


def hotel_max_people(data: t.List[t.Tuple[int]]) -> int:
    """Даны даты заезда и отъезда каждого гостя.
    Для каждого гостя дата заезда строго раньше даты отъезда
    (то есть каждый гость останавливается хотя бы на одну ночь).
    В пределах одного дня считается, что сначала старые гости выезжают,
    а затем въезжают новые. Найти максимальное число постояльцев, которые
    одновременно проживали в гостинице (считаем, что измерение количества
    постояльцев происходит в конце дня).

    sample = [ (1, 2), (1, 3), (2, 4), (2, 3), ]"""
    pass


def group_words_by_liters(data: t.List[str]) -> t.List[t.List[str]]:
    """Сгруппировать слова по общим буквам
    Sample Input ["eat", "tea", "tan", "ate", "nat", "bat"]
    Sample Output [ ["ate", "eat", "tea"], ["nat", "tan"], ["bat"] ]
    """
    pass


def swap_string(one: str, two: str) -> bool:
    """Даны две строки. Написать функцию, которая вернёт True, если из первой
    строки можно получить вторую, совершив не более 1 изменения
    (== удаление / замена символа).
    """
    pass


def get_range_for_target_sum(data: t.List[int], target: int) -> t.List[int]:
    """Дан список интов и число-цель. Нужно найти такой range, чтобы сумма
    его элементов давала число-цель.

    elements = [1, -3, 4, 5]
    target = 9
    result = range(2, 4) # because elements[2] + elements[3] == target"""
    pass


def test_intersection_of_many() -> None:
    res = intersection_of_many([1, 2, 3, 2, 0], [5, 1, 2, 7, 3, 2])
    assert sorted(res) == [1, 2, 2, 3], "res="


def test_simple_cut_lines_int() -> None:
    res = cut_lines_int(
        1, 10, [2, 4]
    )

    assert res == 8, f"{res=}"


def test_byte_sum() -> None:
    res = byte_sum(2, 2)
    assert res == 4, f"{res=}"


def test_byte_sum_with_carry() -> None:
    res = byte_sum(44, 22)
    assert res == 66, f"{res=}"


def test_cut_lines_int() -> None:
    res = cut_lines_int(
        15, 165, [37, 68], [52, 74], [118, 146], [35, 44], [37, 65], [46, 74]
    )

    assert res == 83, f"{res=}"


def test_cut_lines_with_float() -> None:
    res = cut_lines_with_float(
        1.3, 10.3, [2.6, 4.5], [1.5, 4.5], [7.1, 8], [7.5, 8.9]
    )

    assert res == 4.2, f"{res=}"
