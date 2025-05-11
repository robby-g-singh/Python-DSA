class TrieNode:
    def __init__(self, char=''):
        self.children = [None] * 26  # store pointers to the children
        self.is_end_word = False  # true if the node represents the end of a word
        self.char = char


class Trie:
    def __init__(self):
        self.root = TrieNode()

    @staticmethod
    # returns a value in range of 0-25 based on ASCII values of passed character compared with 'a'
    # the returned value will serve as an index to insert to check the children array based on the alphabetical
    # placement provided by this returned index value
    def get_index(letter):
        return ord(letter) - ord('a')

    def insert(self, key):
        if key is None:  # base case for passing a null key value
            return False

        key = key.lower()  # base case operation to only deal with lowercase characters
        current = self.root  # initialize a current variable to iterate through the Trie

        for letter in key:  # loop through the key value parameter
            index = self.get_index(letter)  # retrieve the index the letter would be stored in

            # if the current index is vacant, store the new node with value letter here
            if current.children[index] is None:
                current.children[index] = TrieNode(letter)

            current = current.children[index]  # iterate to the next level in the Trie

        current.is_end_word = True  # once the loop is exited, set the current char as the end of the word

    def search(self, key):
        # similar base case and operations as seen above
        if key is None:
            return False

        key = key.lower()
        current = self.root

        # loop through the key value parameter
        for letter in key:
            index = self.get_index(letter)
            # if the index where the letter should be in the Trie is vacant, it means the word is not in the Trie.
            # Return False
            if current.children[index] is None:
                return False
            current = current.children[index]  # iterate to next level in the Trie

        # once the key has been iterated over via the above for loop, and current is not Null and is_end_word = True,
        # return True. otherwise, return False:
        return current.is_end_word

    def delete(self, key):
        def _delete(node, word, depth):  # helper function
            if node is None:
                return False

            if depth == len(word):  # if reached the end of the word
                if not node.is_end_word:  # if word doesn't actually exist in Trie
                    return False
                node.is_end_word = False  # otherwise, undo the flag in order to delete
                return all(child is None for child in node.children)  # check to verify no children

            index = self.get_index(word[depth])  # retrieve the index based on alphabetical placement of the char
            child_node = node.children[index]  # set a variable for the node to delete

            should_delete_child = _delete(child_node, word, depth + 1)  # pass that node to the _delete function

            if should_delete_child:  # if it can be deleted, i.e. has no children and not end
                node.children[index] = None  # remove reference to child node
                # check to see if current node can be deleted as well:
                return not node.is_end_word and all(child is None for child in node.children)

            return False  # word exists but cannot delete the node (still needed)

        _delete(self.root, key, 0)  # pass variables to _delete helper function
