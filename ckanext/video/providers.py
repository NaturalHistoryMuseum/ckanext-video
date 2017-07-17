#!/usr/bin/env python
# encoding: utf-8
"""
Created by Ben Scott on '17/07/2017'.
"""

# Dictionary of allowable video provider patterns
video_provider_patterns = {
    'vimeo':  '//player.vimeo.com/video/[0-9]+',  # Embedded vimeo link
    'youtube_link':  'http[s]?:\/\/www.youtube.com\/watch\?v=([0-9a-z/-]+)',  # Link to you tube video page - () group to de-mark video ID
    'youtube_embedded': 'http[s]?:\/\/www.youtube.com\/embed\/([0-9a-z/-]+)'  # Embedded youtube video - () group to de-mark video ID
}