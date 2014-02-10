#!/usr/bin/python
# coding: utf-8

'''pdfmerge setup file'''

# Native
from setuptools import setup
import sys

# Package
import pdfmerge

IS_WINDOWS = sys.platform.startswith('win')


def get_deps(path):
    '''Parse requirements file.'''
    deps = []
    for line in open(path):
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        deps.append(line)
    return deps


OPTS = {
    'name': 'pdfmerge',
    'description': pdfmerge.__doc__.split('\n')[0],
    'long_description': pdfmerge.__doc__,

    'version': pdfmerge.__version__.replace('pre', ''),
    'py_modules': ['pdfmerge'],
    'provides': ['pdfmerge'],

    'install_requires': get_deps('requirements.txt'),
    'scripts': ['scripts/pdfmerge'],
    'entry_points': {'console_scripts': ['pdfmerge = pdfmerge:main']},

    'author': pdfmerge.__author__,
    'author_email': pdfmerge.__email__,
    'license': pdfmerge.__license__,

    'url': 'https://github.com/metaist/pdfmerge',
    'download_url': 'https://github.com/metaist/pdfmerge',

    'keywords': 'pdf merge split',
    'classifiers': [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries'
    ]
}

if sys.version_info >= (3,):
    OPTS['use_2to3'] = True

if IS_WINDOWS:
    OPTS['scripts'] += [s + '.bat' for s in OPTS['scripts']]

    try:
        import py2exe
        OPTS['console'] = ['pdfmerge.py']
    except ImportError:
        print '''
NOTE: If you want to build a Windows executable, you need to download and
install py2exe from http://sourceforge.net/projects/py2exe/files/py2exe/0.6.9/
'''

setup(**OPTS)
