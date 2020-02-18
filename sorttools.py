import typing as tp


def select_sort_inplace(data: tp.List[int], ascending=True) -> None:
    """Select sorting in-place
    
    Arguments:
        data {tp.List[int]} -- input list with integers
        ascending {bool} -- direction of soring
    """
    start_ind = 0
    end_ind = len(data) - 1
    while start_ind <= end_ind:
        for i in range(start_ind+1, end_ind+1):
            if ascending:
                if data[i] < data[start_ind]:
                    data[i], data[start_ind] = data[start_ind], data[i]
            elif not ascending:
                if data[i] > data[start_ind]:
                    data[i], data[start_ind] = data[start_ind], data[i]
        start_ind += 1


def select_sort(data: tp.List[int], ascending=True) -> tp.List[int]:
    """""Select sorting
    
    Arguments:
        data {tp.List[int]} -- input list with integers
    
    Returns:
        tp.List[int] -- ordered list with integers
        ascending {bool} -- direction of soring
    """
    result: tp.List[int] = data.copy()
    select_sort_inplace(result, ascending=ascending)
    return result
