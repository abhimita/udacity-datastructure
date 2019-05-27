import unittest
from union_and_intersect import LinkedListOp, LinkedList

class TestLinkedListOp(unittest.TestCase):
    def test_intersection_with_no_common_elements(self):
        first_list = self._create_linked_list([1, 2, 3, 4])
        second_list = self._create_linked_list([5, 6, 7, 8])
        linked_list_op = LinkedListOp()
        self.assertEqual(linked_list_op.intersection(first_list, second_list).head, None)

    def test_intersection_with_common_elements(self):
        first_list = self._create_linked_list([1, 2, 3, 6, 8])
        second_list = self._create_linked_list([5, 6, 7, 8])
        linked_list_op = LinkedListOp()
        intersect_result = linked_list_op.intersection(first_list, second_list)
        self.assertEqual(intersect_result.size(), 2)
        self.assertEqual(str(intersect_result), "6 -> 8")

    def test_intersection_with_one_empty_list(self):
        first_list = self._create_linked_list([1, 2, 3, 6, 8])
        second_list = self._create_linked_list([])
        linked_list_op = LinkedListOp()
        intersect_result = linked_list_op.intersection(first_list, second_list)
        self.assertEqual(intersect_result.size(), 0)
        self.assertEqual(str(intersect_result), "")

    def test_union_with_one_empty_list(self):
        first_list = self._create_linked_list([1, 2, 3, 6, 8])
        second_list = self._create_linked_list([])
        linked_list_op = LinkedListOp()
        union_result = linked_list_op.union(first_list, second_list)
        self.assertEqual(union_result.size(), 5)
        self.assertEqual(str(union_result), "1 -> 2 -> 3 -> 6 -> 8")

    def test_union_with_two_nonempty_list(self):
        first_list = self._create_linked_list([1, 2, 3, 6, 8])
        second_list = self._create_linked_list([9, 10])
        linked_list_op = LinkedListOp()
        union_result = linked_list_op.union(first_list, second_list)
        self.assertEqual(union_result.size(), 7)
        self.assertEqual(str(union_result), "1 -> 2 -> 3 -> 6 -> 8 -> 9 -> 10")

    def test_union_with_two_lists_having_common_elements(self):
        first_list = self._create_linked_list([1, 2, 3, 6, 8])
        second_list = self._create_linked_list([3, 1, 9, 10])
        linked_list_op = LinkedListOp()
        union_result = linked_list_op.union(first_list, second_list)
        self.assertEqual(union_result.size(), 7)
        self.assertEqual(str(union_result), "1 -> 2 -> 3 -> 6 -> 8 -> 9 -> 10")

    def test_union_with_two_lists_having_duplicate_elements_in_first_list(self):
        first_list = self._create_linked_list([1, 2, 3, 6, 8, 2])
        second_list = self._create_linked_list([3, 1, 9, 10])
        linked_list_op = LinkedListOp()
        union_result = linked_list_op.union(first_list, second_list)
        self.assertEqual(union_result.size(), 7)
        self.assertEqual(str(union_result), "1 -> 2 -> 3 -> 6 -> 8 -> 9 -> 10")

    def _create_linked_list(self, values_list):
        llist = LinkedList()
        for i in values_list:
            llist.append(i)
        return llist

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)