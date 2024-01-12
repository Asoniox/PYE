class Order():
    def lt(a, b):
        """
        Same as a < b.
        Kindly borrowed from the `operator` module.
        """
        return a < b

    def gt(a, b):
        """
        Same as a > b.
        Kindly borrowed from the `operator` module.
        """
        return a > b

    ascending = lt
    descending = gt

def bubbleSort(_list: list, order: Order):
    """
    Sort a list with the Bubble Sort algorithm.

    Parameters
    ----------
    _list: `list`
        List to be sorted.

    order: `bubblesort.Order`
        Whether the sort should be ascending or descending.

    Returns
    -------
    sorted_list: `list`
        The same list but sorted. Overwrites the unsorted list completely.
    """
    n = len(_list)
    for i in range(n): # 0-N, step 1
        for j in range(n-1, i, -1):
            if order(_list[j], _list[j-1]):
                _list[j], _list[j-1] = _list[j-1], _list[j]
    return _list
