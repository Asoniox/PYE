"""Sourced from: http://ebooks.edu.gr/ebooks/v/pdf/8547/4618/24-0601-01_Programmatismos-Ypologiston_G-EPAL_Didaktiko-Yliko-Mathiti/"""  # noqa


def binarysearch(array, key):
    """Θεωρούμε πως η λίστα είναι ταξινομημένη σε αύξουσα σειρά.

    Παράμετροι
        array `list[Any]`: Λίστα την οποία θα ψάξουμε
        key `Any`: Κλειδί που θέλουμε να βρούμε μέσα στην λίστα

    Επιστρέφει
        found `bool`: Αν βρέθηκε το κλειδί στην λίστα
    """
    first = 0  # Αρχή της λίστας
    last = len(array) - 1  #
    found = False
    while first <= last and not found:
        mid = (first + last) // 2  # noqa: single slash for integer division in python 2
        if array[mid] == key:
            found = True
        elif array[mid] < key:
            first = mid + 1
        else:
            last = mid - 1

    return found


def bubblesort(array):
    """Απλή ευθείας ανταλλαγής ταξινόμηση σε αύξουσα σειρά

    Παράμετροι
        array `list[Any]`: Λίστα την οποία θα ψάξουμε

    Επιστρέφει
        array `list[Any]`: Η ταξινομημένη λίστα
    """
    n = len(array)
    for i in range(n - 1):  # n index 1 to 0
        for j in range(n - 1, i, -1):  # n - 1, i = 0, backwards step
            if array[j] < array[j - 1]:  # ascending
                array[j], array[j - 1] = array[j - 1], array[j]

    return array


array1 = [1, 2, 3, 6, 8, 4, 21, 7, 3, 8, 12]
print(array1)
print("-----")
bubblesort(array1)
print(array1)
print("-----")
setkey = 7
foundkey = binarysearch(array1, setkey)
print(foundkey)
