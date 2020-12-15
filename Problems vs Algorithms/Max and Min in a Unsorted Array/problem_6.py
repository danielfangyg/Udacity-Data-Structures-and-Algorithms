def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    output_min = 0
    output_max = 0
    for value in ints:
        output_min = min(value, output_min)
        output_max = max(value, output_max)

    return (output_min, output_max)


if __name__ == '__main__':
    import random

    l = [i for i in range(0, 10)]  # a list containing 0 - 9
    random.shuffle(l)

    print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
