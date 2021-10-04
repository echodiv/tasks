from typing import ItemsView


import typing as t

from collections import deque


def search(data: t.Dict, target: str) -> bool:
    """Поиск в ширину
    Ищем волнами,
    при первом совпадении выдаём истину,
    избегаем рекурсии
    """
    search_quie = deque()
    search_quie += data["start"]
    searched = []
    while search_quie:
        current = search_quie.popleft()
        if current in searched:
            continue

        if current == target:
            return True
        else:
            search_quie += data[current]
            searched.append(current)
    return False


def test_search():
    data = {
        "start": ["one", "two"],
        "one": ["one_1", "two_1"],
        "two": ["one_2", "two_2"],
        "one_1": [],
        "one_2": [],
        "two_1": [],
        "two_2": ["target"],
        "target": ["start"],
    }
    assert search(data, "target"), "Invalid result"
    assert not search(data, "not found"), "Invalid result"
