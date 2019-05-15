import unittest
import mock
import sys

sys.path.append('./src')
import file_recursion

class TestFileRecursion(unittest.TestCase):

    # Path name is a regular file not having the suffix
    @mock.patch('file_recursion.os.path.isfile')
    def test_find_file_when_path_single_file_without_matching_suffix(self, mock_isfile):
        mock_isfile.return_value = True
        self.assertEqual(file_recursion.FileRecursion.find_files('.c', '/users/foo/a.txt'), [])
        self.assertEqual(mock_isfile.call_count, 1)
        mock_isfile.called_with('/users/foo/a.txt')

    # Path name is a regular file having the suffix
    @mock.patch('file_recursion.os.path.isfile')
    def test_find_file_when_path_is_single_file_with_matching_suffix(self, mock_isfile):
        mock_isfile.return_value = True
        self.assertEqual(file_recursion.FileRecursion.find_files('.c', '/users/foo/a.c'), ['/users/foo/a.c'])
        self.assertEqual(mock_isfile.call_count, 1)
        mock_isfile.called_with('/users/foo/a.c')

    # Path name is null
    @mock.patch('file_recursion.os.path.isfile')
    def test_find_file_when_path_is_null(self, mock_isfile):
        self.assertEqual(file_recursion.FileRecursion.find_files('.c', None), [])
        self.assertEqual(mock_isfile.call_count, 0)

    # Path name is a directory with subdirectories
    #
    # /top_dir ----> dir1 -----> a.c
    #    |             |-------> b.c
    # .  |---------> dir2 -----> e.txt
    # top_dir has two directroies 'dir1' & 'dir2'
    # 'dir1' has two matching files - a.c & b.c
    # 'dir2' has a file but suffix of that file doesn't match
    #
    @mock.patch('file_recursion.os.path.isfile')
    @mock.patch('file_recursion.os.listdir')
    def test_find_file_when_multiple_files_with_suffix_found(self, mock_listdir, mock_isfile):
        mock_isfile.side_effect = (False, False, True, True, False, True)
        mock_listdir.side_effect = (['dir1', 'dir2'], ['a.c', 'b.c'], ['e.txt'])
        self.assertEqual(file_recursion.FileRecursion.find_files('.c', '/top_dir'), ['/top_dir/dir1/a.c', '/top_dir/dir1/b.c'])
        self.assertEqual(mock_isfile.call_count, 6)
        self.assertEqual(mock_listdir.call_count, 3)
        mock_isfile.called_with('/top_dir', '/top_dir/dir1', '/top_dir/dir1/a.c', '/top_dir/dir1/b.c', '/top_dir/dir2', '/top_dir/dir2/e.txt')

if __name__ == '__main__':
#    unittest.main(argv=['first-arg-is-ignored'], exit=False)
    unittest.main()


