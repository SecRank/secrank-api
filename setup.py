#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

from secrank import __version__


DEPENDENCIES = open('requirements.txt', 'r', encoding='utf-8').read().split('\n')
README = open('README.rst', 'r', encoding='utf-8').read()

setup(
    name='secrank',
    version=__version__,
    description='Python library and command-line tool for SecRank (https://secrank.com)',
    long_description=README,
    long_description_content_type='text/x-rst',
    author='iliwoy',
    author_email='iliwoy@gmail.com',
    url='https://github.com/SecRank/secrank-api',
    packages=['secrank'],
    entry_points={'console_scripts': ['secrank=secrank.cli:main']},
    install_requires=DEPENDENCIES,
    keywords=['security tool', 'secrank', 'command tool'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
