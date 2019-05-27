import unittest
from union_and_intersect import UnionIntersectionOperator, LinkedList

class TestUnionIntersectionOperator(unittest.TestCase):
    def setUp(self):
        return UnionIntersectionOperator()

    def test_intersection_with_no_common_elements(self):
        first_list = self._create_linked_list([1, 2, 3, 4])
        second_list = self._create_linked_list([5, 6, 7, 8])
        union_intersection_operator = self.setUp()
        self.assertEqual(union_intersection_operator.intersection(first_list, second_list).head, None)

    def test_intersection_with_common_elements(self):
        first_list = self._create_linked_list([1, 2, 3, 6, 8])
        second_list = self._create_linked_list([5, 6, 7, 8])
        union_intersection_operator = self.setUp()
        intersect_result = union_intersection_operator.intersection(first_list, second_list)
        self.assertEqual(intersect_result.size(), 2)
        self.assertEqual(str(intersect_result), "6 -> 8")

    def test_intersection_with_one_empty_list(self):
        first_list = self._create_linked_list([1, 2, 3, 6, 8])
        second_list = self._create_linked_list([])
        union_intersection_operator = self.setUp()
        intersect_result = union_intersection_operator.intersection(first_list, second_list)
        self.assertEqual(intersect_result.size(), 0)
        self.assertEqual(str(intersect_result), "")

    def test_union_with_one_empty_list(self):
        first_list = self._create_linked_list([1, 2, 3, 6, 8])
        second_list = self._create_linked_list([])
        union_intersection_operator = self.setUp()
        union_result = union_intersection_operator.union(first_list, second_list)
        self.assertEqual(union_result.size(), 5)
        self.assertEqual(str(union_result), "1 -> 2 -> 3 -> 6 -> 8")

    def test_union_with_two_nonempty_list(self):
        first_list = self._create_linked_list([1, 2, 3, 6, 8])
        second_list = self._create_linked_list([9, 10])
        union_intersection_operator = self.setUp()
        union_result = union_intersection_operator.union(first_list, second_list)
        self.assertEqual(union_result.size(), 7)
        self.assertEqual(str(union_result), "1 -> 2 -> 3 -> 6 -> 8 -> 9 -> 10")

    def test_union_with_two_lists_having_common_elements(self):
        first_list = self._create_linked_list([1, 2, 3, 6, 8])
        second_list = self._create_linked_list([3, 1, 9, 10])
        union_intersection_operator = self.setUp()
        union_result = union_intersection_operator.union(first_list, second_list)
        self.assertEqual(union_result.size(), 7)
        self.assertEqual(str(union_result), "1 -> 2 -> 3 -> 6 -> 8 -> 9 -> 10")

    def test_union_with_two_lists_having_duplicate_elements_in_first_list(self):
        first_list = self._create_linked_list([1, 2, 3, 6, 8, 2])
        second_list = self._create_linked_list([3, 1, 9, 10])
        union_intersection_operator = self.setUp()
        union_result = union_intersection_operator.union(first_list, second_list)
        self.assertEqual(union_result.size(), 7)
        self.assertEqual(str(union_result), "1 -> 2 -> 3 -> 6 -> 8 -> 9 -> 10")

    def _create_linked_list(self, values_list):
        llist = LinkedList()
        for i in values_list:
            llist.append(i)
        return llist

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestUnionIntersectionOperator)
    unittest.TextTestRunner(verbosity=2).run(suite)
    # unittest.main(argv=['first-arg-is-ignored'], exit=False)