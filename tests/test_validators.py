import pytest
from ckan.plugins import toolkit
from ckanext.video.logic.validators import is_valid_video_url
from mock import MagicMock


class TestValidVideoURL(object):
    def test_vimeo_valid(self):
        assert is_valid_video_url(
            'https://player.vimeo.com/video/459651092', MagicMock()
        )
        assert is_valid_video_url('//player.vimeo.com/video/459651092', MagicMock())

    def test_vimeo_invalid(self):
        with pytest.raises(toolkit.Invalid):
            is_valid_video_url('https://player.vimeo.com/video/', MagicMock())
        with pytest.raises(toolkit.Invalid):
            is_valid_video_url('https://vimeo.com/459651092', MagicMock())

    def test_youtube_valid(self):
        assert is_valid_video_url(
            'https://www.youtube.com/watch?v=-voP-V7YcqA', MagicMock()
        )

    def test_youtube_invalid(self):
        with pytest.raises(toolkit.Invalid):
            is_valid_video_url('https://www.youtube.com/watch?x=beans', MagicMock())
        with pytest.raises(toolkit.Invalid):
            is_valid_video_url('https://www.youtube.com/watch?v=', MagicMock())

    def test_youtube_embed_valid(self):
        assert is_valid_video_url(
            'https://www.youtube.com/embed/-voP-V7YcqA', MagicMock()
        )

    def test_youtube_embed_invalid(self):
        with pytest.raises(toolkit.Invalid):
            is_valid_video_url('https://www.youtube.com/embed/', MagicMock())
