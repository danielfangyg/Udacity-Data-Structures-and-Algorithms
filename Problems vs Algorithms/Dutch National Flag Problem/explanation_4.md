The overall idea to tackle this problem is to move 0 to the leftmost and move 2 to the rightmost. Once the list has been traversed like this, the generated output list will be the sorted one.

There are two ways to do this. One is to leverage Python's built-in list methods to delete elements and insert them into either the leftmost or rightmost of the list. The other is to swap 0 and 2 with the elements in the left and right by tracking number of 0 and 2 that have been positioned.

Time complexity: O(n), single traversal
n is the size of the array
Space complexity: O(n)
n is the size of the array
