#!/usr/bin/env python
# encoding: utf-8
#
# This file is part of ckanext-video
# Created by the Natural History Museum in London, UK
import pytest
from ckan.plugins import toolkit
from ckan.tests import factories
from ckan.tests.helpers import call_action

VIDEO_URL = u'https://www.youtube.com/embed/-voP-V7YcqA'
TITLE = u'Test View'
DESCRIPTION = u'A nice test view'
WIDTH = 400
HEIGHT = 400


@pytest.fixture
def rendered_view(app):
    package = factories.Dataset()
    resource = factories.Resource(package_id=package[u'id'])
    data_dict = {
        u'resource_id': resource[u'id'],
        u'view_type': u'video',
        u'title': TITLE,
        u'description': DESCRIPTION,
        u'height': WIDTH,
        u'width': HEIGHT,
        u'video_url': VIDEO_URL,
    }
    call_action(u'resource_view_create', **data_dict)
    url = toolkit.url_for(u'resource.read', id=package[u'name'], resource_id=resource[u'id'])
    return app.get(url)


@pytest.mark.filterwarnings(u'ignore::sqlalchemy.exc.SADeprecationWarning')
@pytest.mark.ckan_config(u'ckan.plugins', u'video')
@pytest.mark.usefixtures(u'clean_db', u'with_plugins', u'with_request_context')
class TestVideoView(object):

    def test_video_is_shown(self, rendered_view):
        assert VIDEO_URL in rendered_view

    def test_title_description_iframe_shown(self, rendered_view):
        assert TITLE in rendered_view
        assert DESCRIPTION in rendered_view
        assert u'iframe' in rendered_view

    def test_iframe_attributes(self, rendered_view):
        assert u'width="{}"'.format(WIDTH) in rendered_view
        assert u'height="{}"'.format(HEIGHT) in rendered_view
