#!/usr/bin/env python

from distutils.core import setup

setup(name='mediawikitools',
      version='1.2.0',
      description='Python package for interacting with a MediaWiki wiki',
      long_description = """A Python package for interacting with a MediaWiki wiki using the MediaWiki API.
Designed for MediaWiki version 1.16 and higher, should work on 1.13, older
versions may have bugs.
The edit-API must be enabled on the site to use editing features.
Please report any bugs to <http://code.google.com/p/python-wikitools/issues>""",
      author='Alex Z. (User:Mr.Z-man @ en.wikipedia)',
      author_email='mrzmanwiki@gmail.com',
      url='http://code.google.com/p/python-wikitools/',
      license='GPL v3',
      packages=['mediawikitools'],
     )
