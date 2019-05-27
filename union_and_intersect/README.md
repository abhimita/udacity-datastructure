# Introduction

The union of two sets A and B is the set of elements which are in A, in B, or in both A and B. The intersection of two sets A and B, denoted by <a href="https://www.codecogs.com/eqnedit.php?latex=A\bigcap&space;B" target="_blank"><img src="https://latex.codecogs.com/svg.latex?A\bigcap&space;B" title="A\bigcap B" /></a>, is the set of all objects that are members of both the sets A and B.

The script takes two linked lists and return a linked list that is composed of either the union or intersection, respectively.

## Directory organization

There are two directories. 
1. `src` - contains the source code for union/intersection of linked lists
2. `test` - contains the unit test cases. 

## Execution

To execute the code from command line, following steps are needed.

1. `cd <directory where code is checked out>`
2. `PYTHONPATH=union_and_intersect/src python union_and_intersect/test/test_union_and_intersect.py`

### Output

test_intersection_with_common_elements (__main__.TestUnionIntersectionOperator) ... ok
test_intersection_with_no_common_elements (__main__.TestUnionIntersectionOperator) ... ok
test_intersection_with_one_empty_list (__main__.TestUnionIntersectionOperator) ... ok
test_union_with_one_empty_list (__main__.TestUnionIntersectionOperator) ... ok
test_union_with_two_lists_having_common_elements (__main__.TestUnionIntersectionOperator) ... ok
test_union_with_two_lists_having_duplicate_elements_in_first_list (__main__.TestUnionIntersectionOperator) ... ok
test_union_with_two_nonempty_list (__main__.TestUnionIntersectionOperator) ... ok

----------------------------------------------------------------------
Ran 7 tests in 0.001s

OK

## Code design

`UnionIntersectionOperator` class has two methods
1. `union`: This methods accepts two linked lists. As each linked list is traversed, nodes with `value` not seen before is added a dictionary and appended to the end of a newly created linked list. If such a node has been seen before then no action is needed. This way the dictionary helps eliminate the duplicate.

2. `intersection`: This method is similar to `union` operator but it needs to output node only when nodes with same `value` exist in both linked lists. Dictionary's `key` is the `value` coming from linked list node. Key of the dictionary references a tuple containing (reference to the actual node, index identifier of the linked list where this node is seen)

If the first linked list has duplicate elements, index identifier helps rejecting such node from being added to the new list.

## Efficiency

### Time efficiency

Assume the first linked list is of size m and the second one is of size n. Computing union requires traversing both linked lists result in O(m + n) complexity.

Intersect operator also requires traversing both lists. Overall complexity for this method is also O(m + n)

### Space Complexity

Both method requires a dictionary. In case none of the lists have no duplicate elements as well as has no elements in common then the dictionary size will be O(m + n). Also the return value in a new list of size O(m + n). Worst case complexity is O(m + n)

