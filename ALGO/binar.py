def binarySearch(sortarr, value):
    low = 0
    high = len(sortarr)-1

    while low <= high:
        mid = (low+high)//2 # проверяется средний элемент каждый раз
        guess = sortarr[mid]
        if guess == value:
            return mid
        if guess > value:
            high = mid - 1
        else:
            low = mid + 1
    return None