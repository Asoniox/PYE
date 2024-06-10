"""bubblesort.py
---
Simple and straightforward bubble sort module, with convenience features.

Example Usage:
    ```python
    import bubblesort
    from bubblesort import Order

    array = [1, 6, 3, 2, 7, 8, 3, 1]
    bubbleSort(array, Order.ascending)
    ```
"""


class Order:
    def lt(a, b):
        """Same as a < b.

        Kindly borrowed from the `operator` module.
        """
        return a < b

    def gt(a, b):
        """Same as a > b.

        Kindly borrowed from the `operator` module.
        """
        return a > b

    ascending = lt
    descending = gt


def bubbleSort(array: list, order: Order):
    """Sort a list with the Bubble Sort algorithm.

    Parameters
    ----------
    array: `list`
        List to be sorted.

    order: `bubblesort.Order`
        Whether the sort should be ascending or descending.

    Returns
    -------
    sortedarray: `list`
        The same list but sorted. Overwrites the unsorted list completely.
    """
    n = len(array)
    for i in range(n):  # 0-N, step 1
        for j in range(n - 1, i, -1):
            if order(array[j], array[j - 1]):
                array[j], array[j - 1] = array[j - 1], array[j]
    return array
