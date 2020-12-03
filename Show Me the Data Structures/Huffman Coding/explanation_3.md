HuffmanNode was built on top of Node to have attributes like character, frequency and Huffman code.

The Queue class was introduced mainly for printing the tree. The Queue class and the tree printing function were copied from the notebooks in the nanodegree.

PriorityQueue was based on the Python data structure heapq. When performing pop and push, it is the heapq that does the job. However, a dictionary that maps the values in the heapq (key-value tuple) to HuffmanNodes allows the manupulation for HuffmandNodes simutaneously.

The code first builds a Huffman tree based on the input data with the PriorityQueue. Then it traverse the tree to encode each HuffmanNode, and further renders the encoded string. The decoding part uses a deque to iterate over the encoded string. The reason why a queue is used here is that once a leaf node is identified by verifying that there are no more children, the character that was used to determine this termination has to be added back.

time complexity: O(nlogn)
n is the length of a string
space complexity: O(n)
n is the length of a string if talking about encoded or decoded strings
n is the number of unique characters if talking about the dicitonary
