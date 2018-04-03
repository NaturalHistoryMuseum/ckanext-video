#!/usr/bin/env python
# encoding: utf-8
#
# This file is part of ckanext-video
# Created by the Natural History Museum in London, UK

import paste.fixture
import pylons.config as config
import urlparse

import ckan.model as model
import ckan.tests as tests
import ckan.plugins as plugins
import ckan.lib.helpers as h
import ckanext.pdfview.plugin as plugin
import ckan.lib.create_test_data as create_test_data
import ckan.config.middleware as middleware


class TestVideoView(tests.WsgiAppCase):
    ''' '''

    @classmethod
    def setup_class(cls):
        ''' '''

        cls.config_templates = config[u'ckan.legacy_templates']
        config[u'ckan.legacy_templates'] = u'false'
        wsgiapp = middleware.make_app(config[u'global_conf'], **config)
        cls.app = paste.fixture.TestApp(wsgiapp)

        plugins.load(u'video_view')

        create_test_data.CreateTestData.create()

        context = {u'model': model,
                   u'session': model.Session,
                   u'user': model.User.get(u'testsysadmin').name}
        #
        cls.package = model.Package.get(u'annakarenina')
        cls.resource_id = cls.package.resources[1].id
        cls.resource_view = {
            u'resource_id': cls.resource_id,
            u'view_type': u'video',
            u'title': u'Test View',
            u'description': u'A nice test view',
            u'height': 400,
            u'width': 400,
            u'video_url': u'https://www.youtube.com/embed/-voP-V7YcqA'
        }
        cls.resource_view = plugins.toolkit.get_action(u'resource_view_create')(context, cls.resource_view)

    @classmethod
    def teardown_class(cls):
        ''' '''
        config[u'ckan.legacy_templates'] = cls.config_templates
        model.repo.rebuild_db()

    def test_video_is_shown(self):
        ''' '''
        url = h.url_for(controller=u'package', action=u'resource_read', id=self.package.name, resource_id=self.resource_id)
        result = self.app.get(url)
        assert self.resource_view[u'video_url'] in result

    def test_title_description_iframe_shown(self):
        ''' '''
        url = h.url_for(controller=u'package', action=u'resource_read', id=self.package.name, resource_id=self.resource_id)
        result = self.app.get(url)
        assert self.resource_view[u'title'] in result
        assert self.resource_view[u'description'] in result
        assert u'iframe' in result.body

    def test_iframe_attributes(self):
        ''' '''
        url = h.url_for(controller=u'package', action=u'resource_read', id=self.package.name, resource_id=self.resource_id)
        result = self.app.get(url)
        assert u'width="%s"' % self.resource_view[u'width'] in result
        assert u'height="%s"' % self.resource_view[u'height'] in result
