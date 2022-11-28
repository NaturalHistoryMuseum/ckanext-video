#!/usr/bin/env python
# encoding: utf-8
#
# This file is part of ckanext-video
# Created by the Natural History Museum in London, UK

import re

from ckan.plugins import toolkit
from ckanext.video.providers import video_provider_patterns


def is_valid_video_url(value, context):
    """
    Validate a URL is a valid video URL.

    :param value:
    :param context:
    """
    for pattern in video_provider_patterns.values():
        if re.search(pattern, value, re.IGNORECASE):
            return value

    raise toolkit.Invalid(toolkit._('URL is not a valid video provider'))
