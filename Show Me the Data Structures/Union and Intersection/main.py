class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


def union(llist_1, llist_2):
    '''
    Runtime O(n) because
    1. Iterating over two linked_lists takes O(n), n = len(llist1) + len(llist2)
    2. Set.union takes O(n), n = len(llist1) + len(llist2)
    3. Appending to the new linked list takes O(n), n = len(union_set)
    '''
    node_1 = llist_1.head
    node_2 = llist_2.head
    set_1 = set()
    set_2 = set()
    while node_1:
        set_1.add(node_1.value)
        node_1 = node_1.next

    while node_2:
        set_2.add(node_2.value)
        node_2 = node_2.next

    union_set = set_1.union(set_2)
    union_llist = LinkedList()
    for node in union_set:
        union_llist.append(node)

    return union_llist


def intersection(llist_1, llist_2):
    '''
    Runtime O(n) because
    1. Iterating over two linked_lists takes O(n), n = len(llist1) + len(llist2)
    2. Set.intersecton takes O(n), n = min(len(llist1), len(llist2))
    3. Appending to the new linked list takes O(n), n = len(union_set)
    '''
    node_1 = llist_1.head
    node_2 = llist_2.head
    set_1 = set()
    set_2 = set()
    while node_1:
        set_1.add(node_1.value)
        node_1 = node_1.next

    while node_2:
        set_2.add(node_2.value)
        node_2 = node_2.next

    union_set = set_1.intersection(set_2)
    union_llist = LinkedList()
    for node in union_set:
        union_llist.append(node)

    return union_llist


if __name__ == '__main__':
    # Test case 1

    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
    element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    print(union(linked_list_1, linked_list_2))
    print(intersection(linked_list_1, linked_list_2))

    # Test case 2

    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()

    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
    element_2 = [1, 7, 8, 9, 11, 21, 1]

    for i in element_1:
        linked_list_3.append(i)

    for i in element_2:
        linked_list_4.append(i)

    print(union(linked_list_3, linked_list_4))
    print(intersection(linked_list_3, linked_list_4))
