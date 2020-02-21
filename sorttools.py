import typing as tp
from functools import wraps


def sort_output(func):
    """Decorator create a copy of input data, sort
    copy and return this new copy with sorted data
    
    Arguments:
        func {[function]} -- any inplace sorting function
    """
    @wraps(func)
    def wrapper(data: tp.List[int], *args, **kwargs):
        copy_of_data = data.copy()
        func(copy_of_data, *args, **kwargs)
        return copy_of_data
    return wrapper


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


@sort_output
def select_sort(data: tp.List[int], ascending=True) -> tp.List[int]:
    """""Select sorting
    
    Arguments:
        data {tp.List[int]} -- input list with integers
    
    Returns:
        tp.List[int] -- ordered list with integers
        ascending {bool} -- direction of soring
    """
    select_sort_inplace(data, ascending=ascending)
