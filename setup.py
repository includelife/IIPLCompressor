# -*- coding: utf-8 -*-
from distutils.core import setup
import py2exe
import numpy


setup(
	windows=[{"script":"IIPLCompressor.py",'icon_resources':[(1,'iipl.ico')]}],
	data_files=['optipng.exe','iipl.ico']
	# options = {"py2exe": {"bundle_files":"1"}}

	)
