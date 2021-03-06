#!python3

from prefixtreenode import PrefixTreeNode


class PrefixTree:
    """PrefixTree: A multi-way prefix tree that stores strings with efficient
    methods to insert a string into the tree, check if it contains a matching
    string, and retrieve all strings that start with a given prefix string.
    Time complexity of these methods depends only on the number of strings
    retrieved and their maximum length (size and height of subtree searched),
    but is independent of the number of strings stored in the prefix tree, as
    its height depends only on the length of the longest string stored in it.
    This makes a prefix tree effective for spell-checking and autocompletion.
    Each string is stored as a sequence of characters along a path from the
    tree's root node to a terminal node that marks the end of the string."""

    # Constant for the start character stored in the prefix tree's root node
    START_CHARACTER = ''

    def __init__(self, strings=None):
        """Initialize this prefix tree and insert the given strings, if any."""
        # Create a new root node with the start character
        self.root = PrefixTreeNode(PrefixTree.START_CHARACTER)
        # Count the number of strings inserted into the tree
        self.size = 0
        # Insert each string, if any were given
        if strings is not None:
            for string in strings:
                self.insert(string)

    def __repr__(self):
        """Return a string representation of this prefix tree."""
        return f'PrefixTree({self.strings()!r})'

    def is_empty(self):
        """Return True if this prefix tree is empty (contains no strings)."""
        # DONE
        # Time complexity: O(1), since the method simply checks the value of an attribute
        return self.size == 0

    def contains(self, string):
        """Return True if this prefix tree contains the given string."""
        # DONE
        # Time complexity: O(n), where n is the size of the string, since the entire string...
        # ...must be traversed in the worst-case
        # Set Prefix Tree node pointer to root
        pt_node = self.root
        # Iterate through each character of input string (first letter already checked)
        for char in string:
            # Return False if next char in string is not in current node's children
            if not pt_node.has_child(char):
                return False
            else:
                pt_node = pt_node.children[char]
        # Return True of string is present and the last node is terminal
        return pt_node.terminal

    def insert(self, string):
        """Insert the given string into this prefix tree."""
        # DONE
        # Time complexity: O(n), where n is the size of the string, since the entire string...
        # ...must be traversed/added in the worst-case (adding adds additional but negligible constant time)
        pt_node = self.root
        # Iterate through each character of input string
        for char in string:
            if not pt_node.has_child(char):
                # Add a new node with the character as a child
                new_node = PrefixTreeNode(char)
                pt_node.add_child(char, new_node)
            # Iterate to existing or newly created child
            pt_node = pt_node.children[char]
        # If last node not already set as terminal, set to terminal and increment size count (new string added)
        if not pt_node.terminal:
            pt_node.terminal = True
            self.size += 1

    def _find_node(self, string):
        """Return a pair containing the deepest node in this prefix tree that
        matches the longest prefix of the given string and the node's depth.
        The depth returned is equal to the number of prefix characters matched.
        Search is done iteratively with a loop starting from the root node."""
        # Time complexity: O(n), where n is the size of the string, since the entire string...
        # ...must be traversed in the worst-case
        # Match the empty string
        if len(string) == 0:
            return self.root, 0
        # Start with the root node
        node = self.root
        # DONE
        # Keep count of depth
        depth = 0
        # Iterate through each character of input string
        for char in string:
            # Return empty list if node has no children
            if not node.has_child(char):
                return [], depth
            else:
                node = node.children[char]
                depth += 1
        # Return node and depth at end of string
        return node, depth

    def complete(self, prefix):
        """Return a list of all strings stored in this prefix tree that start
        with the given prefix string."""
        # Time complexity: O(mn), where m is the number of strings and n is the size of the longest string.
        # ...The worst-case is achieved with m amount of n-long distinct words (each starting with different prefixes).
        # Create a list of completions in prefix tree
        completions = []
        # DONE
        node, _ = self._find_node(prefix)
        if node:
            return self._traverse(node, prefix, completions)
        else:
            return completions

    def strings(self):
        """Return a list of all strings stored in this prefix tree."""
        # Time complexity: O(mn), where m is the number of strings and n is the size of the longest string.
        # The worst-case is achieved with m amount of n-long distinct words (each starting with a different letter).
        # Create a list of all strings in prefix tree
        # DONE
        # Call `complete` method with empty string (root) passed as argument to return all strings
        return self.complete('')

    def _traverse(self, node, prefix, visit):
        """Traverse this prefix tree with recursive depth-first traversal.
        Start at the given node with the given prefix representing its path in
        this prefix tree and visit each node with the given visit function."""
        # Time complexity: O(mn), where m is the number of strings and n is the size of the longest string.
        # The worst-case is achieved with m amount of n-long distinct words (each starting with a different letter).
        # DONE
        if node.terminal == True:
            visit.append(prefix)
        for char in node.children:
            self._traverse(node.children[char], prefix + char, visit)
        return visit


def create_prefix_tree(strings):
    print(f'strings: {strings}')

    tree = PrefixTree()
    print(f'\ntree: {tree}')
    print(f'root: {tree.root}')
    print(f'strings: {tree.strings()}')

    print('\nInserting strings:')
    for string in strings:
        tree.insert(string)
        print(f'insert({string!r}), size: {tree.size}')

    print(f'\ntree: {tree}')
    print(f'root: {tree.root}')

    print('\nSearching for strings in tree:')
    for string in sorted(set(strings)):
        result = tree.contains(string)
        print(f'contains({string!r}): {result}')

    print('\nSearching for strings not in tree:')
    prefixes = sorted(set(string[:len(string)//2] for string in strings))
    for prefix in prefixes:
        if len(prefix) == 0 or prefix in strings:
            continue
        result = tree.contains(prefix)
        print(f'contains({prefix!r}): {result}')

    print('\nCompleting prefixes in tree:')
    for prefix in prefixes:
        completions = tree.complete(prefix)
        print(f'complete({prefix!r}): {completions}')

    print('\nRetrieving all strings:')
    retrieved_strings = tree.strings()
    print(f'strings: {retrieved_strings}')
    matches = set(retrieved_strings) == set(strings)
    print(f'matches? {matches}')


def main():
    # Simpe test case of string with Pokemon names
    strings = ['charmander', 'charmeleon', 'charizard', 'pikachu']
    create_prefix_tree(strings)


if __name__ == '__main__':
    main()
