# Быстрая сортировка
def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]
    return quicksort(less) + [pivot] + quicksort(greater)


print(quicksort([10, 5, 2, 3, 7, 87, 4]))


# Сортировка слиянием
def merge_soft(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        merge_soft(left)
        merge_soft(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = left[j]
                j += 1
            k += 1

        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1


list1 = [1, 4, 5, 7, 2, 23, 26, 1, 6]
merge_soft(list1)
print(list1)
