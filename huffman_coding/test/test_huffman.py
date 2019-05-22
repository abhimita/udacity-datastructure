import sys
import unittest
sys.path.append('./src')
from huffman import HuffmanCoding

class TestHuffmanCoding(unittest.TestCase):

    def test_decoded_msg_given_the_original_msg(self):
        txt = "The bird is the word"
        huffman_coding = HuffmanCoding(txt)
        print ("The size of the data is: {}\n".format(sys.getsizeof(txt)))
        print ("The content of the data is: {}\n".format(txt))
        encoded_data, tree = huffman_coding.huffman_encoding()
        print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
        print ("The content of the encoded data is: {}\n".format(encoded_data))
        self.assertTrue(txt, huffman_coding.huffman_decoding(encoded_data, tree))

    def test_when_msg_is_null(self):
        with self.assertRaises(Exception) as context:
            huffman_coding = HuffmanCoding(None)
        self.assertTrue("Text to be encoded can't be null" in context.exception)

    def test_when_msg_is_single_char(self):
        txt = "T"
        huffman_coding = HuffmanCoding(txt)
        print ("The size of the data is: {}\n".format(sys.getsizeof(txt)))
        print ("The content of the data is: {}\n".format(txt))
        encoded_data, tree = huffman_coding.huffman_encoding()
        print(encoded_data)
        print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
        print ("The content of the encoded data is: {}\n".format(encoded_data))
        decoded_data = huffman_coding.huffman_decoding(encoded_data, tree)
        print(decoded_data)
        self.assertTrue(txt, huffman_coding.huffman_decoding(encoded_data, tree))

if __name__ == '__main__':
    unittest.main()