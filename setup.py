#!/usr/bin/env python

from setuptools import setup, find_packages

from Kittens import __version__

setup(name='astro-kittens',
      version=__version__,
      description='Collection of Python utility functions for purr, tigger, meqtrees and others',
      author='Oleg Smirnov',
      author_email='Oleg Smirnov <osmirnov@gmail.com>',
      url='https://github.com/ska-sa/kittens',
      packages=find_packages(),
      install_requires=['future', 'astropy', 'configparser'],
      setup_requires=['pytest-runner'],
      tests_require=['pytest', 'mock'],
      test_suite="tests",
      license="GPL2",
      classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: System :: Operating System Kernels :: Linux",
        "Environment :: X11 Applications",
      ]
)
