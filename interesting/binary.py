def choose_one(nums) -> int:
    res = nums[0]
    for i in nums[1:]:
        res ^= i
    return res


def test_choose_one():
    assert choose_one([1,1,2,2,3,4,4,5,5]) == 3
