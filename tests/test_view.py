#!/usr/bin/env python
# encoding: utf-8
#
# This file is part of ckanext-video
# Created by the Natural History Museum in London, UK
import pytest
from ckan.plugins import toolkit
from ckan.tests import factories
from ckan.tests.helpers import call_action

VIDEO_URL = 'https://www.youtube.com/embed/-voP-V7YcqA'
TITLE = 'Test View'
DESCRIPTION = 'A nice test view'
WIDTH = 400
HEIGHT = 400


@pytest.fixture
def rendered_view(app):
    package = factories.Dataset()
    resource = factories.Resource(package_id=package['id'])
    data_dict = {
        'resource_id': resource['id'],
        'view_type': 'video',
        'title': TITLE,
        'description': DESCRIPTION,
        'height': WIDTH,
        'width': HEIGHT,
        'video_url': VIDEO_URL,
    }
    call_action('resource_view_create', **data_dict)
    url = toolkit.url_for(
        'resource.read', id=package['name'], resource_id=resource['id']
    )
    return app.get(url)


@pytest.mark.filterwarnings('ignore::sqlalchemy.exc.SADeprecationWarning')
@pytest.mark.ckan_config('ckan.plugins', 'video')
@pytest.mark.usefixtures('clean_db', 'with_plugins', 'with_request_context')
class TestVideoView(object):
    def test_video_is_shown(self, rendered_view):
        assert VIDEO_URL in rendered_view

    def test_title_description_iframe_shown(self, rendered_view):
        assert TITLE in rendered_view
        assert DESCRIPTION in rendered_view
        assert 'iframe' in rendered_view

    def test_iframe_attributes(self, rendered_view):
        assert f'width="{WIDTH}"' in rendered_view
        assert f'height="{HEIGHT}"' in rendered_view
