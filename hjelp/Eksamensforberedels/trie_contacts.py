
class TrieNode:

    def __init__(self, char):
        self.char = char
        self.children = []
        self.is_word = False
        self.word_count = 0

    def get_child(self, char):
        for child in self.children:
            if child.char == c:
                return child
        return None


class Trie:

    def __init__(self):
        self.root = TrieNode('*')

    def add(self, word):
        current = self.root
        for char in word:
            next_node = current.get_child(char)
            if next_node is None:
                next_node = TrieNode(char)
                current.children.append(next_node)
            next_node.word_count += 1
            current = next_node
        current.is_word = True

    def find(self, word):
        current = self.root
        for char in word:
            next_node = current.get_child(char)
            if next_node is None:
                return 0
            current = next_node
        return current.word_count
