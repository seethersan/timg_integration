# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in timg_integration/__init__.py
from timg_integration import __version__ as version

setup(
	name='timg_integration',
	version=version,
	description='App for Integration with TIMG systems',
	author='seethersan',
	author_email='carlos_jcez@hotmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
