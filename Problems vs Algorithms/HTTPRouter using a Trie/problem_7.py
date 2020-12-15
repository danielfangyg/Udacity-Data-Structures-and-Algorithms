import re


# A RouteTrieNode will be similar to our autocomplete TrieNode...
# with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler=None):
        # Initialize the node with children as before, plus a handler
        self.handler = handler
        self.children = {}

    def insert(self, part_of_path, handler):
        # Insert the node as before
        self.children[part_of_path] = RouteTrieNode(handler)

    def __str__(self):
        return "RouteTrieNode({})".format(self.handler)


# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, root_handler=None, default_handler=None):
        # Initialize the trie with an root node and a handler,
        # this is the root path or home page node
        self.default_handler = default_handler
        self.root = RouteTrieNode(root_handler)

    def insert(self, part_of_path, handler):
        # Similar to our previous example you will
        # want to recursively add nodes
        # Make sure you assign the handler to only
        # the leaf (deepest) node of this path
        current_node = self.root
        for part in part_of_path:
            if part not in current_node.children:
                current_node.insert(part, self.default_handler)
            current_node = current_node.children[part]

        current_node.handler = handler

    def find(self, part_of_path):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match

        current_node = self.root
        if part_of_path == [""]:
            return current_node.handler

        for part in part_of_path:
            if part not in current_node.children:
                return self.default_handler

            current_node = current_node.children[part]
        return current_node.handler


# The Router class will wrap the Trie and handle
class Router:
    def __init__(self, handler=None, default_handler=None):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for
        # 404 page not found responses as well!
        self.trie = RouteTrie(handler, default_handler)

    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        part_of_path = self.split_path(path)
        self.trie.insert(part_of_path, handler)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        part_of_path = self.split_path(path)
        return self.trie.find(part_of_path)

    def split_path(self, path):
        # you need to split the path into parts for
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        path_cleaned = re.sub(r"^\/", "", path)
        path_cleaned = re.sub(r"\/$", "", path_cleaned)
        part_of_path = path_cleaned.split("/")
        return part_of_path


if __name__ == '__main__':
    # remove the 'not found handler' if you did not implement this
    router = Router("root handler", "not found handler")
    # add a route
    router.add_handler("/home/about", "about handler")
    # should print 'root handler'
    print(router.lookup("/"))
    # should print 'not found handler' or None if you did not implement one
    print(router.lookup("/home"))
    # should print 'about handler'
    print(router.lookup("/home/about"))
    # should print 'about handler' or None
    # if you did not handle trailing slashes
    print(router.lookup("/home/about/"))
    # should print 'not found handler' or None if you did not implement one
    print(router.lookup("/home/about/me"))
