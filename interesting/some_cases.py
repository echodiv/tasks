"""
TODO:
    1. Напишите метод, находящий максимальное из двух чисел без
    использования if-else или любых других операторов сравнения.
    ---
    2. Опишите, как бы вы использовали один одномерный
    массив для реализации трех стеков.

"""
import typing as t
import copy


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
