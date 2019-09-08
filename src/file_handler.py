import os


class FileHandler(object):
    def __init__(self, file):
        self.data = self.__funnelFileFormat(file)

    def __funnelFileFormat(self, file):
        return self.readFile(file) if isinstance(file, str) else file.read() if hasattr(file, 'read') else None

    def readFile(self, file):
        try:
            with open(file, 'r') as f:
                data = f.read()
            return data
        except FileNotFoundError:
            return None

    def toString(self):
        return str(self.data)

    @staticmethod
    def saveAnyDataTo(data, path):
        dir = os.path.dirname(path)
        if not os.path.isdir(dir):
            os.makedirs(dir)
        with open(os.path.join(path), "wb+") as f:
            f.write(data)

    def saveDataTo(self, path):
        FileHandler.saveAnyDataTo(self.data, path)

    def getFileAsList(self):
        return self.toString().split('\n')
