#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup.py file for username"""

from setuptools import setup, find_packages

DESCRIPTION = 'Get the current username'
LONG_DESCRIPTION = open("readme.md").read()

VERSION = '2.1.0'
URL = 'https://projects.abranhe.com/username'
GITHUB_URL = 'https://github.com/abranhe/lupe'

setup(
    name='username',
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',

    url=URL,
    project_urls={'Source': GITHUB_URL},

    author='Abraham Hernandez',
    author_email='abraham@abranhe.com',
    license='MIT',

    classifiers=[
        'Programming Language :: Python',
        'Natural Language :: English',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Operating System :: OS Independent',
        'Operating System :: MacOS',
        'Operating System :: Unix',
    ],


		packages=find_packages(),
    keywords='cli command-line-interface python bash-tool username',
)
