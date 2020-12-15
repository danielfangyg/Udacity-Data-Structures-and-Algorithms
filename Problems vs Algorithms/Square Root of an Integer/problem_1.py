def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if not isinstance(number, int):
        raise TypeError("The number must be an integer")
    if number < 0:
        raise ValueError("The number must be non-negative")

    if number == 0 or number == 1:
        return number
    return sqrt_recursive(number, 0, number)


def sqrt_recursive(number, small, big):
    mid = (small+big)//2
    if small + 1 == big:
        return small

    if mid**2 > number:
        return sqrt_recursive(number, small, mid)
    elif mid**2 < number:
        return sqrt_recursive(number, mid, big)
    else:
        return mid


def test():
    print("Pass" if (3 == sqrt(9)) else "Fail")
    print("Pass" if (0 == sqrt(0)) else "Fail")
    print("Pass" if (4 == sqrt(16)) else "Fail")
    print("Pass" if (1 == sqrt(1)) else "Fail")
    print("Pass" if (5 == sqrt(27)) else "Fail")
    try:
        print("Pass" if (5 == sqrt(-1)) else "Fail")
    except ValueError as err:
        print(err)

    try:
        print("Pass" if (5 == sqrt(None)) else "Fail")
    except TypeError as err:
        print(err)

    try:
        print("Pass" if (5 == sqrt(5.1)) else "Fail")
    except TypeError as err:
        print(err)


if __name__ == '__main__':
    test()
