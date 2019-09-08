import unittest
from unittest.mock import patch, Mock

from src.request_handler import RequestHandler


class FileHandlerTest(unittest.TestCase):
    def setUp(self) -> None:
        self.sut = RequestHandler()

    def test_checkURL_invalid(self):
        testUrl = "gc.vhv.com"
        assert self.sut.checkURL(testUrl) == False

    def test_checkURL_valid(self):
        testUrl = "http://abc.com"
        m = Mock()
        m.status_code = 200
        with patch('requests.get', Mock(return_value=m)) as p:
            assert self.sut.checkURL(testUrl) == True

    def test_fetchAll(self):
        testUrl = "http://abc.com"
        m = Mock()
        m.status_code = 200
        m.content = "test data"
        with patch('requests.get', Mock(return_value=m)) as p:
            actual_data = self.sut.fetchAll(testUrl)
            assert actual_data.content == "test data"

    def test_breakURL(self):
        testUrls = ["http://abc.com/img.jpg", "http://abc.com/img.jpg?a=1"]
        for url in testUrls:
            root, filename = self.sut.breakURL(url)
            assert root == "http://abc.com"
            assert filename == "img.jpg"


if __name__ == '__main__':
    unittest.main()
