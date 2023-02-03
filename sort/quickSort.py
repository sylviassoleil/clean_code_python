import random as rd


def quickSort(array, low=None, high=None, eq=None):
    if len(array) <= 1:
        return array
    pivot = array[-1]
    if low is None:
        low = []
    if high is None:
        high = []
    if eq is None:
        eq = [pivot]
    for i in range(len(array) - 1):
        e = array[i]
        if e > pivot:
            high.append(e)
        elif e < pivot:
            low.append(e)
        else:
            eq.append(eq)
    return quickSort(low) + quickSort(eq) + quickSort(high)


def partition(ar, lo, hi):
    pivot = ar[hi]

    i = lo - 1
    for j in range(lo, hi):
        if ar[j] <= pivot:
            i += 1
            ar[j], ar[i] = ar[i], ar[j]  # the last left element is now at index i
    i += 1
    ar[hi], ar[i] = ar[i], ar[hi]
    return i


def quickSortInplace(ar, lo, hi):
    '''
    // Sorts a (portion of an) array, divides it into partitions, then sorts those
algorithm quicksort(A, lo, hi) is
  // Ensure indices are in correct order
  if lo >= hi || lo < 0 then
    return

  // Partition array and get the pivot index
  p := partition(A, lo, hi)

  // Sort the two partitions
  quicksort(A, lo, p - 1) // Left side of pivot
  quicksort(A, p + 1, hi) // Right side of pivot

// Divides array into two partitions
algorithm partition(A, lo, hi) is
  pivot := A[hi] // Choose the last element as the pivot

  // Temporary pivot index
  i := lo - 1

  for j := lo to hi - 1 do
    // If the current element is less than or equal to the pivot
    if A[j] <= pivot then
      // Move the temporary pivot index forward
      i := i + 1
      // Swap the current element with the element at the temporary pivot index
      swap A[i] with A[j]

  // Move the pivot element to the correct pivot position (between the smaller and larger elements)
  i := i + 1
  swap A[i] with A[hi]
  return i // the pivot index

    :return:
    '''
    if lo >= hi:
        return

    p = partition(ar, lo, hi)
    # print(p)
    quickSortInplace(ar, lo, p - 1)
    quickSortInplace(ar, p + 1, hi)
    return ar


if __name__ == '__main__':
    pass
    seq = list(set([rd.randint(-50, 50) for i in range(10)]))
    l = quickSort(seq)
    l = quickSortInplace(seq, 0, len(seq) - 1)
