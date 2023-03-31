import os
import re


class FileSystemIterator:
    def __init__(self, root: str, only_files=False, only_dirs=False, pattern=None):
        self.root = root
        self.only_files = only_files
        self.only_dirs = only_dirs
        self.pattern = pattern

    def __iter__(self):
        for path, _, files in os.walk(self.root):
            if not self.only_files:
                if self.pattern is None or re.search(self.pattern, path):
                    yield path
            if not self.only_dirs:
                for file in files:
                    full_path = os.path.join(path, file)
                    if self.pattern is None or re.search(self.pattern, full_path):
                        yield full_path

    def __next__(self):
        next(self.__iter__())
