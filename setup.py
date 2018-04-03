#!/usr/bin/env python
# encoding: utf-8
#
# This file is part of ckanext-video
# Created by the Natural History Museum in London, UK

from setuptools import find_packages, setup

version = u'0.2'

setup(
    name=u'ckanext-video',
    version=version,
    description=u'',
    long_description=u'',
    classifiers=[],
    # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords=u'',
    license=u'',
    packages=find_packages(exclude=[u'ez_setup', u'examples', u'tests']),
    namespace_packages=[u'ckanext', u'ckanext.video'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
        ],
    entry_points= \
        u'''
            [ckan.plugins]
                video = ckanext.video.plugin:VideoPlugin
        ''',
    )
