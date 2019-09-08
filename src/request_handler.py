import re
import requests


class RequestHandler(object):
    def __init__(self):
        pass

    def checkURL(self, url):
        if not re.match('(www.)|((http)(s?)([:])//)', url):
            return False
        request = requests.get(url)
        return True if request.status_code == 200 else False

    def fetchAll(self, url):
        return requests.get(url, stream=True)

    @classmethod
    def breakURL(cls, url):
        root, filename = url.rsplit('/', 1)
        if '?' in filename:
            for _ in range(filename.count('?')):
                filename = filename.rsplit('?', 1)[0]
        return root, filename
