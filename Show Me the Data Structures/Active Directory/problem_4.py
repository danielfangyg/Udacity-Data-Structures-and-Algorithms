from collections import deque


class Group(object):
    def __init__(self, _name):
        assert _name is not None, "name is invalid"
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    q = deque()
    q.append(group)
    sub_users = []
    while len(q) > 0:
        current_group = q.popleft()
        sub_users.extend(current_group.get_users())
        for sub_group in current_group.get_groups():
            q.append(sub_group)
    users = group.get_users() + sub_users
    if user in users:
        return True
    else:
        return False


def test_case1():
    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")

    sub_child_user = "sub_child_user"
    sub_child.add_user(sub_child_user)

    child.add_group(sub_child)
    parent.add_group(child)

    print(is_user_in_group("sub_child_user", child))

    # Expect True in ouput


def test_case2():
    parent = Group("")
    child = Group("")
    sub_child = Group("")

    sub_child_user = ""
    sub_child.add_user(sub_child_user)

    child.add_group(sub_child)
    parent.add_group(child)

    print(is_user_in_group("", child))

    # Expect True in ouput


def test_case3():
    parent = Group(u'A unicode \u018e string \xf1')
    child = Group(u'B unicode \u018e string \xf1')
    sub_child = Group(u'C unicode \u018e string \xf1')

    sub_child_user = u'D unicode \u018e string \xf1'
    sub_child.add_user(sub_child_user)

    child.add_group(sub_child)
    parent.add_group(child)

    print(is_user_in_group(u'D unicode \u018e string \xf1', child))

    # Expect True in ouput


def test_case4():
    parent = Group(None)
    child = Group(None)
    sub_child = Group(None)

    sub_child_user = None
    sub_child.add_user(sub_child_user)

    child.add_group(sub_child)
    parent.add_group(child)

    print(is_user_in_group(None, child))

    # Expect AssertionError

if __name__ == '__main__':
    import time
    print("***test case 1***")
    test_case1()
    print("\n")
    print("***test case 2***")
    test_case2()
    print("\n")
    print("***test case 3***")
    time.sleep(1)
    test_case3()
    print("\n")
    print("***test case 4***")
    time.sleep(1)
    test_case4()
