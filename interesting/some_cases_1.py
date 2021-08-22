"""
TODO:
    1. Напишите метод, находящий максимальное из двух чисел без
    использования if-else или любых других операторов сравнения.
    ---
    2. Опишите, как бы вы использовали один одномерный
    массив для реализации трех стеков.
    ---
    3.Имеется файл размером 20 Гбайт, состоящий из строк.
    Как бы вы выполнили сортировку такого файла?
"""
import typing as t
import copy
import unittest


def swap(a: t.List[int], b: t.List[int]) -> t.Union[t.List[int], t.List[int]]:
    """Напишите функцию, которая переставляет значения
    переменных без использования временных переменных и a,b = b,a."""
    a[0] = a[0] - b[0]
    b[0] = b[0] + a[0]
    a[0] = b[0] - a[0]


def is_all_symbols_are_unique(string: str) -> bool:
    """Реализуйте алгоритм, определяющий, все ли символы в строке встречаются
    только один раз. А если при этом запрещено использование
    дополнительных структур данных?"""
    for symbol in string:
        if string.count(symbol) > 1:
            return False
    return True


def swap_lines_and_tables_to_zeros(table: t.List[t.List[int]]) -> None:
    """Напишите алгоритм, реализующий следующее условие: если элемент
    матрицы MxN равен 0, то весь столбец и вся строка обнуляются."""
    indexes = [
        set(), set()
    ]
    x, y = len(table[0]), len(table)

    for i, line in enumerate(table):
        if 0 in line:
            indexes[0].add(i)
        [indexes[1].add(x[0]) for x in enumerate(line) if not x[1]]

    if len(indexes[0]) == y or len(indexes[1]) == x:
        table.clear()
        table.append([[0 for _ in range(x)] for _ in range(y)])
        return None

    for i, line in enumerate(table):
        if i in indexes[0]:
            table.pop(i)
            table.insert(i, [0 for _ in range(x)])
            continue
        for j, element in enumerate(line):
            if j in indexes[1]:
                line.pop(j)
                line.insert(j, 0)


def zip_string(string: str) -> str:
    """Реализуйте метод для выполнения простейшего сжатия строк с
     использованием счетчика повторяющихся символов. Например, строка
     ааbсссссааа превращается в а2b1с5а3. Если сжатая строка не становится
     короче исходной, то метод возвращает исходную строку. Предполагается, что
     строка состоит только из букв верхнего и нижнего регистра (a-z)."""
    counter = 0
    prev = ""
    res = ""
    for symbol in string:
        if symbol == prev:
            counter += 1
        else:
            prev = symbol
            res += str(counter) if counter else ""
            res += symbol
            counter = 1
    else:
        res += str(counter) if counter else ""

    return res


def delete_repeated_data(data: t.List) -> None:
    """Напишите код для удаления дубликатов из несортированного
    связного списка."""
    for element in data:
        if data.count(element) > 1:
            for i in range(data.count(element) - 1):
                data.pop(data.index(data.index(element)+1, element))


def x_o_check_result(data: t.List[t.List[int]]) -> int:
    """Разработайте алгоритм, проверяющий результат игры в
    крестики-нолики (3х3). 1 - игрок 1, 2 - игрок 2"""
    zero_result = {
        "column": [0, 0, 0],
        "d_one": 0,
        "d_two": 0,
    }
    for player in [1, 2]:
        result = copy.deepcopy(zero_result)

        for i, line in enumerate(data):
            if line.count(player) == 3:
                return player

            if data[i][i] == player:
                result['d_one'] += 1

            if data[2-i][2-i] == player:
                result['d_two'] += 1

            for j, point in enumerate(line):
                if point == player:
                    result['column'][j] += 1

                if result['column'][j] == 3:
                    return player

        if result['d_one'] == 3 or result['d_two'] == 3:
            return player
    return 0


def robot_move(field: t.List[t.List[int]]) -> str:
    """Робот стоит в левом верхнем углу сетки, состоящей из r строк и k
    столбцов. Робот может перемещаться в двух направлениях: вправо и вниз,
    но некоторые ячейки сетки заблокированы, то есть робот через них проходить
    не может. Разработайте алгоритм построения маршрута от левого верхнего
    до правого нижнего угла.
    input:
    [[0, 1, 0, 0],
     [0, 0, 0, 0],
     [0, 0, 1, 0],
     [1, 0, 1, 0],
     [0, 1, 1, 0]]
    где 0 - поле доступное для робота
        1 - поле недоступное для робота
    """
    def is_free(x, y, field):
        return not bool(field[y][x])

    def get_path(
            x: int,
            y: int,
            field: t.List[t.List[int]],
            path: t.List[t.List[int]]
    ) -> t.List[t.List[int]]:
        path.append([x, y])
        if not x and not y:
            return True, path

        success = False
        if x >= 1 and is_free(x-1, y, field):
            success, path = get_path(x-1, y, field, path)
        if not success and y >= 1 and is_free(x, y-1, field):
            success, path = get_path(x, y-1, field, path)
        if not success:
            path.pop(-1)
        return success, path

    y = len(field) - 1
    x = len(field[0]) - 1
    return get_path(x, y, field, [])


def fizz_bazz_print(length: int, rules: t.List[t.Dict]) -> None:
    """Напишите программу, которая выводит на экран числа от 1 до 100.
    При этом вместо чисел, кратных трем, программа должна
    выводить слово «Fizz», а вместо чисел, кратных пяти — слово «Buzz».
    Если число кратно и 3, и 5, то программа должна выводить слово
    «FizzBuzz»."""
    rules = copy.deepcopy(rules)
    length += 1 if length else length
    for i in range(1, length):
        for rule in rules:
            if all(not i % index for index in rule['indexes']):
                print(rule['text'])
                break
        else:
            print(i)


@unittest.skip("Just print")
def test_fizz_bazz_print():
    data = [
        {
            "indexes": [3, 5], "text": "FizzBuzz"
        },
        {
            "indexes": [3], "text": "Fizz"
        },
        {
            "indexes": [5], "text": "Buzz"
        },
    ]
    fizz_bazz_print(100, data)


def test_robot_move():
    data = [
        [0, 1, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 1, 0],
        [1, 0, 1, 0],
        [0, 1, 0, 0]
    ]
    res_path = [[3, 4], [3, 3], [3, 2], [3, 1], [2, 1], [1, 1], [0, 1], [0, 0]]
    success, res = robot_move(data)
    assert success and res == res_path


def test_swap_function():
    a = [4]
    b = [5]
    swap(a, b)
    assert a[0] == 5 and b[0] == 4


def test_is_all_symbols_are_unique_with_true():
    string = "abcd"
    assert is_all_symbols_are_unique(string)


def test_is_all_symbols_are_unique_with_false():
    string = "abcda"
    assert not is_all_symbols_are_unique(string)


def test_swap_lines_and_tables_to_zeros():
    table = [
        [1, 1, 1, 0],
        [1, 0, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 0],
    ]
    result = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [1, 0, 1, 0],
        [0, 0, 0, 0],
    ]
    swap_lines_and_tables_to_zeros(table)
    assert result == table


def test_zip_string():
    string = "aaabbcac"
    res = zip_string(string)
    assert res == "a3b2c1a1c1"


def test_delete_repeated_data():
    data = [1, 2, 1, 4, 3, 2, 1, 2]
    exp_res = [1, 2, 4, 3]

    delete_repeated_data(data)
    assert data == exp_res


def test_x_o_check_result_column():
    data = [
        [0, 1, 0],
        [2, 1, 2],
        [0, 1, 2],
    ]
    res = x_o_check_result(data)
    assert res == 1


def test_x_o_check_result_diagonally():
    data = [
        [2, 1, 0],
        [2, 2, 1],
        [0, 1, 2],
    ]
    res = x_o_check_result(data)
    assert res == 2


def test_x_o_check_result_line():
    data = [
        [1, 1, 1],
        [2, 2, 0],
        [0, 1, 2],
    ]
    res = x_o_check_result(data)
    assert res == 1


def test_x_o_check_result_no_winner():
    data = [
        [1, 1, 0],
        [2, 2, 0],
        [0, 1, 1],
    ]
    res = x_o_check_result(data)
    assert res == 0
