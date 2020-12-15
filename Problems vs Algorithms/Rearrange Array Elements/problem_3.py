def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if input_list is None:
        raise TypeError("Input list should not be none")
    if len(input_list) == 0:
        raise ValueError("Input list should not be empty")
    sorted_list = merge_sort(input_list)
    size = len(sorted_list)
    output_list1 = []
    output_list2 = []
    for idx in range(size):
        if idx % 2 == 0:
            output_list1.append(sorted_list[idx])
        else:
            output_list2.append(sorted_list[idx])
    output_sum1 = [value * 10**i for i, value in enumerate(output_list1)]
    output_sum1 = sum(output_sum1)
    output_sum2 = [value * 10**i for i, value in enumerate(output_list2)]
    output_sum2 = sum(output_sum2)
    return [output_sum1, output_sum2]


def merge_sort(arr):
    size = len(arr)
    if size == 1:
        return arr
    mid_idx = size // 2
    left_arr = merge_sort(arr[:mid_idx])
    right_arr = merge_sort(arr[mid_idx:])
    merge_arr = merge(left_arr, right_arr)
    return merge_arr


def merge(left_arr, right_arr):
    len_left = len(left_arr)
    len_right = len(right_arr)
    sorted_merge = []
    left_idx = 0
    right_idx = 0
    while left_idx < len_left and right_idx < len_right:
        if left_arr[left_idx] <= right_arr[right_idx]:
            sorted_merge.append(left_arr[left_idx])
            left_idx += 1
        else:
            sorted_merge.append(right_arr[right_idx])
            right_idx += 1

    if left_idx >= len_left:
        sorted_merge.extend(right_arr[right_idx:])
    elif right_idx >= len_right:
        sorted_merge.extend(left_arr[left_idx:])
    return sorted_merge


def test_case1():
    print(rearrange_digits([1, 2, 3, 4, 5]))
    # expected output
    # [531, 42]/[42, 531] or [542, 31]/[31, 542]


def test_case2():
    print(rearrange_digits([4, 6, 2, 5, 9, 8]))
    # expected output
    # [964, 852]/[852, 964]


def test_case3():
    print(rearrange_digits([0]))
    # expected output
    # [0, 0]


def test_case4():
    print(rearrange_digits(None))
    # expected output
    # TypeError("Input list should not be none")


def test_case5():
    print(rearrange_digits([]))
    # expected output
    # ValueError("Input list should not be empty")


if __name__ == '__main__':
    test_case1()
    test_case2()
    test_case3()
    try:
        test_case4()
    except Exception as err:
        print(err)

    try:
        test_case5()
    except Exception as err:
        print(err)
