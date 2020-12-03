The data structure used was simply a list. More importantly, the algorithm was based on recursion. The reason why recursion can be applied here was that os.walk is not allowed to be used. Thus, the first step is to work with files and subdirectories under the current folder before exploring files under subdirectories. In this case, a recursion algorithm works because each time when the function is called, it checks the the files under the current folder and then goes to the next level. Subsequently, it allows traversing over the folder and its all descendants.

time complexity: O(n)
n is the total number of directories and files under the path
space complexity: O(n)
n is the number of files with the specified subffix
