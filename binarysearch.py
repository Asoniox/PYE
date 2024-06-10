key = 5
_list = [1, 2, 3, 5, 10]
N = len(_list)
start = 0
end = N - 1
flag = True  # or pos = -10**100
while start <= end and flag:  # or pos == -10**100
    m = (start + end) / 2
    if _list[m] == key:
        flag = False  # or pos = m
    elif key > _list[m]:
        start = m + 1
    else:
        end = m - 1
