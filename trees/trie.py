class TrieNode:
    def __init__(self, char=''):
        self.children = [None] * 26  # store pointers to the children
        self.is_end_word = False  # true if the node represents the end of a word
        self.char = char


class Trie:
    def __init__(self):
        self.root = TrieNode()

    @staticmethod
    def get_index(letter):
        return ord(letter) - ord('a')

    def insert(self, key):
        if key is None:
            return False

        key = key.lower()
        current = self.root

        # iterate over each letter
        # if letter exists, go down a level
        # else simply create a Trie Node and go down a level

        for letter in key:
            index = self.get_index(letter)

            if current.children[index] is None:
                current.children[index] = TrieNode(letter)
                print(letter, "inserted")

            current = current.children[index]

        current.is_end_word = True
        print("'" + key + "' inserted")

    def search(self, key):
        if key is None:
            return False

        key = key.lower()

        current = self.root

        # iterative over each letter in the key
        # if the letter doesn't exist, return False
        # if the letter exists, go down a level
        # return True only if leaf node reached and Trie has been traversed based on length of the key

        for letter in key:
            index = self.get_index(letter)
            if current.children[index] is None:
                return False
            current = current.children[index]

        if current is not None and current.is_end_word:
            return True

        return False

    def delete(self, key):
        if not key:
            return

        stack = []  # stack to hold (parent, char_index)
        node = self.root

        for letter in key:
            index = self.get_index(letter)
            if not node.children[index]:
                # word doesn't exist
                return
            stack.append((node, index))
            node = node.children[index]

        # Un-mark the end of the word
        if not node.is_end_word:
            return
        node.is_end_word = False

        # backtrack and clean up unnecessary nodes
        for parent, index in reversed(stack):
            child = parent.children[index]

            if child.is_end_word or any(child.children):
                break
            parent.children[index] = None

