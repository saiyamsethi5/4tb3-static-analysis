#input_code.py
#test input case for optimizer

#Test Case of Nested For Loop
def perimeter_increment_calc (height, width):
    for i in range (0, height):
        for j in range (0, width):
            print (i + j)

# Test Case for If Else Optimization
def find_item(item_to_find, input_list):
    if (str(item_to_find) in input_list):
        index_item = input_list.index(item_to_find)
    else:
        index_item = -1

    return index_item

 # Test Case for Avoid Multiple Finite Differences Optimization
def random_numbers ():
    for i in range(0, 10):
        print(i * 100)

#Test Case for Loop Overhead Optimization
def binarySearch(x,low,mid,high,list):
    if (x == list[mid]):
        return mid
    elif (x > list[mid]):
        low = mid+1
    elif (x < list[mid]):
        high = mid-1

    for i in range(low, high):
        if x == list[i]:
            return i

    return -1
