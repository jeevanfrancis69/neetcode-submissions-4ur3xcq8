from typing import List


def sort_words(words: List[str]) -> List[str]:
    return merge(words)

def sort_numbers(numbers: List[int]) -> List[int]:
    return merge(numbers)

def sort_decimals(numbers: List[float]) -> List[float]:
    return merge(numbers)

def merge(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge(arr[:mid])
    right = merge(arr[mid:])
    
    return merge_sort(left,right)
    

def merge_sort(L,R):
    i = 0 #left
    j = 0 #right
    result = []

    while i < len(L) and j < len(R):
        if (L[i] >= R[j]):
            result.append(L[i])
            i += 1
        else:
            result.append(R[j])
            j += 1

    result.extend(L[i:])
    result.extend(R[j:])
    return result



# do not modify below this line
print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, 5, 3, 2, 4, 11, 19, 9, 2, 5, 6, 7, 4, 2, 6]))

print(sort_decimals([3.14, 2.82, 6.433, 7.9, 21.555, 21.554]))
