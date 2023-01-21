# !/usr/bin/env python
# encoding: utf-8
#
# This file is part of ckanext-video
# Created by the Natural History Museum in London, UK

video_provider_patterns = {
    'vimeo': r'//player.vimeo.com/video/[0-9]+',  # Embedded vimeo link
    'youtube_link': r'https?://www.youtube.com/watch\?v=([0-9a-z/-]+)',
    'youtube_embedded': r'https://www.youtube.com/embed/([0-9a-z/-]+)',
    'youtube_shortened': r'https://youtu.be/([0-9a-z/-]+)'
}
