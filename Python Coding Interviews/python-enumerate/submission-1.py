from typing import List


def get_index_of_seven(nums: List[int]) -> int:
    _index, flag = 0, 0
    if 7 not in nums:
        return -1
    else:
        for _id, _value in enumerate(nums):
            if _value == 7 and flag == 0:
                _index = _id
                flag += 1
        return _index

def get_dist_between_sevens(nums: List[int]) -> int:
    _index1, _index2, flag = 0, 0, 0
    for _id, _value in enumerate(nums):
        if _value == 7 and flag == 0:
            _index1 = _id
            flag += 1
        elif flag == 1 and _value == 7:
            _index2 = _id
            flag += 5
    return _index2 - _index1


# do not modify below this line
print(get_index_of_seven([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(get_index_of_seven([1, 2, 3, 4, 5, 6, 8, 9]))
print(get_index_of_seven([2, 4, 7, 5, 7, 8, 4, 2]))

print(get_dist_between_sevens([1, 2, 7, 4, 5, 6, 7, 8, 9]))
print(get_dist_between_sevens([2, 7, 7, 7, 8]))
print(get_dist_between_sevens([7, 4, 8, 4, 2, 7]))
