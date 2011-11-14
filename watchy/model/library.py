"""Library."""

import os


class Library(object):
    """Library class, will hold the collection of media."""

    def __init__(self):
        self.directories = {}
        self.files = {}

    def _registerDirectory(self, path):
        """Register directory."""

        if path in self.directories:
            return

        self.directories[path] = os.path.getmtime(path)

    def _addFile(self, path)
        """Add file to library."""


    def add(self, path):
        """Add the directory to the collection."""
        dirname = os.path.dirname(path)
        self._registerDirectory(dirname)


class MovieLibrary(Library):
    """Move Library."""

    def __init__(self, *args, **kwargs):
        super(MovieLibrary, self).__init__(*args, **kwargs)
