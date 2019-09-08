import logging
import re

import requests

logger = logging.getLogger(__file__)

'''RequestHandler has a bunch of capabilities to help out with downloading files'''
class RequestHandler(object):
    def __init__(self):
        pass

    def checkURL(self, url):
        # regex for verifying url's validity
        if not re.match('(www.)|((http)(s?)([:])//)', url):
            logging.error('INVALID url - {}'.format(url))
            return False
        try:
            r = requests.head(url)
            return True if r.status_code == 200 else False
        except(requests.exceptions.RequestException):
            logging.error('INVALID url - {}'.format(url))
            return False

    def fetchAll(self, url):
        return requests.get(url, stream=True)

    @classmethod
    def breakURL(cls, url):
        # breaks the url into root url and image name
        root, filename = url.rsplit('/', 1)
        # removing unwanted characters after file name
        if '?' in filename:
            for _ in range(filename.count('?')):
                filename = filename.rsplit('?', 1)[0]
        return root, filename
