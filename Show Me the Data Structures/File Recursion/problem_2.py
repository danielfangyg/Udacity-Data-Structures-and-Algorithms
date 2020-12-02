import os


def find_files(subffix, path):
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
    test_list = find_files("c", r"E:\Projects\Data Structures and Algorithms\Show Me the Data Structures\File Recursion\testdir")

    for path in test_list:
        print(path)

    # expected output
    '''
    E:\Projects\Data Structures and Algorithms\Show Me the Data Structures\File Recursion\testdir\subdir1\a.c
    E:\Projects\Data Structures and Algorithms\Show Me the Data Structures\File Recursion\testdir\subdir3\subsubdir1\b.c
    E:\Projects\Data Structures and Algorithms\Show Me the Data Structures\File Recursion\testdir\subdir5\a.c
    E:\Projects\Data Structures and Algorithms\Show Me the Data Structures\File Recursion\testdir\t1.c
    '''


def test_case2():
    test_list = find_files("b", r"E:\Projects\Data Structures and Algorithms\Show Me the Data Structures\File Recursion\testdir")

    for path in test_list:
        print(path)
    # expected output: empty output


def test_case3():
    test_list = find_files(None, r"E:\Projects\Data Structures and Algorithms\Show Me the Data Structures\File Recursion\testdir")

    for path in test_list:
        print(path)
    # expected output: empty output


def test_case4():
    test_list = find_files("c", None)

    for path in test_list:
        print(path)
    # expect TypeError

if __name__ == "__main__":
    print("***test case 1***")
    test_case1()
    print("\n")
    print("***test case 2***")
    test_case2()
    print("\n")
    print("***test case 3***")
    test_case3()
    print("\n")
    print("***test case 4***")
    test_case4()
