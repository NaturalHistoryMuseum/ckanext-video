# !/usr/bin/env python
# encoding: utf-8
#
# This file is part of ckanext-video
# Created by the Natural History Museum in London, UK

video_provider_patterns = {
    u'vimeo': u'//player.vimeo.com/video/[0-9]+',  # Embedded vimeo link
    u'youtube_link': u'http[s]?://www.youtube.com/watch\?v=([0-9a-z/-]+)',
    # Link to you tube video page - () group to de-mark video ID
    u'youtube_embedded': u'http[s]?://www.youtube.com/embed/([0-9a-z/-]+)'
    # Embedded youtube video - () group to de-mark video ID
}
