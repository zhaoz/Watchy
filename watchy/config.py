"""Configuration stuff.

Author: Ziling Zhao <zilingzhao@gmail.com>
"""

from collections import MutableMapping
import os

class _Config(MutableMapping):
    """Config holder.

    A Config class that emulates a dict for use in loading, config items are
    accessible via standard getattr type access for ease of use.

    """
    def __init__(self):
        self._dict = {}

    def __len__(self):
        return len(self._dict)

    def __iter__(self):
        return self._dict.__iter__()

    def __getitem__(self, key):
        return self._dict.__getitem__(key)

    def __setitem__(self, key, value):
        return self._dict.__setitem__(key, value)

    def __delitem__(self, key):
        return self._dict.__delitem__(key)

    def __getattr__(self, key):
        return self._dict[key]


class _ConfigLoader(object):
    """Config loader.

    Takes python config files, and updates a _Config object.
    """

    DEFAULT_CONFIGS = ['/etc/watchy', '~/.config/watchy']

    def __init__(self, config, extra_paths=None):
        self.paths = self.DEFAULT_CONFIGS[:]
        self.paths.extend(extra_paths or [])

        self._config = config

    def load(self):
        for f in self.paths:
            f = os.path.expanduser(f)
            if os.path.isfile(f):
                execfile(f, globals(), self._config)


config = _Config()
_config = _ConfigLoader(config)
_config.load()


# vim: expandtab ts=4 sw=4 tw=79:
