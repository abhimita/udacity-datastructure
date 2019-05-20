import sys

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
        if start_node is None:
            return
        else:
            self.traverse(start_node.left, code=code + '0', code_lookup=code_lookup)
            self.traverse(start_node.right, code=code + '1', code_lookup=code_lookup)
            if start_node.left is None and start_node.right is None:
                code_lookup[start_node.value] = code

"""
Class implementing Huffman coding algorithm
"""
class HuffmanCoding:
    def __init__(self, text):
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

    """
    Method to encode text into Huffman code
    Return: Huffman encoded string containing 0 & 1 
    """
    def huffman_encoding(self):
        while len(self.frequency.keys()) > 1:
            sorted_by_count = sorted(self.frequency, key=lambda x: self.frequency[x].count)
            if self.frequency[sorted_by_count[0]].count > self.frequency[sorted_by_count[1]].count:
                first_node = self.frequency[sorted_by_count[1]]
                second_node = self.frequency[sorted_by_count[0]]
            else:
                first_node = self.frequency[sorted_by_count[0]]
                second_node = self.frequency[sorted_by_count[1]]
            new_value = first_node.value + ':' + second_node.value
            new_node = Node(
                new_value,
                first_node.get_count() + second_node.get_count(),
                left=first_node,
                right=second_node
            )
            self.frequency.pop(sorted_by_count[0])
            self.frequency.pop(sorted_by_count[1])
            self.frequency[new_value] = new_node
        root_node = self.frequency[new_value]
        tree = BinaryTree(root_node)
        tree.traverse(tree.root, self.lookup, '')
        return ''.join([self.lookup[c] for c in self.text]), tree

    """
    Method for decoding Huffman encoded string to retrieve the original message
    """
    def huffman_decoding(self,data,tree):
        begin_decoding = True
        decoded_msg = []
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
    a_great_sentence = "The bird is the word"
    huffman_coding = HuffmanCoding(a_great_sentence)

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_coding.huffman_encoding()

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_coding.huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))