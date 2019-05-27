import unittest
from block_chain import BlockChain, Block

class TestBlockChain(unittest.TestCase):
    # The chain is empty. Test the first block can be appended to the chain
    def test_append_first_block(self):
        block_chain = BlockChain()
        self.assertTrue(block_chain.tail is None)
        first_block = Block.create_first_block()
        block_chain.append(first_block)
        self.assertTrue(block_chain.tail is not None)
        self.assertEqual([x for x in block_chain.read_content()], ['First Block'])

    # There are blocks in this chain already
    # Create a new block and append at the end of the chain
    def test_append_when_chain_is_not_empty(self):
        block_chain = BlockChain()
        first_block = Block.create_first_block()
        block_chain.append(first_block)
        next_block = Block.create_next_block(block_chain.tail.block)
        block_chain.append(next_block)
        # Get the contents of blocks in block chain in reverse order
        self.assertEqual([x for x in block_chain.read_content()], ['This is block - 1', 'First Block'])

    # Block in block chain is append only and not mutable
    # Test that data in a block can't be modified once it is appended to the chain
    def test_attempt_to_modify_last_block_content(self):
        block_chain = BlockChain()
        first_block = Block.create_first_block()
        block_chain.append(first_block)
        next_block = Block.create_next_block(block_chain.tail.block)
        block_chain.append(next_block)
        with self.assertRaises(AttributeError) as context:
            next_block.data = "Illegal modification"
            self.assertTrue("can't set attribute" in context.exception)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestBlockChain)
    unittest.TextTestRunner(verbosity=2).run(suite)
    # unittest.main(argv=['first-arg-is-ignored'], exit=False)
