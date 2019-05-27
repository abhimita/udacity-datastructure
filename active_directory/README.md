# Introduction

In Windows Active Directory, a group can consist of user(s) and group(s) themselves. User is represented by `id`. `Group` is represented as a Python class. Instance variable `groups` is a list data type and contains reference to other groups which are members of this group. Similarly instance variable `users` is a list data type and contains the list of user ids which belong to this class.

Here we implement to a function which determines an efficient lookup to determine whether user is a member of a given group.

## Directory organization

There are two directories. 
1. `src` - contains the source code for active directory searching
2. `test` - contains the unit test cases. 

## Execution

To execute the code from command line, following steps are needed.

1. `cd <directory where code is checked out>/active_directory`
2. `PYTHONPATH=src python test/test_groups.py`


## Code design

A group can contain member groups which in turn can contain other groups. An user can belong to a group directory or it can have membership transitively. To find whether user belongs to a group directly or indirectly, requires recursive traversal. That will not result in efficient lookup. To minimize that, `init` method of the class `MembershipFinder` builds data structure which helps in that look up process.

Here we are using a modified version of union-find algorithm without path compression. First users and groups are treated as objects and given an internal `id` starting from 0. Ordering of this id generation doesn't have any meaning. 

Let us assume the following relationship among the groups and users

<pre>
group-1----> group-2 -----> user-2
               |----------> user-3
  |--------> group-3
  |--------> user-1
  
</pre>
  
After `id` generation step:

<pre>
+--------+---+
|group-1 | 0 |
|group-2 | 1 |
|group-3 | 2 |
|user-1  | 3 |
|user-2  | 4 |
|user-3  | 5 |
+--------+---+
</pre>

Initially all groups and users are disjoint. That means there is no relationship among them. This is represented as: 


List: `data`

<pre>
 Group-1 Group-2 Group-3 User-1  User-2   User-3
+-------+-------+-------+-------+-------+-------+
|   0   |   1   |   2   |   3   |   4   |   5   |
+-------+-------+-------+-------+-------+-------+
    0       1       2       3       4       5     <--- Index of the list
    
</pre>
    
Without any association, each entry in the above list means that it is a parent of itself. That changes as we go through each group associations.

First association shows that group-2 (index = 1) is a child group of group-1 (index = 0). So content of `data[1]` is changed to: `data[1] = 0`

Next association shows that `user-2` (index = 4) belongs to `group-2` (index = 1). So content of `data[4]` si changed to: `data[4] = 1`

When all associations are processed then list: `data` looks like following:

<pre>

 Group-1 Group-2 Group-3 User-1  User-2   User-3
+-------+-------+-------+-------+-------+-------+
|   0   |   0   |   0   |   0   |   1   |   1   |
+-------+-------+-------+-------+-------+-------+
    0       1       2       3       4       5     <--- Index of the list
    
</pre>

Now to check membership of an user in a group, a dictionary is build for every `user` in the above list. For example - `user - 1` is in `index = 3` and `data[3] = 0`. Next `index = 0` is access which is for `Group-1`. A dictionary is entry is made for `(user-1, group-1)`

Let us walk through another example for `user-2` at `index = 4`. `data[4] = 1` next `index = 1` is accessed resulting a new entry in the dictionary as `(user-2, group-2)`. This process continues till we hit a position in the list where `index == data[index]`. That happens when `data[1]` which is `0` is used to access `data[0]`.

## Efficiency

### Time efficiency

There is some overhead to build the final dictionary which is stored in instance variable `self.user_group_map`. But this is built only once during initialization step. The actual lookup results in time complexity of O(1) given user & group.

### Space Complexity

Storage arises from the need to store the dictionary with combined key of `(user, group)`. To estimate the size of the dictionary assume that there are `m` groups and `n` users with each group having `p` on an average. Each group can be considered as a node of a `p-ary` tree. Assumming the tree is full, all groups will be inner nodes while nodes for `user` will be leaf node. The depth of the tree will be - <a href="https://www.codecogs.com/eqnedit.php?latex=log_{p}m" target="_blank"><img src="https://latex.codecogs.com/svg.latex?log_{p}m" title="log_{p}m" /></a>

Total storage requirement for the dictionary will be <a href="https://www.codecogs.com/eqnedit.php?latex=nlog_{p}m" target="_blank"><img src="https://latex.codecogs.com/svg.latex?nlog_{p}m" title="nlog_{p}m" /></a>

Storage complexity will be <a href="https://www.codecogs.com/eqnedit.php?latex=O(nlog_{p}m)" target="_blank"><img src="https://latex.codecogs.com/svg.latex?O(nlog_{p}m)" title="O(nlog_{p}m)" /></a>
