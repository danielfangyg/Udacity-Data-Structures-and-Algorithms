Clean leading and trailing slashes before spliting a path into a list. Include a default handler in Route to replace the None value. Others are staightforward.

Time complexity:
RouteTrieNode.insert: O(1)
RouteTrie.insert: O(n), n is the number of parts
RouteTrie.find: O(n), n is the number of parts
Route.add_handler: same as RouteTrie.insert
Route.lookup: same as RouteTrie.find

Space complexity: O(mn)
m is the number of parts in pathes, n is the number of characters in parts
