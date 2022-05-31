'''Find missing number from a list'''

listA = [63, 75, 26, 42, 96, 38, 58, 69, 56, 48, 32, 18, 1, 78, 94, 93, 66,
65, 34, 72, 55, 77, 71, 25, 40, 88, 44, 76, 89, 90, 62, 3, 33, 37, 4, 13, 50,
100, 22, 27, 17, 7, 85, 97, 39, 9, 83, 15, 41, 80, 19, 14, 64, 20, 51, 70, 73,
5, 99, 24, 21, 30, 57, 35, 84, 74, 45, 36, 23, 91, 68, 6, 67, 31, 52, 59, 43,
82, 60, 2, 47, 46, 98, 28, 54, 61, 11, 79, 10, 12, 8, 92, 49, 95, 87, 53, 29,
81, 86]

def get_missing_number(arr):
    '''Function to get missing number from a list'''
    array_len = len(arr)
    total = (array_len+1)*(array_len+2) // 2
    missing_num = total - sum(arr)
    return missing_num


num = get_missing_number(listA)
print(num)
