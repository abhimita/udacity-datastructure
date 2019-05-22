import random
import string

"""
Class for binary tree node
"""
class Node:
    def __init__(self, value, count=1, left=None, right=None):
        self.value = value  # content/value of the node
        self.right = right  # Reference to right node
        self.left = left    # Reference to left node
        self.count = count  # Frequency count of the value
    def get_count(self):
        return self.count
    def set_count(self, count):
        self.count = count
    def __repr__(self):
        return str(self.value + ':' + str(self.count))

"""
Class for binary tree 
"""
class BinaryTree:
    def __init__(self, node):
        self.root = node
    """'
    Recursive traversal of the binary tree used for generating Huffman code
    """
    def traverse(self, start_node, code_lookup, code=''):
        # Base case
        if start_node is None:
            return
        else:
            # Traverse left subtree - add '0' to Huffman code generated so far
            self.traverse(start_node.left, code=code + '0', code_lookup=code_lookup)
            # Traverse right subtree - add '1' to Huffman code generated so far
            self.traverse(start_node.right, code=code + '1', code_lookup=code_lookup)
            # Leaf node
            if start_node.left is None and start_node.right is None:
                code_lookup[start_node.value] = code

"""
Class implementing Huffman coding algorithm
"""
class HuffmanCoding:
    def __init__(self, text):
        if not text:
            raise Exception("Text to be encoded can't be null")
        self.text = text
        self.frequency = {}
        self.sorted_keys = []
        self.lookup = {}
        # Get frequency count of each character and build a dictionary
        # Key of the dictionary is character in input data stream
        # Value of the dictionary is an instance of Node class
        for c in text:
            if self.frequency.get(c, None):
                n = self.frequency[c]
                n.set_count(n.get_count() + 1)
            else:
                n = Node(value=c, count=1)
            self.frequency[c] = n
        if len(text) == 1:
            dummy_char = random.choice(''.join([c for c in string.ascii_letters if c != text[0]]))
            self.frequency[dummy_char] = Node(value=dummy_char, count=0)
        print(self.frequency)

    """
    Method to encode text into Huffman code
    Return: Huffman encoded string containing 0 & 1 
    """
    def huffman_encoding(self):
        while len(self.frequency.keys()) > 1:
            # Sort the characters based on their frequency of usage
            sorted_by_count = sorted(self.frequency, key=lambda x: self.frequency[x].count)
            # Two characters with least frequency are considered as two leaf nodes of a binary tree
            if self.frequency[sorted_by_count[0]].count > self.frequency[sorted_by_count[1]].count:
                first_node = self.frequency[sorted_by_count[1]]
                second_node = self.frequency[sorted_by_count[0]]
            else:
                first_node = self.frequency[sorted_by_count[0]]
                second_node = self.frequency[sorted_by_count[1]]
            new_node = Node(
                first_node.value + ':' + second_node.value,
                first_node.get_count() + second_node.get_count(),
                left=first_node,
                right=second_node
            )
            # Two nodes with least frequency are deleted from dictionary
            self.frequency.pop(sorted_by_count[0])
            self.frequency.pop(sorted_by_count[1])
            # Parent node is introduced in the dictionary
            self.frequency[first_node.value + ':' + second_node.value] = new_node
        root_node = self.frequency[self.frequency.keys()[0]]
        tree = BinaryTree(root_node)
        tree.traverse(tree.root, self.lookup, '')
        return ''.join([self.lookup[c] for c in self.text]), tree

    """
    Method for decoding Huffman encoded string to retrieve the original message
    """
    def huffman_decoding(self,data,tree):
        begin_decoding = True
        decoded_msg = []
        # For every 0 or 1 in the inputstream traverse the binary tree using following rules
        # move to left subtree when input character is 0
        # move to right subtree when input character is 1
        # Once leaf node is encountered, "value" of the node is output
        # Repeat the above process till inputstream is exhnausted
        for d in data:
            if begin_decoding:
                start_node = tree.root
                begin_decoding = False
            if d == '1':
                start_node = start_node.right
            else:
                start_node = start_node.left
            if start_node.left is None and start_node.right is None:
                begin_decoding = True
                decoded_msg.append(start_node.value)
        return ''.join(decoded_msg)

if __name__ == "__main__":
    txt = "TaTpTpT"
    huffman_coding = HuffmanCoding(txt)
    encoded_data, tree = huffman_coding.huffman_encoding()
    decoded_data = huffman_coding.huffman_decoding(encoded_data, tree)
    print(encoded_data, decoded_data)