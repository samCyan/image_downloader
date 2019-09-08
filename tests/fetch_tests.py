import unittest
from unittest.mock import patch, mock_open, Mock

from src.fetch import FetchImages

from src.request_handler import RequestHandler


class FileHandlerTest(unittest.TestCase):
    def setUp(self) -> None:
        self.path1 = "abc/xyz"
        req_mock = Mock()
        req_mock.checkURL = lambda x: True
        req_mock.breakURL = lambda x: RequestHandler.breakURL(x)
        content_mock = Mock()
        content_mock.content = "test data"
        req_mock.fetchAll = Mock(return_value=content_mock)
        self.sut = FetchImages(req_mock)

    def test_fromFile(self):
        with patch("builtins.open", mock_open(read_data="link1\nlink2")) as mock_file:
            newSut = self.sut.fromFile(self.path1)
            assert newSut.urls == ['link1', 'link2']

    def test_fromUrl(self, url=None, filename=None):
        testUrl = url or "http://abc.com/image1.jpg"
        expectdFileName = filename or "image1.jpg"
        img, filename = self.sut.fromUrl(testUrl)
        assert img.content == "test data"
        assert filename == expectdFileName

    def test_fromUrl_invalid(self):
        testUrl = "http://abc.com/image1.jpg"
        self.sut.reqHandler.checkURL = lambda x: False
        img, filename = self.sut.fromUrl(testUrl)
        assert img is None
        assert filename is None

    def test_getImages(self):
        for i in range(4):
            self.test_fromUrl("http://abc.com/image{}.jpg".format(i), "image{}.jpg".format(i))

    def test_saveTo(self):
        with patch("builtins.open", mock_open(read_data="www.abc.com/image1.jpg")):
            self.sut = self.sut.fromFile(self.path1)
            with patch("builtins.open", mock_open(), create=True) as mock_file:
                with patch('os.path.isdir') as dir_mock:
                    dir_mock.return_value = lambda x: True
                    self.sut.saveTo('abc')
                    mock_file.assert_called_with('abc/image1.jpg', 'wb+')


if __name__ == '__main__':
    unittest.main()
