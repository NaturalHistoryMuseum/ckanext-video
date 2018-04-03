#!/usr/bin/env python
# encoding: utf-8
#
# This file is part of ckanext-video
# Created by the Natural History Museum in London, UK

import paste.fixture

import ckan.tests as tests
from ckan import model, plugins
from ckan.lib import create_test_data
from ckan.plugins import toolkit


class TestVideoView(tests.WsgiAppCase):
    ''' '''

    @classmethod
    def setup_class(cls):
        ''' '''

        cls.config_templates = toolkit.config[u'ckan.legacy_templates']
        toolkit.config[u'ckan.legacy_templates'] = u'false'
        wsgiapp = toolkit.middleware.make_app(toolkit.config[u'global_conf'],
                                              **toolkit.config)
        cls.app = paste.fixture.TestApp(wsgiapp)

        plugins.load(u'video_view')

        create_test_data.CreateTestData.create()

        context = {
            u'model': model,
            u'session': model.Session,
            u'user': model.User.get(u'testsysadmin').name
            }
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
        cls.resource_view = toolkit.get_action(u'resource_view_create')(context,
                                                                        cls.resource_view)

    @classmethod
    def teardown_class(cls):
        ''' '''
        toolkit.config[u'ckan.legacy_templates'] = cls.config_templates
        model.repo.rebuild_db()

    def test_video_is_shown(self):
        ''' '''
        url = toolkit.url_for(controller=u'package', action=u'resource_read',
                              id=self.package.name, resource_id=self.resource_id)
        result = self.app.get(url)
        assert self.resource_view[u'video_url'] in result

    def test_title_description_iframe_shown(self):
        ''' '''
        url = toolkit.url_for(controller=u'package', action=u'resource_read',
                              id=self.package.name, resource_id=self.resource_id)
        result = self.app.get(url)
        assert self.resource_view[u'title'] in result
        assert self.resource_view[u'description'] in result
        assert u'iframe' in result.body

    def test_iframe_attributes(self):
        ''' '''
        url = toolkit.url_for(controller=u'package', action=u'resource_read',
                              id=self.package.name, resource_id=self.resource_id)
        result = self.app.get(url)
        assert u'width="%s"' % self.resource_view[u'width'] in result
        assert u'height="%s"' % self.resource_view[u'height'] in result
