from ..myIsamIndexFile import MyIsamIndexFile
from unittest import TestCase


class TestsReadMyIsamIndexFile(TestCase):
    def test_verify(self):
        """
        When we open a valid mysql myisam index file
        And that index file is valid
        Then we will not raise an exception.
        """
        MyIsamIndexFile("dataFiles/tests/examples/readme/myisam_table_one.MYI")

    def test_parse_header(self):
        """
        When we open a valid mysql myisam index file
        And we attempt to read information from the header
        We will pull out the right information.

        Note: This test uses a cooked up myisam index file that we assume to be correct.
        """
        index_file = MyIsamIndexFile("dataFiles/tests/examples/readme/myisam_table_one.MYI")
        index_file.parse_header()
        self.assertEqual(0, index_file.header_state['keys'])
        self.assertEqual(0, index_file.header_state['full_text_keys'])
