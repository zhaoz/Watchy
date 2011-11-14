"""Wrappers around files.

Author: Ziling Zhao <zilingzhao@gmail.com>
"""

import mimetypes

from watchy import UnknownFileTypeException


class VideoFile(object):
    """A single video file."""

    def __init__(self, path):
        # check and see if this is a known media file
        self.path = path
    
    def __str__(self):
        return self.path


class AVIVideoFile(VideoFile):
    """An .avi video file."""


class MKVVideoFile(VideoFile):
    """A .mkv video file."""


_VIDEO_EXT_TO_CLASS = {
        'avi': AVIVideoFile,
        'mkv': MKVVideoFile
        }

_VIDEO_TYPE_TO_CLASS = {
        'video/x-msvideo': AVIVideoFile
    }


def WrapVideoFile(path):
    """Detect the type of file and return an object for it."""

    ext = path.split('.')[-1]

    cls = _VIDEO_EXT_TO_CLASS.get(ext, None)

    if not cls:
        # try mimetypes
        mtype = mimetypes.guess_type(path)[0]
        cls = _VIDEO_TYPE_TO_CLASS.get(mtype, None)

    if not cls:
        raise UnknownFileTypeException(
                'File "{0}" cannot be handled.'.format(path))

    return cls(path)


# vim: expandtab ts=4 sw=4 tw=80:
