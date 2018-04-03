#!/usr/bin/env python

from distutils.core import setup

setup(name='Song Recogniser',
      version='1.0',
      description='It can memorise songs',
      author='S M Ahasanul Haque',
      author_email='ahsanul.haque.ovi@gmail.com',
      url='https://github.com/Ahsanul08/song_recogniser',
      scripts=['song'],
      py_modules = ['config', 'export_db', 'import_db', 'new_song', 'start', 'utils'])
