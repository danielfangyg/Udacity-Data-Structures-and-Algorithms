Given the input array is rotated, splitting from the middle, either left or right part of the array is sorted. For the sorted part, we can apply the usual binary serach method. For the unsorted part, it is still a rotated array that can be passed into the original function. Thus, we can solve the problem recursively.

Time complexity: O(logn)
n is the size of the array
Space complexity: O(n)
n is the size of the array
