The reason why a ordered dictionary was chosen was that a dictionary enables the O(1) time complexity for get() and set(). Additionally, given that a ordered dictionary is ordered, it allows us to determine which key is the least recently used by shifting the order of elements when used.

time complexity: O(1)
space complexity: O(n) n is the capacity
