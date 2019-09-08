import os

from src.request_handler import RequestHandler
from src.file_handler import FileHandler


class FetchImages(object):
    '''
    FetchImages provides functionalities for interacting with image urls and downloading them
    '''
    def __init__(self, reqHandler=None):
        super(FetchImages, self).__init__()
        self.urls = []
        self.reqHandler = reqHandler or RequestHandler()

    def fromFile(self, path):
        file_handler = FileHandler(path)
        self.urls = file_handler.getFileAsList()
        return self

    def fromUrl(self, url):
        if self.reqHandler.checkURL(url):
            _, fileName = self.reqHandler.breakURL(url)
            image = self.reqHandler.fetchAll(url)
            return image, fileName
        return (None, None)

    def fromUrls(self, urls):
        self.urls = urls
        return self

    def getImages(self):
        for url in self.urls:
            yield self.fromUrl(url)

    def saveTo(self, dir):
        self.dir = dir
        for image, fileName in self.getImages():
            if image is None:
                continue
            FileHandler.saveAnyDataTo(image.content, os.path.join(self.dir, fileName))


if __name__ == "__main__":
    fetchimages = FetchImages()
    source = '/Users/samarth/Documents/My_MAC_Files/projects/dev/python/flask/image_downloader/gits/image_downloader/images.txt'
    dest = '/Users/samarth/Documents/My_MAC_Files/projects/dev/python/flask/image_downloader/gits/image_downloader/downloads/'
    fetchimages.fromFile(source).saveTo(dest)
