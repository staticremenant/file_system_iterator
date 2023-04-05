import os
import re


class FileSystemIterator:
    def __init__(self, root: str, only_files=False, only_dirs=False, pattern=None):
        if only_files is True and only_dirs is True:
            raise ValueError("Params 'only_files' and 'only_dirs' can't both be True")
        self.root = root
        self.only_files = only_files
        self.only_dirs = only_dirs
        self.pattern = pattern

        def gen():
            for path, _, files in os.walk(self.root):
                if not self.only_files:
                    yield path
                if not self.only_dirs:
                    for file in files:
                        yield os.path.join(path, file)

        self.__it = (it for it in gen() if self.pattern is None or re.search(self.pattern, it))

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.__it)
