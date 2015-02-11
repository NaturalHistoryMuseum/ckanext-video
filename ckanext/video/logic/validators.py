#!/usr/bin/env python
# encoding: utf-8
"""
Created by 'bens3' on 2013-06-21.
Copyright (c) 2013 'bens3'. All rights reserved.
"""

from ckan.common import _
import ckan.lib.navl.dictization_functions as df
import re
from ckanext.video import video_provider_patterns

Invalid = df.Invalid
Missing = df.Missing


def is_valid_video_url(value, context):

    """Validate a URL is a valid video URL"""
    for pattern in video_provider_patterns.values():
        if re.search(pattern, value, re.IGNORECASE):
            return value

    raise Invalid(_('URL is not a valid video provider'))