import multiprocessing

def merge_sort(array):
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]

    return result

if __name__ == "__main__":
    array = [1, 5, 3, 2, 4, 7, 6, 0]
    num_processes = 4

    with multiprocessing.Pool(num_processes) as pool:
        result = pool.map(merge_sort, np.array_split(array, num_processes))

    print(result)
