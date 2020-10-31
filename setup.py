# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in comments/__init__.py
from comments import __version__ as version

setup(
	name='comments',
	version=version,
	description='Comments Flow ',
	author='Firsterp',
	author_email='support@firsterp.in',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
