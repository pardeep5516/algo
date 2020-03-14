def partition(list, first, last):
    pivot  = list[first]
    left = first + 1
    right = last
    while True:
        while left <= right and list[left] <= pivot:
            left  = left + 1
        while left <= right and list[right] >= pivot:
            right = right - 1
        if right < left:
            break
        else:
            list[left], list[right] = list[right], list[left]
    list[first], list[right] = list[right], list[first]
    return right
def quick_sort(list, first, last):
    if first < last:
        p = partition(list, first, last)
        quick_sort(list, first, p-1)
        quick_sort(list, p + 1, last)


list=[98,28,14,69,35]
quick_sort(list, 0, len(list)-1)
print(list)