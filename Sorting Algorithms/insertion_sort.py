## Insertion sort

arr1 = [6,5,3,1,8,7]

def insertion_sort_ascending(input_array):
    for i in range(1, len(input_array)):
        k = input_array[i]
        j = i-1
        while j>=0 and input_array[j]>k:
            input_array[j+1] = input_array[j]
            j -= 1
        input_array[j+1] = k
    return input_array

print(insertion_sort_ascending(arr1))

def insertion_sort_descending(input_array):
    for i in range(1, len(input_array)):
        k = input_array[i]
        j=i-1
        while j>=0 and input_array[j]<k:
            input_array[j+1] = input_array[j]
            j -= 1
        input_array[j+1] = k
    return input_array

print(insertion_sort_descending(arr1))

