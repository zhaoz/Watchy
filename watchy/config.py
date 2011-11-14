"""Configuration stuff."""
from collections import MutableMapping
import os

class Config(MutableMapping):
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


config = Config()


class _ConfigLoader(object):

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


_config = _ConfigLoader(config)
_config.load()
