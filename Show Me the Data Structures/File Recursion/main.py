import os


def find_files(subffix, path):
    # o.listdir
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


if __name__ == "__main__":
    test_list = find_files("c", "./testdir")
    for path in test_list:
        print(path)
