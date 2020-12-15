def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    if input_list is None:
        raise TypeError("The input list must not be none")

    if len(input_list) == 0:
        return -1
    size = len(input_list)
    return rotated_array_search_recursive(input_list, number, 0, size-1)


def rotated_array_search_recursive(input_list, number, start_idx, end_idx):

    mid_idx = (start_idx+end_idx)//2
    first = input_list[start_idx]
    last = input_list[end_idx]
    middle = input_list[mid_idx]
    if number == middle:
        return mid_idx
    elif number == first:
        return start_idx
    elif number == last:
        return end_idx

    if middle > first and middle > last:
        if first < number and number < middle:
            return binarysearch(input_list, number, start_idx+1, mid_idx-1)
        else:
            return rotated_array_search_recursive(input_list, number,
                                                  mid_idx+1, end_idx-1)
    elif middle < first and middle < last:
        if middle < number and number < last:
            return binarysearch(input_list, number, mid_idx+1, end_idx-1)
        else:
            return rotated_array_search_recursive(input_list, number,
                                                  start_idx+1, mid_idx-1)
    else:
        return binarysearch(input_list, number, start_idx+1, end_idx-1)


def binarysearch(input_list, number, start_idx, end_idx):
    if start_idx > end_idx:
        return -1

    mid_idx = (start_idx+end_idx)//2
    middle = input_list[mid_idx]
    if number == middle:
        return mid_idx
    elif number < middle:
        return binarysearch(input_list, number, start_idx, mid_idx-1)
    else:
        return binarysearch(input_list, number, mid_idx+1, end_idx)


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list,
                                                                 number):
        print("Pass")
    else:
        print("Fail")


if __name__ == '__main__':
    '''expect pass for all'''
    test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
    test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
    test_function([[6, 7, 8, 1, 2, 3, 4], 8])
    test_function([[6, 7, 8, 1, 2, 3, 4], 1])
    test_function([[6, 7, 8, 1, 2, 3, 4], 10])
    test_function([[], 0])
