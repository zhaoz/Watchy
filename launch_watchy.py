#!/usr/bin/python2

from watchy.scanner import Librarian
from watchy.library import MovieLibrary


lib = MovieLibrary()

librarian = Librarian('~/Movies/Movies', lib)

librarian.scan()

