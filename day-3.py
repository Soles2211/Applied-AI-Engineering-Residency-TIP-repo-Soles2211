# Day 3

def length_of_longest_substring (s):
    seen = {}
    left = 0
    max_length = 0

    for right in s: 
        if seen[right] in seen and seen[right] >= left:
            left = seen[right] + 1
        seen[right] = right
        max_length = max(max_length, right - left + 1)
    return max_length
        
print(length_of_longest_substring([1,2,3,4,5]))