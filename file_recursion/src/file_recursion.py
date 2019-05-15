import os

class FileRecursion:
    """
    Method to find file with a given suffix
    Arguments:
        suffix   : File extension e.g. .c
        path     : File path to be search for file with given suffix. File path can be a regular file as well
        file_list: Result set returned
    """
    @staticmethod
    def _find_files(suffix, path, file_list):
        # Base case for recursion
        if path is None:
            return
        # If the given path is not a directory but a file
        if os.path.isfile(path):
            # Check if the file ends with required suffix
            if path.endswith(suffix):
                # Add it to the list of results if the file has the suffix
                file_list.append(path)
            else:
                return
        else:
            # If the path is a directory then for every entry in directory recurse
            for content in os.listdir(path):
                FileRecursion._find_files(suffix, os.path.join(path, content), file_list)


    """
    Externally exposed method for finding file(s) with given suffix 
    """
    @staticmethod
    def find_files(suffix, path):
        file_list = []
        FileRecursion._find_files(suffix, path, file_list)
        return file_list
    
        

