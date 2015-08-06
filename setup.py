#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

version = '0.1.1'
long_description = '\n'.join([
    open('README.rst').read(),
    open('AUTHORS.rst').read(),
    open('HISTORY.rst').read(),
    ])

classifiers = [
    'Development Status :: 4 - Beta',
    'Environment :: Plugins',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
]

setup(
    name='pygments-style-jellywrd',
    version=version,
    description=('Pygments jellywrd style '
                 '(from vim jellywrd colorscheme via vim2vim)'),
    long_description=long_description,
    classifiers=classifiers,
    keywords=['pygments', 'style', 'light', 'dark', 'syntax highlighting'],
    author='Wes Turner',
    author_email='wes@wrd.nu',
    url='https://github.com/westurner/pygments-style-jellywrd',
    license='MIT',
    packages=find_packages(),
    install_requires=['pygments >= 1.5'],
    entry_points="""
        [pygments.styles]
        jellywrd=pygments_style_jellywrd.jellywrd:JellywrdStyle
    """,
    zip_safe=False,
)
