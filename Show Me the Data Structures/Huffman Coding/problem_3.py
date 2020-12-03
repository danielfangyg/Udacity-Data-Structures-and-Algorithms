import heapq
import sys
from collections import deque


class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def set_left_child(self, node):
        self.left = node

    def set_right_child(self, node):
        self.right = node

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def has_left_child(self):
        return self.left is not None

    def has_right_child(self):
        return self.right is not None

    def __repr__(self):
        return f"Node({self.get_value()})"


class HuffmanNode(Node):
    def __init__(self, char, freq, code=""):
        super().__init__()
        self.char = char
        self.freq = freq
        self.code = code

    def set_char(self, char):
        self.char = char

    def set_freq(self, freq):
        self.freq = freq

    def set_code(self, code):
        self.code = code

    def get_char(self):
        return self.char

    def get_freq(self):
        return self.freq

    def get_code(self):
        return self.code

    def __repr__(self):
        return "HuffmanNode({}, {}, {})".format(
                self.get_char(), self.get_freq(), self.get_code())


class Queue:
    def __init__(self):
        self.q = deque()

    def enq(self, value):
        self.q.appendleft(value)

    def deq(self):
        if len(self.q) > 0:
            return self.q.pop()
        else:
            return None

    def __len__(self):
        return len(self.q)

    def __repr__(self):
        if len(self.q) > 0:
            s = "<enqueue here>\n_________________\n"
            s += "\n_________________\n".join([str(item) for item in self.q])
            s += "\n_________________\n<dequeue here>"
            return s
        else:
            return "<queue is empty>"


class Tree:
    def __init__(self, node):
        self.root = node

    def get_root(self):
        return self.root

    def __repr__(self):
        level = 0
        q = Queue()
        visit_order = list()
        node = self.get_root()
        q.enq((node, level))
        while(len(q) > 0):
            node, level = q.deq()
            if node is None:
                visit_order.append(("<empty>", level))
                continue
            visit_order.append((node, level))
            if node.has_left_child():
                q.enq((node.get_left_child(), level+1))
            else:
                q.enq((None, level+1))

            if node.has_right_child():
                q.enq((node.get_right_child(), level+1))
            else:
                q.enq((None, level+1))

        s = "Tree:\n"
        previous_level = -1
        for i in range(len(visit_order)):
            node, level = visit_order[i]
            if level == previous_level:
                s += " | " + str(node)
            else:
                s += "\n" + str(node)
                previous_level = level
        s += "\n"
        s += "-"*200
        return s


class PriorityQueue:
    def __init__(self, list_of_tuple):
        self.pq = list_of_tuple
        self.node_map = {}
        for tuple_ in list_of_tuple:
            freq, char = tuple_
            self.node_map[tuple_] = HuffmanNode(char=char, freq=freq)
        heapq.heapify(self.pq)

    def push(self, node):
        tuple_ = (node.get_freq(), node.get_char())
        heapq.heappush(self.pq, tuple_)
        self.node_map[tuple_] = node

    def pop(self):
        node_value = heapq.heappop(self.pq)
        return self.node_map[node_value]

    def __repr__(self):
        return str([self.node_map[tuple_] for tuple_ in self.pq])

    def __len__(self):
        return len(self.pq)


def build_huffman_tree(freq_dict):
    freq_lt = [(value, key) for key, value in freq_dict.items()]
    huffman_pq = PriorityQueue(freq_lt)
    counter = 0
    while len(huffman_pq) > 1:
        s1 = huffman_pq.pop()
        s2 = huffman_pq.pop()
        s_sum = HuffmanNode(char="dummy"+str(counter),
                            freq=s1.get_freq() + s2.get_freq())
        s_sum.set_left_child(s1)
        s_sum.set_right_child(s2)
        huffman_pq.push(s_sum)
        counter += 1

    huffman_tree = Tree(huffman_pq.pop())
    return huffman_tree


def encode_huffman_tree(tree):
    q = Queue()
    code_map = {}
    node = tree.get_root()
    if not node.has_left_child() and not node.has_right_child():
        char = node.get_char()
        if "dummy" not in char:
            node.set_code("0")
            code_map[char] = node.get_code()
            return tree, code_map

    q.enq(node)
    while(len(q) > 0):
        node = q.deq()
        char = node.get_char()
        if "dummy" not in char:
            code_map[char] = node.get_code()

        if node.has_left_child():
            left_child = node.get_left_child()
            left_child.set_code(node.get_code() + "0")
            q.enq(left_child)

        if node.has_right_child():
            right_child = node.get_right_child()
            right_child.set_code(node.get_code() + "1")
            q.enq(right_child)
    return tree, code_map


def huffman_encoding(data):
    if data is None or len(data) == 0:
        raise ValueError("The input data must not be none "
                         "and the length must be larger than 0")
    freq_dict = {}
    for key in data:
        freq_dict[key] = freq_dict.get(key, 0) + 1
    huffman_tree = build_huffman_tree(freq_dict)
    huffman_tree_encoded, code_map = encode_huffman_tree(huffman_tree)
    encoded_list = [code_map[key] for key in data]
    encoded_str = "".join(encoded_list)
    return encoded_str, huffman_tree_encoded


def huffman_decoding(data, tree):
    node = tree.get_root()
    if len(set(data)) == 1:
        return node.get_char()*len(data)

    char_q = deque(data)
    decoded_list = []

    while(len(char_q) > 0):
        char = char_q.popleft()
        if char == "0":
            if node.has_left_child():
                node = node.get_left_child()
            else:
                decoded_list.append(node.get_char())
                char_q.appendleft(char)
                node = tree.get_root()
        elif char == "1":
            if node.has_right_child():
                node = node.get_right_child()
            else:
                decoded_list.append(node.get_char())
                char_q.appendleft(char)
                node = tree.get_root()

        if len(char_q) == 0:
            decoded_list.append(node.get_char())
    decoded_data = "".join(decoded_list)
    return decoded_data


def test_case1():
    a_great_sentence = "AAAAAAABBBCCCCCCCDDEEEEEE"

    print("The size of the data is: {}\n".format(
            sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)
    print("The size of the encoded data is: {}\n".format(
            sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(
            sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))

    # expected output
    '''
    The size of the data is: 74

    The content of the data is: AAAAAAABBBCCCCCCCDDEEEEEE

    The size of the encoded data is: 32

    The content of the encoded data is: 1010101010101000100100111111111111111000000010101010101

    The size of the decoded data is: 74

    The content of the encoded data is: AAAAAAABBBCCCCCCCDDEEEEEE
    '''


def test_case2():
    a_great_sentence = "The bird is the word"

    print("The size of the data is: {}\n".format(
            sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)
    print("The size of the encoded data is: {}\n".format(
            sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(
            sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))

    # expected output
    '''
    The size of the data is: 69

    The content of the data is: The bird is the word

    The size of the encoded data is: 36

    The content of the encoded data is: 1111001101011011111100101111011010000011100010011010110001100001011110

    The size of the decoded data is: 69

    The content of the encoded data is: The bird is the word
    '''


def test_case3():
    a_great_sentence = ""

    print("The size of the data is: {}\n".format(
            sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)
    print("The size of the encoded data is: {}\n".format(
            sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(
            sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))

    # expected to raise ValueError with message
    '''"The input data must not be None"
                     "and the length must be larger than 0"'''


def test_case4():
    a_great_sentence = None

    print("The size of the data is: {}\n".format(
            sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)
    print("The size of the encoded data is: {}\n".format(
            sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(
            sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))

    # expected to raise ValueError with message
    '''"The input data must not be None"
                     "and the length must be larger than 0"'''


def test_case5():
    a_great_sentence = "aaaaaa"

    print("The size of the data is: {}\n".format(
            sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)
    print("The size of the encoded data is: {}\n".format(
            sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(
            sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))

    # expected output:
    '''
    The size of the data is: 55
    The content of the data is: aaaaaa

    The size of the encoded data is: 24

    The content of the encoded data is: 000000

    The size of the decoded data is: 55

    The content of the encoded data is: aaaaaa
    '''


if __name__ == "__main__":
    import time
    print("***test case 1***")
    test_case1()
    print("\n")
    print("***test case 2***")
    test_case2()
    print("\n")
    print("***test case 3***")
    time.sleep(1)
    try:
        test_case3()
    except ValueError as er:
        print(er)
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
    test_case5()
