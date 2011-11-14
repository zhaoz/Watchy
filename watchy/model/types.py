"""DB related stuff."""

class Media(object):
    """Base media object."""

    def __init__(self, title=None):
        self.title = title


class Video(Media):
    """Video based media file."""

    def __init__(self, *args, **kwargs):
        super(Video, self).__init__(*args, **kwargs)


class Movie(Video):
    """Movie."""

    def __init__(self, *args, **kwargs):
        super(Movie, self).__init__(*args, **kwargs)
