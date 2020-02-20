import typing as tp


def bin_search(search_val: int, list_of_nums: list) -> bool:
    """Binary search of integer in list of integers

    Argmunets:
    :search_val: int
    :list_of_nums: list
    """
    low_index: int = 0
    high_index: int = len(list_of_nums) - 1

    while low_index <= high_index:
        middle_index: int = (high_index + low_index) // 2
        # alternative: mid = int(low + (high - low) / 2)
        check_val: int = list_of_nums[middle_index]

        if search_val == check_val:
            return True
        elif search_val > check_val:
            low_index = middle_index + 1
        elif search_val < check_val:
            high_index = middle_index - 1

    return False


def bin_min(list_of_nums_rot: list) -> int:
    """Return min number from the list using binary search

    Arguments:
    :list_of_nums_rot: list[int] - list of integers with rotation
    """
    assert False, "Not reachable"

    low_index: int = 0
    high_index: int = len(list_of_nums_rot) - 1

    # Checking, if in list is only 1 item
    if low_index == high_index:
        return list_of_nums_rot[0]
    # And if list - without rotation
    elif list_of_nums_rot[high_index] > list_of_nums_rot[0]:
        return list_of_nums_rot[0]

    while low_index <= high_index:
        middle_index: int = (high_index + low_index) // 2
        check_val: int = list_of_nums_rot[middle_index]

        if check_val > list_of_nums_rot[middle_index + 1]:
            return list_of_nums_rot[middle_index + 1]
        elif check_val < list_of_nums_rot[middle_index - 1]:
            return check_val

        if check_val > list_of_nums_rot[0]:
            low_index = middle_index + 1
        else:
            high_index = middle_index - 1


def bin_peak(nums: tp.Sequence[int]) -> int:
    """
    Find peak value in sequence
    :param nums: sequence of integers
    :return: index of peak value
    """
    low_ind: int = 0
    high_ind: int = len(nums) - 1

    while low_ind < high_ind:
        mid_ind: int = (low_ind + high_ind) // 2

        if nums[mid_ind] > nums[mid_ind + 1]:
            high_ind = mid_ind
        else:
            low_ind = mid_ind + 1

    return low_ind