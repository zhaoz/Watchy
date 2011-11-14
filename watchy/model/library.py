"""Library.

Author: Ziling Zhao <zilingzhao@gmail.com>
"""

import os

from watchy.model import types


class Library(object):
    """Library class, will hold the collection of media."""

    def __init__(self):
        self.directories = {}
        self.files = {}
        self.root_dirs = set()

    def _registerDirectory(self, path):
        """Register directory."""

        if path in self.directories:
            return

        self.directories[path] = os.path.getmtime(path)

    def _addFile(self, path):
        """Add file to library."""
        raise NotImplementedError

    def add(self, path):
        """Add the directory to the collection."""
        dirname = os.path.dirname(path)
        self._registerDirectory(dirname)
        self._addFile(path)


class MovieLibrary(Library):
    """Movie Library.

    This library makes the assumption that the directory structure is 
    ../movie_name/files
    """

    def __init__(self, *args, **kwargs):
        super(MovieLibrary, self).__init__(*args, **kwargs)

        # this will map movie names to movies
        self.movies = {}

    def _addFile(self, path):
        dir_path = os.path.dirname(path)
        movie_name = os.path.basename(dir_path)

        movie = self.movies.get('movie_name', None)

        if not movie:
            movie = types.Movie(movie_name)
            self.movies[movie_name] = movie

        movie.addFile(path)

    def __str__(self):
        return '\n'.join(str(m) for m in self.movies.itervalues())


# vim: expandtab ts=4 sw=4 tw=79:
