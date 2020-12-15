The fundamental of the trie here is very similar to the one taught in the class. An additional problem is to find all suffixes according to a prefix. The method applied in the code is to recursively traverse the tree structure and add the character of each node to the list of suffixes.

Time complexity:
TrieNode.insert: O(1)
TrieNode.suffixes: O(n) n is the total number of characters in all suffixes
Trie.insert: O(n) n is the number of children
Trie.find: O(n) n is the total number of characters up to the prefix

Space complexity: O(n)
n is the total number of characters
