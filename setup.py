#!/usr/bin/python
# coding: utf-8

from distutils.core import setup

import pdfmerge

setup(
    name='pdfmerge',
    version=pdfmerge.__version__,
    author=pdfmerge.__author__,
    author_email=pdfmerge.__email__,
    url='https://github.com/metaist/pdfmerge',
    download_url='https://github.com/metaist/pdfmerge',
    description=pdfmerge.__doc__.split('\n')[0],
    long_description=pdfmerge.__doc__,
    py_modules=['pdfmerge'],
    keywords='pdf merge',
    license=blogit.__license__,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries'
    ]
)
