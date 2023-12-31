def quicksort(A, start, end):
    if start < end:
        parti = lomutoPartition(A, start, end)
        quicksort(A, start, parti-1)
        quicksort(A, parti+1, end)

def lomutoPartition(A, start, end):
    pivot = A[end]
    i = low-1
    for j in range(start, end):
        if pivot >= A[j]:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[end] = A[end], A[i+1]
    return i+1

if __name__ == "__main__":
    A = [4, 2, 7, 3, 1, 9, 6, 0, 8]
    start, end = 0, len(A)-1
    print("BEFORE SORTING:", A)
    quicksort(A, start, end)
    print("AFTER SORTING:", A)
