"""Model.

Author: Ziling Zhao <zilingzhao@gmail.com>
"""

from watchy import filetypes

class Media(object):
    """Base media object."""

    def __init__(self, title=None):
        self.title = title

        # TODO: need to implement some title cleaner
        self.clean_title = None

    def __str__(self):
        return self.title


class Video(Media):
    """Video based media file."""

    def __init__(self, *args, **kwargs):
        super(Video, self).__init__(*args, **kwargs)

        # use a list for files to allow a media file to be split into
        # multiple parts
        self.files = []

    def addFile(self, path):
        """Add a file to this video."""
        self.files.append(filetypes.WrapVideoFile(path))

    def __str__(self):
        return '{0}: {1}'.format(
                self.title,
                ', '.join(str(f) for f in self.files)
                )


class Movie(Video):
    """Movie."""

    def __init__(self, *args, **kwargs):
        super(Movie, self).__init__(*args, **kwargs)
        self.metadata_file = None

    def __str__(self):
        return 'Movie: {0}'.format(super(Movie, self).__str__())


# vim: expandtab ts=4 sw=4 tw=80:
