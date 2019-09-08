import logging
import os

from src.file_handler import FileHandler
from src.request_handler import RequestHandler
from src import ROOT_DIR

logger = logging.getLogger(__file__)

'''FetchImages provides functionalities for interacting with image urls and downloading them'''
class FetchImages(object):

    def __init__(self, reqHandler=None):
        super(FetchImages, self).__init__()
        self.urls = []
        # reqHandler optional parameter helps with dependency injection while writing unit test scripts
        self.reqHandler = reqHandler or RequestHandler()

    def fromFile(self, path):
        file_handler = FileHandler(path)
        self.urls = file_handler.getFileAsList()
        logging.info('list of urls - \n{}'.format('\n'.join(self.urls)))
        # returning self for enabling method chaining
        return self

    def fromUrl(self, url):
        if self.reqHandler.checkURL(url):
            _, fileName = self.reqHandler.breakURL(url)
            image = self.reqHandler.fetchAll(url)
            return image, fileName
        return (None, None)

    def fromUrls(self, urls):
        self.urls = urls
        logging.info('list of urls - {}'.format('\n'.join(self.urls)))
        # returning self for enabling method chaining
        return self

    def getImages(self):
        for url in self.urls:
            yield self.fromUrl(url)

    def saveTo(self, dir=os.path.join(ROOT_DIR, 'downloads')):
        # by default the images are stored in a <root>/downloads folder
        self.dir = dir
        for image, fileName in self.getImages():
            if image is None:
                continue
            FileHandler.saveAnyDataTo(image.content, os.path.join(self.dir, fileName))


if __name__ == "__main__":
    fetchimages = FetchImages()
    source = '/Users/samarth/Documents/My_MAC_Files/projects/dev/python/flask/image_downloader/gits/image_downloader/images.txt'
    # dest = '/Users/samarth/Documents/My_MAC_Files/projects/dev/python/flask/image_downloader/gits/image_downloader/downloads/'
    fetchimages.fromFile(source).saveTo()
