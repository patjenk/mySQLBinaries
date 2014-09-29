from ..myIsamIndexFile import MyIsamIndexFile
from unittest import TestCase


class TestsReadMyIsamIndexFile(TestCase):
    def test_verify(self):
        MyIsamIndexFile("dataFiles/tests/examples/readme/myisam_table_one.MYI")

    def test_parse_header(self):
        index_file = MyIsamIndexFile("dataFiles/tests/examples/readme/myisam_table_one.MYI")
        index_file.parse_header()
        self.assertEqual(1, index_file.options)
        self.assertEqual(0, index_file.keys)
        self.assertEqual(5, index_file.state_records)
