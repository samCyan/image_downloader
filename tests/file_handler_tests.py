import unittest
from io import StringIO
from unittest.mock import patch, mock_open

from src.file_handler import FileHandler


class FileHandlerTest(unittest.TestCase):
    def setUp(self) -> None:
        self.path1 = 'xyz'
        with patch("builtins.open", mock_open(read_data="test data")) as mock_file:
            self.sut = FileHandler(self.path1)

    def test_funnelFileFormat_path(self):
        with patch("builtins.open", mock_open(read_data="test data")) as mock_file:
            sut = FileHandler(self.path1)
            assert sut.data == "test data"
            mock_file.assert_called_with(self.path1, 'r')

    def test_funnelFileFormat_file(self):
        file1 = StringIO("test data")
        sut = FileHandler(file1)
        assert sut.data == "test data"

    def test_readFile_valid(self):
        with patch("builtins.open", mock_open(read_data="test data")) as mock_file:
            data = self.sut.readFile(self.path1)
            assert data == "test data"
            mock_file.assert_called_with(self.path1, 'r')

    def test_readFile_invalid(self):
        data = self.sut.readFile("abc")
        assert data == None

    def test_toString(self):
        assert self.sut.toString() == "test data"

    def test_saveAnyDataTo(self):
        m = mock_open()
        with patch("builtins.open", m, create=True) as mock_file:
            with patch('os.path.isdir') as dir_mock:
                dir_mock.return_value = lambda x: True
                FileHandler.saveAnyDataTo("test data", self.path1)
                m.assert_called_with(self.path1, 'wb+')

    def test_saveDataTo(self):
        m = mock_open()
        with patch("builtins.open", m, create=True) as mock_file:
            with patch('os.path.isdir') as dir_mock:
                dir_mock.return_value = lambda x: True
                self.sut.saveDataTo(self.path1)
                m.assert_called_with(self.path1, 'wb+')

    def test_getFileAsList(self):
        self.sut.data = 'abc\ndef'
        assert self.sut.getFileAsList() == ['abc', 'def']


if __name__ == '__main__':
    unittest.main()
