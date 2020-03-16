# coding: utf-8
from __future__ import unicode_literals

from .common import InfoExtractor

from ..utils import (
    determine_ext,
    ExtractorError,
    int_or_none,
    js_to_json,
    KNOWN_EXTENSIONS,
    parse_filesize,
    rot47,
    url_or_none,
    urlencode_postdata,
)

class NXLoadIE(InfoExtractor):
    _VALID_URL = ''
    _TEST = {
        'url': 'https://nxload.com/embeded/0yif9Vh0lhWX/kinowelt-resident-evil-the-final-chapter-1080.mkv',
        'md5': '',
        'info_dict': {
            'id': '0yif9Vh0lhWX',
            'ext': 'mkv',
            'title': 'kinowelt-resident-evil-the-final-chapter-1080p.mkv'
        }
    }

    def _real_extract(self, url):
        video_id = self._match_id(url)
        webpage = self._download_webpage(url, video_id)
        title = self._extract_title(webpage)

        return {
            'id': video_id,
            'title': title,
            'url': url,
        }

    def _extract_title(self, webpage):
        return compat_b64decode(self._html_search_meta(
            'full:title', webpage, 'title')).decode('utf-8')