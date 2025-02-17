from dec import time_it

@time_it
def linear_search(number_list, number_to_find):
    for index, element in enumerate(number_list):
        if element == number_to_find:
            return index
    return -1

@time_it
def binary_search(number_list, number_to_find):
    left_index = 0
    right_index = len(number_list) - 1
    mid_index = 0
    
    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = number_list[mid_index]
        
        if mid_number == number_to_find:
            return mid_index
        
        if mid_number < number_to_find:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1
    return -1

def binary_search_recursive(number_list, number_to_find, left_index, right_index):
    
    if right_index < left_index:
        return -1
    
    mid_index = (left_index + right_index) // 2
    mid_number = number_list[mid_index]
    if mid_index>= len(number_list) or mid_index<0:
        return-1
    
    if mid_number == number_to_find:
        return mid_index
    if mid_number < number_to_find:
        left_index = mid_index + 1
    else:
        right_index = mid_index - 1
        
    return binary_search_recursive(number_list, number_to_find, left_index, right_index)
    
    
    
    


if __name__ == '__main__' :
    
    number_list = [12,15,17,19,21,24,45,67,81]
    number_to_find = int(input("Enter a number:"))
    
    # number_list = [i for i in range(10000001)]
    # number_to_find = 1000000
    
    index = linear_search(number_list, number_to_find)
    print(f"Number found at index {index} using linear search")
    
    indexs = binary_search(number_list, number_to_find)
    print(f"Number found at index {indexs} using binary search")
    
    indexs = binary_search_recursive(number_list, number_to_find, 0, len(number_list))
    print(f"Number found at index {indexs} using binary search")