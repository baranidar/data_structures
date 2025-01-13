def merge_sort(arr):
    
    if len(arr) <= 1:
        return
    
    mid_point = len(arr) // 2

    left = arr[:mid_point]
    right = arr[mid_point:]

    merge_sort(left)
    merge_sort(right)

    merge_two_sorted_lists(left, right, arr)
    return arr

def merge_two_sorted_lists(l, r, arr):
    len_l = len(l)
    len_r = len(r)

    i = j = k = 0

    while i < len_l and j < len_r:
        if l[i] <= r[j]:
            arr[k] = l[i]
            i += 1
        else:
            arr[k] = r[j]
            j += 1
        k += 1
    
    while i < len_l:
        arr[k] = l[i]
        i += 1
        k += 1   

    while j < len_r:
        arr[k] = r[j]
        j += 1
        k += 1   
    
if __name__ == '__main__':
    arr = [10, 3, 15, 7, 8, 23, 98, 29]
    result = merge_sort(arr)
    print(result)