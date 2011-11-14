#!/usr/bin/python2

from watchy.scanner import Scanner
from watchy.model.library import MovieLibrary


lib = MovieLibrary()

scanner = Scanner(lib)

scanner.scan('./Movies')

print lib

