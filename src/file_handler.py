import logging
import os

logger = logging.getLogger(__file__)

'''FileHandler helps in dealing with storage/retrieval of files'''
class FileHandler(object):
    def __init__(self, file):
        self.data = self.__funnelFileFormat(file)

    '''returns the file content according to the param file type'''
    def __funnelFileFormat(self, file):
        return self.readFile(file) if isinstance(file, str) else file.read() if hasattr(file, 'read') else None

    def readFile(self, file):
        try:
            with open(file, 'r') as f:
                data = f.read()
            return data
        except FileNotFoundError:
            logging.error('INVALID file path - {}'.format(file))
            return None

    def toString(self):
        return str(self.data)

    @staticmethod
    def saveAnyDataTo(data, path):
        dir = os.path.dirname(path)
        # make directories if doesn't exist
        if not os.path.isdir(dir):
            os.makedirs(dir)
        with open(os.path.join(path), "wb+") as f:
            f.write(data)
        logging.info('downloaded {} at {}'.format(path.rsplit('/', 1)[1], path))

    def saveDataTo(self, path):
        FileHandler.saveAnyDataTo(self.data, path)

    def getFileAsList(self):
        return self.toString().split('\n')
