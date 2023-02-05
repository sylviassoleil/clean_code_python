# def split(string):
#     return key
# operations = ['-', '+'...]
#
# def recursive(string):
#     output = split(string)
#     finished = all([(i.isnumeric())| (i in operations) for i in output])
#     if not finished:
#
#     output = split(string)
#     finished = all([i.isnumeric()|i in operations for i in output])
#     if not finished:
#
# array = []
def partition(array, lo, hi):
    pivot = array[hi]
    i = lo-1
    for ind in range(lo, hi):
        if array[ind] < pivot:
            i+=1
            # order by
            array[i], array[ind] = array[ind], array[i]
    i+=1
    array[i], array[hi] = array[hi], array[i]
    return i

def quickSortInPlace(array, lo, hi):
    if (lo>=hi) | (lo<0):
        return array

    p = partition(array, lo, hi)
    quickSortInPlace(array, lo, p-1)
    quickSortInPlace(array, p+1, hi)
    return array

def quickSort(array):
    if len(array)<=1:
        return array

    less = []
    greater = []
    pivot = array[-1]
    for i in range(len(array)-1):
        if array[i]<pivot:
            less.append(array[i])
        if array[i]>pivot:
            greater.append(array[i])
    return quickSort(less) + [pivot] + quickSort(greater)





if __name__ == '__main__':
    array = [6, 5, 3, 4]
    # d = quickSort(array)
    d = quickSortInPlace(array, 0, len(array)-1)