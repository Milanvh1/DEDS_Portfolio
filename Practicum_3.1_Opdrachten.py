#Opdracht na HC 1
#Maak met python minimaal drie arrays van minimaal 20 willekeurige en niet gesorteerde integers (meer mag ook).
#Zoek op internet naar ten minste drie verschillende sorteeralgoritmes die je wilt gebruiken om de integer arrays mee te sorteren.
#Implementer je gekozen sorteeralgoritmes om de integer arrays mee te sorteren. Maak voor elk sorteeralgoritme een nieuwe methode aan die een integer array als parameter heeft en de integer array gesorteerd returnt.
#Kudos als je een moeilijk, super efficient of creatief algoritme kunt vinden óf zelfs bedenken ;)

import random

#quick_sort algoritme (snelste)
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x <= pivot]
        right = [x for x in arr[1:] if x > pivot]
        return quick_sort(left) + [pivot] + quick_sort(right)

#merge_sort algoritme (gemiddeld)
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr    
 
#bubble_sort algoritme (langzaamst)
def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

array1 = random.sample(range(1, 100), 20)
array2 = random.sample(range(1, 100), 20)
array3 = random.sample(range(1, 100), 20)       

sorted_array1 = quick_sort(array1.copy())
sorted_array2 = merge_sort(array2.copy())
sorted_array3 = bubble_sort(array3.copy())

print("Quicksort:", sorted_array1)
print("Mergesort:", sorted_array2)
print("Bubblesort:", sorted_array3)

