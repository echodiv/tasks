import typing as t
from functools import reduce


def cut_lines_int(start, end, *sublines):
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


def cut_lines_with_float(start, end, *sublines):
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


def test_simple_cut_lines_int():
    res = cut_lines_int(
        1, 10, [2, 4]
    )

    assert res == 8, f"{res=}"


def test_cut_lines_int():
    res = cut_lines_int(
        15, 165, [37, 68], [52, 74], [118, 146], [35, 44], [37, 65], [46, 74]
    )

    assert res == 83, f"{res=}"


def test_cut_lines_with_float():
    res = cut_lines_with_float(
        1.3, 10.3, [2.6, 4.5], [1.5, 4.5], [7.1, 8], [7.5, 8.9]
    )

    assert res == 4.2, f"{res=}"
