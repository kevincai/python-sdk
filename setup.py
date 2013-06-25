#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

PACKAGE = 'qiniu'
NAME = 'qiniu'
DESCRIPTION = 'Qiniu Resource (Cloud) Storage SDK for Python 2.X.'
LONG_DESCRIPTION = 'see:\nhttps://github.com/qiniu/python-sdk\n'
AUTHOR = 'Shanghai Qiniu Information Technologies Co., Ltd.'
AUTHOR_EMAIL = 'fengliyuan@qiniu.com'
URL = 'https://github.com/qiniu/python-sdk'
VERSION = __import__(PACKAGE).__version__


setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license='MIT',
    url=URL,
    packages=['qiniu'],
    platforms='any',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    test_suite = 'nose.collector'
)
