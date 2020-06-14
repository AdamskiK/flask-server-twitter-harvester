import logging
import requests

logger = logging.getLogger(__name__)


class Request(object):
    def __init__(self, url):
        self.url = url
        self.headers = {"Content-Type": "application/json"}

    def post(self, data):
        logger.info('Making post request to url: {}'.format(self.url))
        _ = requests.post(self.url, data=data, headers=self.headers)
