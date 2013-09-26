from ..myIsamFormatFile import MyIsamFormatFile
from ..types import MYISAM_DATA_FILE_FORMATS, MYSQL_FIELD_TYPES
from unittest import TestCase


class TestsReadMyIsamFormatFile(TestCase):
    def test_verify(self):
        MyIsamFormatFile("dataFiles/tests/examples/readme/myisam_table_one.frm")

    def test_parse_header(self):
        format_file = MyIsamFormatFile("dataFiles/tests/examples/readme/myisam_table_one.frm")
        format_file.parse_header()
        self.assertEqual(format_file.row_format, MYISAM_DATA_FILE_FORMATS.MYISAM_DYNAMIC)

        self.assertEqual(format_file.frm_ver, '\x09')
        self.assertEqual(format_file.legacy_db_type, '\x03')
        self.assertEqual(format_file.iosize, '\x00\x10')
        self.assertEqual(format_file.length, '\x00\x30\x00\x00')
        self.assertEqual(format_file.rec_length, '\x05\x04')
        self.assertEqual(format_file.max_rows, '\x00\x00\x00\x00')
        self.assertEqual(format_file.min_rows, '\x00\x00\x00\x00')
        self.assertEqual(format_file.key_info_length, '\x09\x00')

        self.assertEqual(format_file.number_of_columns, 5)
        self.assertEqual(format_file.n_length, 43)
        self.assertEqual(['PersonID', 'LastName', 'FirstName', 'Address', 'City'], format_file.column_names)
        expected_column_types = [MYSQL_FIELD_TYPES.MYSQL_TYPE_LONG, MYSQL_FIELD_TYPES.MYSQL_TYPE_VARCHAR, MYSQL_FIELD_TYPES.MYSQL_TYPE_VARCHAR, MYSQL_FIELD_TYPES.MYSQL_TYPE_VARCHAR, MYSQL_FIELD_TYPES.MYSQL_TYPE_VARCHAR]
        self.assertEqual(len(expected_column_types), len(format_file.column_types))
        for column_number, expected_column_type in enumerate(expected_column_types):
            self.assertEqual(MYSQL_FIELD_TYPES.reverse_mapping[expected_column_type], format_file.column_types[column_number])
        self.assertEqual([8, 8, 8, 8, 8], format_file.column_character_sets)
