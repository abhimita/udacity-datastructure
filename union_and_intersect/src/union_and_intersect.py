class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + (" -> " if cur_head.next else "")
            cur_head = cur_head.next
        return out_string

    def get_next(self):
        ptr = self.head
        while ptr is not None:
            prev, ptr = ptr, ptr.next
            yield prev

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


class UnionIntersectionOperator:
    def __init__(self):
        pass
    def union(self, *linked_list):
        new_list = LinkedList()
        nodes = {}
        for index, llist in enumerate(linked_list):
            for n in llist.get_next():
                if not nodes.get(n.value, None):
                    nodes[n.value] = n
                    new_list.append(n.value)
        return new_list


    def intersection(self, *linked_list):
        new_list = LinkedList()
        # nodes is a dictionary of tuple. The tuple has two elements
        # first element is pointer to the node and identification of the list in which it appears
        # if value = 1 is found in 1st list then node[1] = (<ptr to node with value 1>, 1)
        # If the same value s found in the 1st list again then there is no change to dictionary entry
        # If value = 1 is found in second list as well, output that node to be part of intersection result
        # If value -1 is found only in second list then, don't do anything
        nodes = {}
        for index, llist in enumerate(linked_list):
            for n in llist.get_next():
                if nodes.get(n.value, None) is None: # item not seen so far
                    if index == 0: # first list being processed
                        nodes[n.value] = (n, index)
                else:
                    if nodes[n.value][1] == index - 1:
                        node = nodes[n.value][0]
                        nodes[n.value] = (node, index)
                        if index == len(linked_list) - 1:
                            new_list.append(n.value)

        return new_list

