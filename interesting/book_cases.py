from typing import List
from collections import deque


def island_perimeter(grid: List[List[int]]) -> int:
    edges = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                edges += 4
                if i > 0 and grid[i - 1][j] == 1:
                    edges -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    edges -= 2
    return edges


def two_sum(nums, target):
    for i in range(len(nums)):
        current = target - nums[i]
        if current in nums:
            if nums.index(current) != i:
                return [i, nums.index(current)]
            elif nums.count(current) > 1:
                return [i, nums[i + 1 :].index(current) + i + 1]


def reverse(x: int) -> int:
    if -2147483648 > x or x > 2147483647:
        return 0
    plus = 1 if x > 0 else -1
    res = plus * int(str(abs(x))[::-1])
    if -2147483648 > res or res > 2147483647:
        return 0
    return res


def is_polyndrom(x) -> bool:
    if x < 0:
        return False
    if str(x) == str(x)[::-1]:
        return True
    return False


def rome_to_num(s):
    p = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    res = 0
    for i, n in enumerate(s):
        if i < len(s) - 1 and p[n] < p[s[i + 1]]:
            res -= p[n]
        else:
            res += p[n]

    return res


def max_strs_prefix(strs):
    pref = ""
    for i in range(len(strs[0]) + 1):
        for j in strs:
            if not j.startswith(pref):
                return pref[:-1]
        if i < len(strs[0]):
            pref = strs[0][: i + 1]
    return pref


def brackets_validator(s):
    stack = deque()
    p = {
        "(": ")",
        "[": "]",
        "{": "}",
    }
    for i in s:
        if i in ("(", "{", "["):
            stack.append(i)
        elif not stack or not p[stack.pop()] == i:
            return False

    return not stack


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_list_node(l1, l2):
    """
    Скрлеиваем листы через буфер
    Выходим когда один из листов закончится
    Возвращаем всё кроме начала буфера
    """
    dummy_node = ListNode(0)
    tail = dummy_node

    while True:
        if l1 is None:
            tail.next = l2
            break
        if l2 is None:
            tail.next = l1
            break

        if l1.val <= l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next

        tail = tail.next

    return dummy_node.next


def remove_duplicate_in_list(head):
    tail = head

    while tail:
        if tail.next and tail.val == tail.next.val:
            tail.next = tail.next.next
        else:
            tail = tail.next
    return head


def remove_duplicated_nums(nums):
    l = len(nums)
    for i in nums:
        if nums.count(i) > 1:
            for _ in range(nums.count(i) - 1):
                nums.pop(nums.index(i, nums.index(i)))
    l2 = len(nums)
    _ = [nums.append("_") for _ in range(l - len(nums))]
    return l2


def substring_id(haystack: str, needle: str) -> int:
    if needle not in haystack:
        return -1
    return haystack.index(needle)


def where_is_int(nums, target):
    i = 0
    while i < len(nums):
        if nums[i] == target or nums[i] > target:
            return i
        i += 1
    return i


def max_sum(nums):
    dp = [0 for _ in nums]
    dp[0] = nums[0]
    for i in range(1, len(nums)):
        if dp[i - 1] + nums[i] < nums[i]:
            dp[i] = nums[i]
        else:
            dp[i] = dp[i - 1] + nums[i]

    return max(dp)


def max_len_of_last_world(s):
    return len(s.split()[-1])


def custom_increment(digits):
    digits = int("".join(map(str, digits))) + 1
    return [int(i) for i in str(digits)]


def binary_sum(a: str, b: str):
    a = int(a, 2)
    b = int(b, 2)
    return bin(a + b)[2:]


def factorial(x, mem={1: 1, 2: 1, 3: 2}):
    if x in mem:
        return mem[x]

    mem[x] = factorial(x - 1) + factorial(x - 2)
    return mem[x]


def merge_two_list(nums1, m, nums2, n) -> None:
    """%-)"""
    cache = nums1[:m]
    nums2 = nums2[:n]
    res = sorted(cache + nums2)
    for _ in range(len(nums1)):
        nums1.pop()
    for i in res:
        nums1.append(i)


def go_to_binray(root):
    if not root:
        return []
    if not root.left and not root.right:
        return [root.val]
    res = []
    stack = [(root, None)]
    while stack:
        node, visited = stack.pop()
        if visited:
            res.append(node.val)
        else:
            if node.right:
                stack.append((node.right, False))
            stack.append((node, True))
            if node.left:
                stack.append((node.left, False))
    return res


def is_trees_equeal(p, q):
    if not p and not q:
        return True
    if not p or not q:
        return False
    if p.val != q.val:
        return False

    return is_trees_equeal(p.left, q.left) and is_trees_equeal(p.right, q.right)


def test_merge_two_list():
    l1 = [0]
    merge_two_list(l1, 0, [1], 1)
    assert l1 == [1]


def test_factorial():
    assert factorial(1) == 1
    assert factorial(2) == 1
    assert factorial(3) == 2
    assert factorial(4) == 3
    assert factorial(6) == 8


def test_binary_sum():
    assert binary_sum("100", "1") == "101"


def test_custom_increment():
    assert custom_increment([1, 2, 3]) == [1, 2, 4]
    assert custom_increment([9]) == [1, 0]


def test_max_len_of_last_world():
    assert max_len_of_last_world("My name in Joshua") == 6


def test_max_sum():
    assert max_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert max_sum([5, 4, -1, 7, 8]) == 23
    assert max_sum([1, 2, -3, 1, 2, 3]) == 6
    assert max_sum([1, 3, -5, -1, 2, 3]) == 5


def test_where_is_int():
    assert where_is_int([1, 2, 3], 4) == 3
    assert where_is_int([1, 3, 4], 2) == 1
    assert where_is_int([1], 1) == 0
    assert where_is_int([1, 2, 3, 4, 5], 3) == 2


def test_substring_id():
    assert substring_id("hello", "ll") == 2
    assert substring_id("", "") == 0
    assert substring_id("a", "ss") == -1


def test_remove_duplicated_nums():
    n0 = [1, 1, 1, 1]
    assert remove_duplicated_nums(n0) == 1
    assert n0 == [1, "_", "_", "_"]
    n1 = [1, 1, 2]
    assert remove_duplicated_nums(n1) == 2
    assert n1 == [1, 2, "_"]
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    assert remove_duplicated_nums(nums) == 5
    assert nums == [
        0,
        1,
        2,
        3,
        4,
        "_",
        "_",
        "_",
        "_",
        "_",
    ]


def test_merge_list():
    # assert([1,2,4], [1,3,4]) == [1,1,2,3,4,4]
    # a = ListNode(0)
    # b = ListNode(1, a)
    # c = ListNode(2, b)
    print


def test_brackets_validator():
    assert brackets_validator("()")
    assert brackets_validator("()[]{}")
    assert brackets_validator("(([]{})[]{})")
    assert not brackets_validator(")")
    assert not brackets_validator("(")
    assert not brackets_validator("{{}()}[")


def test_max_strs_prefix():
    assert max_strs_prefix(["dog", "racecar", "car"]) == ""
    assert max_strs_prefix(["flower", "flow", "flight"]) == "fl"
    assert max_strs_prefix(["a"]) == "a"
    assert max_strs_prefix(["a", "ab"]) == "a"
    assert max_strs_prefix(["ab", "a"]) == "a"


def test_rome_one():
    assert rome_to_num("VI") == 6
    assert rome_to_num("III") == 3
    assert rome_to_num("V") == 5
    assert rome_to_num("MCMXCIV") == 1994


def test_is_poly():
    assert is_polyndrom(12321)
    assert not is_polyndrom(1232)
    assert not is_polyndrom(-11)


def test_reverse():
    assert reverse(123) == 321
    assert reverse(9646324351) == 0
    assert reverse(1534236469) == 0

    assert reverse(-2147483412) == -2143847412


def test_two_sum():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([2, 2], 4) == [0, 1]
    assert two_sum([0, 0, 0, 2, 2], 4) == [3, 4]


def test_case_0():
    assert (
        island_perimeter([[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]) == 16
    )

    assert island_perimeter([[1]]) == 4

    assert island_perimeter([[1, 1]]) == 6
