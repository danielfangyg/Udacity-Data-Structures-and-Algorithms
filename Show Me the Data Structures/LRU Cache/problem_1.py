from collections import OrderedDict


class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.cach_dict = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        value = self.cach_dict.get(key)
        if value is not None:
            self.cach_dict.move_to_end(key)
            # print(value)
            return value
        else:
            # print(-1)
            return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache.
        # If the cache is at capacity remove the oldest item.
        if key is None:
            raise ValueError("The key must be a non-none value")

        self.cach_dict[key] = value
        if len(self.cach_dict) > self.capacity:
            self.cach_dict.popitem(last=False)


def test_case1():
    our_cache = LRU_Cache(5)
    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(4, 4)
    print(our_cache.get(1))       # returns 1
    print(our_cache.get(2))      # returns 2
    print(our_cache.get(9))      # returns -1
    our_cache.set(5, 5)
    our_cache.set(6, 6)
    print(our_cache.get(3))      # returns -1


def test_case2():
    our_cache = LRU_Cache(0)
    our_cache.set(1, 1)
    print(our_cache.get(1))       # returns -1


def test_case3():
    our_cache = LRU_Cache(5)
    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(4, 4)
    our_cache.set(5, None)
    print(our_cache.get(5))  # returns -1
    our_cache.set(None, 6)
    # raise ValueError with message
    '''The key must be a non-none value'''


if __name__ == "__main__":
    print("****test case 1****")
    test_case1()
    print("\n")
    print("****test case 2****")
    test_case2()
    print("\n")
    print("****test case 3****")
    try:
        test_case3()
    except ValueError as er:
        print(er)
