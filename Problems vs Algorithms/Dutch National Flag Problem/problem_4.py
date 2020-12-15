def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """

    if input_list is None:
        raise TypeError("The input list must not be none")

    if len(input_list) == 0:
        return input_list

    # method 1
    '''
    size = len(input_list)
    i = 0
    counter = 0
    while counter < size:
        if input_list[i] == 0:
            del input_list[i]
            input_list.insert(0, 0)
            i += 1
        elif input_list[i] == 2:
            del input_list[i]
            input_list.append(2)
        else:
            i += 1

        counter += 1
    '''

    # method 2
    size = len(input_list)
    zero_idx = 0
    two_idx = size-1
    i = 0
    counter = 0
    while counter < size:
        if input_list[i] == 0:
            input_list = swap_positions(input_list, i, zero_idx)
            zero_idx += 1
            i += 1
        elif input_list[i] == 2:
            input_list = swap_positions(input_list, i, two_idx)
            two_idx -= 1
        else:
            i += 1

        counter += 1
    return input_list


def swap_positions(list_, pos1, pos2):
    list_[pos1], list_[pos2] = list_[pos2], list_[pos1]
    return list_


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


if __name__ == '__main__':
    # expect pass for all
    test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
    test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
    test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
    test_function([])
