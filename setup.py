#!/usr/bin/env python
# encoding: utf-8
#
# This file is part of ckanext-video
# Created by the Natural History Museum in London, UK

from setuptools import find_packages, setup

__version__ = '2.0.0'

with open('README.md', 'r') as f:
    __long_description__ = f.read()

setup(
    name='ckanext-video',
    version=__version__,
    description='A CKAN extension for embedding Youtube or Vimeo videos as views.',
    long_description=__long_description__,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    keywords='CKAN data video',
    author='Natural History Museum',
    author_email='data@nhm.ac.uk',
    url='https://github.com/NaturalHistoryMuseum/ckanext-video',
    license='GNU GPLv3',
    packages=find_packages(exclude=['tests']),
    namespace_packages=['ckanext', 'ckanext.video'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[],
    entry_points= \
        '''
        [ckan.plugins]
            video=ckanext.video.plugin:VideoPlugin
        ''',
)
