import hashlib
import datetime

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self._index = index
        self._timestamp = timestamp
        self._data = data
        self._previous_hash = previous_hash
        self._hash = self.calc_hash()

    @property
    def index(self):
        return self._index

    @property
    def timestamp(self):
        return self._timestamp

    @property
    def data(self):
        return self._data

    @property
    def hash(self):
        return self._hash

    @property
    def previous_hash(self):
        return self._previous_hash

    def calc_hash(self):
        m = hashlib.sha256()
        m.update((str(self._index) + str(self._timestamp) + str(self._data) + str(self.previous_hash)).encode('utf-8'))
        return m.hexdigest()

    @classmethod
    def create_first_block(cls):
        return cls(0, datetime.datetime.now(), "First Block", "0")

    @classmethod
    def create_next_block(cls, last_block):
        return cls(last_block.index + 1, datetime.datetime.now(), "This is block - %s" % str(last_block.index + 1), last_block.hash)

class LinkedListNode:
    def __init__(self, block, prev=None):
        self._block = block
        self._prev = prev

    @property
    def block(self):
        return self._block

    @property
    def prev(self):
        return self._prev

class BlockChain:
    def __init__(self):
        self._tail = None

    @property
    def tail(self):
        return self._tail

    @tail.setter
    def tail(self, node):
        self._tail = node

    def append(self, block):
        if not self._validate(block):
            raise Exception('Block validation fails')
        if self.tail is None:
            self.tail = LinkedListNode(block)
            self.head = self.tail
        else:
            node = LinkedListNode(block, self.tail)
            self.tail = node


    def _validate(self, block):
        if self.tail is None:
            if block.index != 0 or block.previous_hash != "0":
                return False
        else:
            if self.tail.block.hash != block.previous_hash or block.index != self.tail.block.index + 1:
                return False
        return True

    def read_content(self):
        ptr = self.tail
        while ptr is not None:
            text = ptr.block.data
            ptr = ptr.prev
            yield text







