# Implementing Trie
# Has search insert and starts_with

# class TrieNode:
#
#     def __init__(self):
#         # I could also use here dict and then go (['a']) but this way I still have O(1) to access el.
#         self.children = [None] * 26
#         self.isEndOfWord = False
#
#
# class Trie:
#
#     def __init__(self):
#         self.root = TrieNode()
#
#
#     def _charToIndex(self, ch):
#         # private helper function
#         # Converts key current character into index
#         # use only 'a' through 'z' and lower case
#         # I use this one fore list
#         return ord(ch) - ord('a')
#
#     def insert(self, key):
#
#         # If not present, inserts key into trie
#         # If the key is prefix of trie node,
#         # just marks leaf node
#         cur = self.root
#         length = len(key)
#         for c in range(length):
#             index = self._charToIndex(key[c])
#
#             # if current character is not present
#             if not cur.children[index]:
#                 cur.children[index] = TrieNode()
#             cur = cur.children[index]
#
#         # mark last node as leaf
#         cur.isEndOfWord = True

    # def search(self, key):
    #
    #     # Search key in the trie
    #     # Returns true if key presents in trie, else false
    #
    #     cur = self.root
    #     length = len(key)
    #     for c in range(length):
    #         index = self._charToIndex(key[c])
    #         if not cur.children[index]:
    #             return False
    #         cur = cur.children[index]
    #
    #     return cur.isEndOfWord

    # def starts_with(self, key):
    #
    #     # Search key in the trie
    #     # Returns true if there is a word that start with key
    #
    #     cur = self.root
    #     length = len(key)
    #     for c in range(length):
    #         index = self._charToIndex(key[c])
    #         if not cur.children[index]:
    #             return False
    #         cur = cur.children[index]
    #
    #     return True

# driver function
# def main():
#     # Input keys (use only 'a' through 'z' and lower case)
#     keys = ["the", "a", "there", "anaswe", "any",
#             "by", "their"]
#     output = ["Not present in trie",
#               "Present in trie"]
#
#     # Trie object
#     t = Trie()
#
#     # Construct trie
#     for key in keys:
#         t.insert(key)
#
#     # Search for different keys
#     print("{} ---- {}".format("the", output[t.search("the")]))
#     print("{} ---- {}".format("these", output[t.search("these")]))
#     print("{} ---- {}".format("their", output[t.search("their")]))
#     print("{} ---- {}".format("thaw", output[t.search("thaw")]))

# main()

class TrieNode:
    """A node in the trie structure"""

    def __init__(self, char):
        # the character stored in this node
        self.char = char

        # whether this can be the end of a word
        self.is_end = False

        # a counter indicating how many times a word is inserted
        # (if this node's is_end is True)
        self.counter = 0
        self.end_app = {}

        # a dictionary of child nodes
        # keys are characters, values are nodes
        self.children = {}


class Trie(object):
    """The trie object"""

    def __init__(self):
        """
        The trie has at least the root node.
        The root node does not store any character
        """
        self.root = TrieNode("")

    def insert(self, word, path, indx):
        """Insert a word into the trie"""
        node = self.root

        # Loop through each character in the word
        # Check if there is no child containing the character, create a new child for the current node
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                # If a character is not found,
                # create a new node in the trie
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node

        # Mark the end of a word
        node.is_end = True
        # if node.children == {}:
        #     arr = []
        if node.is_end:
            if path in node.end_app:
                node.end_app[path].append(indx)
            if path not in node.end_app:
                node.end_app[path] = []
                node.end_app[path].append(indx)

        # node.children["word"] = {}
        # Increment the counter to indicate that we see this word once more
        node.counter += 1


    def search(self, key):

        # Search key in the trie
        # Returns true if key presents in trie, else false

        cur = self.root
        length = len(key)
        for c in key:
            if c not in cur.children.keys():
                return False
            cur = cur.children[c]

        return cur.end_app



    # def dfs(self, node, prefix):
    #     """Depth-first traversal of the trie
    #
    #     Args:
    #         - node: the node to start with
    #         - prefix: the current prefix, for tracing a
    #             word while traversing the trie
    #     """
    #     if node.is_end:
    #         self.output.append((prefix + node.char, node.counter))
    #
    #     for child in node.children.values():
    #         self.dfs(child, prefix + node.char)
    #
    # def query(self, x):
    #     """Given an input (a prefix), retrieve all words stored in
    #     the trie with that prefix, sort the words by the number of
    #     times they have been inserted
    #     """
    #     # Use a variable within the class to keep all possible outputs
    #     # As there can be more than one word with such prefix
    #     self.output = []
    #     node = self.root
    #
    #     # Check if the prefix is in the trie
    #     for char in x:
    #         if char in node.children:
    #             node = node.children[char]
    #         else:
    #             # cannot found the prefix, return empty list
    #             return []
    #
    #     # Traverse the trie to get all candidates
    #     self.dfs(node, x[:-1])
    #
    #     # Sort the results in reverse order and return
    #     return sorted(self.output, key=lambda x: x[1], reverse=True)