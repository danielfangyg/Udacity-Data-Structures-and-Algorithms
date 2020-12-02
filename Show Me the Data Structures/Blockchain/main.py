import hashlib
from datetime import datetime


class Block:
    def __init__(self, timestamp, data, previous_hash):
        assert data is not None, "input data is invalid"
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash(data)
        self.next = None

    def get_timestamp(self):
        return self.timestamp

    def get_data(self):
        return self.data

    def get_pervious_hash(self):
        return self.previous_hash

    def get_hash(self):
        return self.hash

    def calc_hash(self, data):
        if data is None:
            return None
        sha = hashlib.sha256()
        hash_str = data.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

    def __repr__(self):
        return ("Block(data: {}, timestamp: {}, "
                "hash: {}, previous_hash: {})").format(
                self.data, self.timestamp, self.hash, self.previous_hash)


class BlockChain:
    def __init__(self):
        self.head = None

    def append(self, data):
        if self.head is None:
            block = Block(timestamp=datetime.utcnow(), data=data,
                          previous_hash=None)
            self.head = block
            return

        current_block = self.head
        while current_block.next:
            current_block = current_block.next

        block = Block(timestamp=datetime.utcnow(), data=data,
                      previous_hash=current_block.get_hash())
        current_block.next = block

    def __len__(self):
        size = 0
        block = self.head
        while block:
            block = block.next
            size += 1
        return size

    def to_list(self):
        output = []
        block = self.head
        while block:
            output.append(block)
            block = block.next
        return output


def test_case1():
    # Test Case 1
    bl = BlockChain()
    data1 = "First Blockchain block"
    data2 = "Second Blockchain block"
    data3 = "Third Blockchain block"
    bl.append(data1)
    bl.append(data2)
    bl.append(data3)
    for block in bl.to_list():
        print(block)
    # expect to see 3 blocks

def test_case2():
    # Test Case 2
    bl1 = BlockChain()
    bl1.append("")
    bl1.append("")
    for block in bl1.to_list():
        print(block)
    # expect to see 2 blocks

def test_case3():
    # Test Case 3
    bl2 = BlockChain()
    bl2.append(None)
    bl2.append(None)
    print(bl2.to_list())

    # expect to raise AssertionError

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
    test_case3()
