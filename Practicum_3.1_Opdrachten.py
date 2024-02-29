# Import necessary libraries
import random
import time

# Generate arrays for testing
arr_quick = random.sample(range(1, 100), 20)
arr_merge = random.sample(range(1, 100), 20)
arr_bubble = random.sample(range(1, 100), 20)

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def print_result(algorithm_name, original_arr, sorted_arr, time_taken):
    print(f"{algorithm_name}:\nOriginal Array: {original_arr}\nSorted Array: {sorted_arr}\nTime Taken: {time_taken:.6f} seconds\n")

# Quick Sort
start_time = time.time()
sorted_arr_quick = quick_sort(arr_quick.copy())
end_time = time.time()
print_result("Quick Sort", arr_quick, sorted_arr_quick, end_time - start_time)

# Merge Sort
start_time = time.time()
sorted_arr_merge = merge_sort(arr_merge.copy())
end_time = time.time()
print_result("Merge Sort", arr_merge, sorted_arr_merge, end_time - start_time)

# Bubble Sort
start_time = time.time()
sorted_arr_bubble = bubble_sort(arr_bubble.copy())
end_time = time.time()
print_result("Bubble Sort", arr_bubble, sorted_arr_bubble, end_time - start_time)
