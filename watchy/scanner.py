"""Scanner related components.

Scan/build collection.

Author: Ziling Zhao <zilingzhao@gmail.com>
"""

import os

from watchy import config


class Scanner(object):
    """Scan file system for files."""

    def __init__(self, library):
        """Scan given root for files.
        """

        self._library = library

    def scan(self, path):
        """Scan directory."""

        path = os.path.expanduser(path)
        if not os.path.isdir(path):
            raise IOError('Given path does not exist')

        self._library.root_dirs.add(path)

        for root, dirs, files in os.walk(path, followlinks=True):
            for f in files:
                path = os.path.join(root, f)
                self._library.add(path)


# vim: expandtab ts=4 sw=4 tw=80:
