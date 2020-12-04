import os


def find_files(subffix, path):
    if path is None:
        raise ValueError("Path should not be None")

    if not os.path.isdir(path):
        print("The input path is not a directory")
        if (os.path.isfile(path)
                and path.endswith(".{}".format(subffix))):
            return [path]
        else:
            return []

    file_path_list = []
    for sub in os.listdir(path):
        sub_path = os.path.join(path, sub)
        if os.path.isdir(sub_path):
            file_paths = find_files(subffix, sub_path)
            file_path_list.extend(file_paths)
        elif (os.path.isfile(sub_path)
                and sub_path.endswith(".{}".format(subffix))):
            file_path_list.append(sub_path)
    return file_path_list


def test_case1():
    test_list = find_files("c", os.path.join(os.getcwd(), r"File Recursion\testdir"))

    for path in test_list:
        print(path)

    # expected output
    '''
    %current work directory%\File Recursion\testdir\subdir1\a.c
    %current work directory%\File Recursion\testdir\subdir3\subsubdir1\b.c
    %current work directory%\File Recursion\testdir\subdir5\a.c
    %current work directory%\File Recursion\testdir\t1.c
    '''


def test_case2():
    test_list = find_files("b", os.path.join(os.getcwd(), r"File Recursion\testdir"))

    for path in test_list:
        print(path)
    # expected output: empty output


def test_case3():
    test_list = find_files(None, os.path.join(os.getcwd(), r"File Recursion\testdir"))

    for path in test_list:
        print(path)
    # expected output: empty output


def test_case4():
    test_list = find_files("c", None)

    for path in test_list:
        print(path)
    # expect ValueError message
    '''Path should not be None'''


def test_case5():
    test_list = find_files("c", os.path.join(os.getcwd(), r"File Recursion\testdir\t1.c"))

    for path in test_list:
        print(path)
    # expect output
    '''%current work directory%\File Recursion\testdir\t1.c'''


if __name__ == "__main__":
    import time
    print("***test case 1***")
    test_case1()
    print("\n")
    print("***test case 2***")
    time.sleep(1)
    test_case2()
    print("\n")
    print("***test case 3***")
    time.sleep(1)
    test_case3()
    print("\n")
    print("***test case 4***")
    time.sleep(1)
    try:
        test_case4()
    except ValueError as er:
        print(er)
    print("\n")
    print("***test case 5***")
    time.sleep(1)
    try:
        test_case5()
    except ValueError as er:
        print(er)
