from typing import List


def sort_words(words: List[str]) -> List[str]:
    return split_sort(words)


def sort_numbers(numbers: List[int]) -> List[int]:
    return split_sortInt(numbers)


def split_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = split_sort(arr[:mid])
    right = split_sort(arr[mid:])

    return mergeStringStr(left,right)

def split_sortInt(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = split_sortInt(arr[:mid])
    right = split_sortInt(arr[mid:])

    return merge(left,right)



def mergeStringStr(l,r):
    i = 0 #left
    j = 0 #right
    result = []

    while (i < len(l) and j < len(r)):
        if (len(l[i]) >= len(r[j])):
            result.append(l[i])
            i += 1
        else:
            result.append(r[j])
            j += 1
    
    result.extend(l[i:])
    result.extend(r[j:])
    return result

def merge(l,r):
    i = 0 #left
    j = 0 #right
    result = []

    while (i < len(l) and j < len(r)):
        if (abs(l[i])) <= (abs(r[j])):
            result.append(l[i])
            i += 1
        else:
            result.append(r[j])
            j += 1
    
    result.extend(l[i:])
    result.extend(r[j:])
    return result




# do not modify below this line
print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]))
