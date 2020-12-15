def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if ints is None:
        raise TypeError("The input list must not be none")

    if len(ints) == 0:
        return None

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

    # expect pass
    print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

    # expect None
    print(get_min_max([]))

    # expect TypeError(The input list must not be none)
    try:
        print(get_min_max(None))
    except Exception as err:
        print(err)
