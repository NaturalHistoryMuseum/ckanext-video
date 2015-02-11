import logging
import ckan.plugins as p
import re
from ckanext.video.logic.validators import is_valid_video_url
from ckanext.video import video_provider_patterns

log = logging.getLogger(__name__)
ignore_empty = p.toolkit.get_validator('ignore_empty')
not_empty = p.toolkit.get_validator('not_empty')
is_positive_integer = p.toolkit.get_validator('is_positive_integer')



class VideoPlugin(p.SingletonPlugin):
    '''
    Resource view for embedding videos (youtube/vimeo)
    '''

    p.implements(p.IConfigurer, inherit=True)
    p.implements(p.IResourceView, inherit=True)
    p.implements(p.IPackageController, inherit=True)

    def update_config(self, config):
        p.toolkit.add_template_directory(config, 'theme/templates')

    def info(self):
        return {'name': 'video',
                'title': 'Embedded video',
                'schema': {
                    'video_url': [ignore_empty, unicode, is_valid_video_url],
                    'width': [not_empty, is_positive_integer],
                    'height': [not_empty, is_positive_integer],
                },
                'iframed': False,
                'icon': 'film'}

    def can_view(self, data_dict):
        return True

    def view_template(self, context, data_dict):
        return 'video_view.html'

    def form_template(self, context, data_dict):
        return 'video_form.html'

    def setup_template_variables(self, context, data_dict):
        """Setup variables available to templates"""

        video_url = data_dict['resource_view'].get('video_url') or data_dict['resource'].get('url')

        # Is this a youtube video?
        if 'youtube.com' in video_url:
            # If this is a youtube link, replace with a URL for embeddable video
            match = re.search(video_provider_patterns['youtube_link'], video_url, re.IGNORECASE)
            if match:
                video_url = 'https://www.youtube.com/embed/%s' % match.group(1)

        # TODO - More video provider types

        return {
            'defaults': {
                'width': 480,
                'height': 390
            },
            'video_url': video_url
        }