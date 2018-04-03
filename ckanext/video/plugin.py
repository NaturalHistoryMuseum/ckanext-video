#!/usr/bin/env python
# encoding: utf-8
#
# This file is part of ckanext-video
# Created by the Natural History Museum in London, UK

import logging

import re
from ckanext.video.logic.validators import is_valid_video_url
from ckanext.video.providers import video_provider_patterns

from ckan.plugins import SingletonPlugin, implements, interfaces, toolkit

log = logging.getLogger(__name__)
ignore_empty = toolkit.get_validator(u'ignore_empty')
not_empty = toolkit.get_validator(u'not_empty')
is_positive_integer = toolkit.get_validator(u'is_positive_integer')


class VideoPlugin(SingletonPlugin):
    '''Resource view for embedding videos (youtube/vimeo)'''

    implements(interfaces.IConfigurer, inherit=True)
    implements(interfaces.IResourceView, inherit=True)
    implements(interfaces.IPackageController, inherit=True)

    def update_config(self, config):
        '''

        :param config: 

        '''
        toolkit.add_template_directory(config, u'theme/templates')

    def info(self):
        ''' '''
        return {
            u'name': u'video',
            u'title': u'Embedded video',
            u'schema': {
                u'video_url': [ignore_empty, unicode, is_valid_video_url],
                u'width': [not_empty, is_positive_integer],
                u'height': [not_empty, is_positive_integer],
                },
            u'iframed': False,
            u'icon': u'film'
            }

    def can_view(self, data_dict):
        '''

        :param data_dict: 

        '''
        return True

    def view_template(self, context, data_dict):
        '''

        :param context: 
        :param data_dict: 

        '''
        return u'video_view.html'

    def form_template(self, context, data_dict):
        '''

        :param context: 
        :param data_dict: 

        '''
        return u'video_form.html'

    def setup_template_variables(self, context, data_dict):
        '''Setup variables available to templates

        :param context: 
        :param data_dict: 

        '''

        video_url = data_dict[u'resource_view'].get(u'video_url') or data_dict[
            u'resource'].get(u'url')

        # Is this a youtube video?
        if u'youtube.com' in video_url:
            # If this is a youtube link, replace with a URL for embeddable video
            match = re.search(video_provider_patterns[u'youtube_link'], video_url,
                              re.IGNORECASE)
            if match:
                video_url = u'https://www.youtube.com/embed/%s' % match.group(1)

        # TODO - More video provider types

        return {
            u'defaults': {
                u'width': 480,
                u'height': 390
                },
            u'video_url': video_url
            }
