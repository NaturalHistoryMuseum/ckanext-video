# this is a namespace package
try:
    import pkg_resources
    pkg_resources.declare_namespace(__name__)
except ImportError:
    import pkgutil
    __path__ = pkgutil.extend_path(__path__, __name__)

# Dictionary of allowable video provider patterns
video_provider_patterns = {
    'vimeo':  '//player.vimeo.com/video/[0-9]+',  # Embedded vimeo link
    'youtube_link':  'http[s]?:\/\/www.youtube.com\/watch\?v=([0-9a-z/-]+)',  # Link to you tube video page - () group to de-mark video ID
    'youtube_embedded': 'http[s]?:\/\/www.youtube.com\/embed\/([0-9a-z/-]+)'  # Embedded youtube video - () group to de-mark video ID
}