# Introduction

The goal is to write code to implement basic functionality of block chain using Python data strutures.

## Directory organization

There are two directories. 
1. `src` - contains the source code for Huffman coding
2. `test` - contains the unit test cases. 

## Execution

To execute the code from command line, following steps are needed.

1. `cd <directory where code is checked out>`
2. `PYTHONPATH=block_chain/src python block_chain/test/test_block_chain.py`

### Output

```
test_append_first_block (__main__.TestBlockChain) ... ok
test_append_when_chain_is_not_empty (__main__.TestBlockChain) ... ok
test_attempt_to_modify_last_block_content (__main__.TestBlockChain) ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.001s

OK
```

## Code design

Block chain implementation uses several data structures

1. `Block` - Python object
2. `LinkedListNode` - Node which contains reference to a block and a reference to previous node. This is the object that chains the blocks together.
3. `BlockChain`- Linked list with tail pointer pointing to the last node in the chain.

Block chain is a write-once data structure. Creation and insertion of the block to the linked list is safe guarded that once added content of the block can't changed. This is achieved using Python's `getter` & `setter` method.

In a block chain addition of blocks are allowed only at the end. So keeping only the `tail` pointer is enough as new blocks come in.

## Efficiency

### Time efficiency

Adding a new block requires only manipulation of the tail pointer and can be done in O(1). Printing data from the blocks take O(n) assuming that there are n blocks in the chain.

### Space Complexity

Space complexity is O(n) assuming there are n data blocks. The linked list will have n entries as well plus additional storage for tail pointer. Overall space complexity is O(n)

