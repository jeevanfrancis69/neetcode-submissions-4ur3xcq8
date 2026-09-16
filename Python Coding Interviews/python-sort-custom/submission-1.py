from typing import List


def sort_words(words: List[str]) -> List[str]:
    return split_sort(words, len, False)


def sort_numbers(numbers: List[int]) -> List[int]:
    return split_sort(numbers, abs, True)


def split_sort(arr, key, reverse):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = split_sort(arr[:mid], key, reverse)
    right = split_sort(arr[mid:], key, reverse)

    return merge(left, right, key, reverse)

def merge(left,right,key,reverse):
    i = j = 0
    result = []

    while i < len(left) and j < len(right):

        if not reverse:
            if (key(left[i]) >= key(right[j])):
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        if reverse:
            if (key(left[i]) <= key(right[j])):
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# do not modify below this line
print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]))
