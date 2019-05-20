
# Introduction

The goal is to write code for finding all files under a directory (and all directories beneath it) that end with ".c"

## Directory organization

There are two directories. 
1. `src` - contains the source code for recursive traversal
2. `test` - contains the unit test cases. As it uses system call like `os.path.isfile`, these calls are mocked using Python's mock module.

There is Jupyter notebook under `src` folder that combines Python class file(s) and its unit tests.

## Execution

To execute the code from command line, following steps are needed.

1. `cd <directory where code is checked out>/file_recursion`
2. `PYTHONPATH=src python test/test_file_recursion.py`


## Code design

File recusion involves two methods. Both methods are defined as `static method` since they don't need creation of the instance of object.

1. `find_files`: This is the public method which takes the path name and file extension as two input parameters and invokes a private method
2. `_find_files`: This is the privat method which takes two parameters described above along-with an additional parameter which is used as an accumulator to collect all files that satisfy the given file extension.

The script uses recursion. Base conditions are 

- The path is none in which case there is nothing to be done
- The path can be a regular file. In this case we check whether the file has the given extension. If the file has the extension then the complete path is appended to the list. Otherwise there is no action

## Efficiency

### Time efficiency

the method `find_files` needs to examine every node of the directory tree. So if there are n entries counting all directories ans sub directories from top level (counting recursively), time complexity will be O(n)

### Space Complexity

Every recursive call require creating an entry in the stack. In a most degenerate case let us assume that one top level directory has one sub directory which has another sub directory and so on .. till the last directory which has one file. Assuming a total of n entries, number of directories + sub directories = (n - 1) That will require O(n - 1) ~ O(n) stack entries.

Similarly the accumulator to preserve all matches will require additional storage. If we assume a top level directory having (n - 1) files below it with each of them having the given suffix then the list will have size ~O(n)

