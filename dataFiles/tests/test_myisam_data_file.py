from ..myIsamDataFile import MyIsamDataFile
from ..types import MYSQL_FIELD_TYPES
from unittest import TestCase


class TestsReadMyIsamDataFile(TestCase):
    def test_verify(self):
        MyIsamDataFile("dataFiles/tests/examples/readme/myisam_table_one.frm")
