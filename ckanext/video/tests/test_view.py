#!/usr/bin/env python
# encoding: utf-8
#
# This file is part of ckanext-video
# Created by the Natural History Museum in London, UK

import ckantest.helpers
from ckantest.models import TestBase

from ckan.plugins import toolkit


class TestVideoView(TestBase):
    plugins = [u'video', u'datastore', u'resource_proxy']

    @classmethod
    def setup_class(cls):
        cls.config_templates = toolkit.config[u'ckan.legacy_templates']
        toolkit.config[u'ckan.legacy_templates'] = u'false'
        super(TestVideoView, cls).setup_class()
        cls._package = cls.data_factory().public_records
        cls._resource = cls._package[u'resources'][0]
        cls.resource_view = {
            u'resource_id': cls._resource[u'id'],
            u'view_type': u'video',
            u'title': u'Test View',
            u'description': u'A nice test view',
            u'height': 400,
            u'width': 400,
            u'video_url': u'https://www.youtube.com/embed/-voP-V7YcqA'
            }
        cls.resource_view = toolkit.get_action(u'resource_view_create')(cls.data_factory().context,
                                                                        cls.resource_view)

    @classmethod
    def teardown_class(cls):
        super(TestVideoView, cls).teardown_class()
        toolkit.config[u'ckan.legacy_templates'] = cls.config_templates

    def test_video_is_shown(self):
        ''' '''
        url = ckantest.helpers.routes.resource_read(self._package,
                                                    self._resource)
        result = self.app.get(url)
        assert self.resource_view[u'video_url'] in result

    def test_title_description_iframe_shown(self):
        ''' '''
        url = ckantest.helpers.routes.resource_read(self._package,
                                                    self._resource)
        result = self.app.get(url)
        assert self.resource_view[u'title'] in result
        assert self.resource_view[u'description'] in result
        assert u'iframe' in result.unicode_body

    def test_iframe_attributes(self):
        ''' '''
        url = ckantest.helpers.routes.resource_read(self._package,
                                                    self._resource)
        result = self.app.get(url)
        assert u'width="%s"' % self.resource_view[u'width'] in result
        assert u'height="%s"' % self.resource_view[u'height'] in result
