from .. import MyIsamFormatFile
from unittest import TestCase


class TestsReadMyIsamFormatFile(TestCase):
    def test_verify(self):
        MyIsamFormatFile("examples/readme/myisam_table_one.frm")

    def test_parse_header(self):
        format_file = MyIsamFormatFile("examples/readme/myisam_table_one.frm")
        format_file.parse_header()
        self.assertEqual(format_file.frm_ver, '\x09')
        self.assertEqual(format_file.legacy_db_type, '\x03')
        self.assertEqual(format_file.iosize, '\x00\x10')
        self.assertEqual(format_file.length, '\x00\x30\x00\x00')
        self.assertEqual(format_file.rec_length, '\x05\x04')
        self.assertEqual(format_file.max_rows, '\x00\x00\x00\x00')
        self.assertEqual(format_file.min_rows, '\x00\x00\x00\x00')
        self.assertEqual(format_file.key_info_length, '\x09\x00')
