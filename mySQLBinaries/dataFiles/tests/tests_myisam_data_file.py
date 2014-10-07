from ..myIsamDataFile import MyIsamDataFile, MyIsamDataFileException
from ..types import MYISAM_DATA_FILE_FORMATS, MYSQL_FIELD_TYPES
from unittest import TestCase


class TestsReadMyIsamDataFile(TestCase):
    def test_guess_row_format(self):
        myisam_data_file = MyIsamDataFile("dataFiles/tests/examples/test_basics/myisam_table_one.MYD")
        self.assertEqual(MYISAM_DATA_FILE_FORMATS.MYISAM_DYNAMIC, myisam_data_file.guess_row_format_type())

    def test_read_dynamic_first_row(self):
        """
        Test that we can read the first row in a dynamically formatted myisam data file.
        """
        myisam_data_file = MyIsamDataFile("dataFiles/tests/examples/test_basics/myisam_table_one.MYD")
        myisam_data_file.column_types = [MYSQL_FIELD_TYPES.MYSQL_TYPE_LONG, MYSQL_FIELD_TYPES.MYSQL_TYPE_VARCHAR, MYSQL_FIELD_TYPES.MYSQL_TYPE_VARCHAR, MYSQL_FIELD_TYPES.MYSQL_TYPE_VARCHAR, MYSQL_FIELD_TYPES.MYSQL_TYPE_VARCHAR]
        myisam_record = myisam_data_file.get_row(1)
        myisam_values = [1, 'lastname 1', 'firstname 1', 'address 1', 'city 1']
        self.assertEqual(myisam_record, myisam_values)

    def test_read_dynamic_second_row(self):
        """
        Test that we can read the secon row in a dynamically formatted myisam data file.
        """
        myisam_data_file = MyIsamDataFile("dataFiles/tests/examples/test_basics/myisam_table_one.MYD")
        myisam_data_file.column_types = [MYSQL_FIELD_TYPES.MYSQL_TYPE_LONG, MYSQL_FIELD_TYPES.MYSQL_TYPE_VARCHAR, MYSQL_FIELD_TYPES.MYSQL_TYPE_VARCHAR, MYSQL_FIELD_TYPES.MYSQL_TYPE_VARCHAR, MYSQL_FIELD_TYPES.MYSQL_TYPE_VARCHAR]
        myisam_record = myisam_data_file.get_row(2)
        myisam_values = [2, 'lastname 2', 'firstname 2', 'address 2', 'city 2']
        self.assertEqual(myisam_record, myisam_values)

    def test_read_dynamic_third_row(self):
        """
        Test that we can read the secon row in a dynamically formatted myisam data file.
        """
        myisam_data_file = MyIsamDataFile("dataFiles/tests/examples/test_basics/myisam_table_one.MYD")
        myisam_data_file.column_types = [MYSQL_FIELD_TYPES.MYSQL_TYPE_LONG, MYSQL_FIELD_TYPES.MYSQL_TYPE_VARCHAR, MYSQL_FIELD_TYPES.MYSQL_TYPE_VARCHAR, MYSQL_FIELD_TYPES.MYSQL_TYPE_VARCHAR, MYSQL_FIELD_TYPES.MYSQL_TYPE_VARCHAR]
        myisam_record = myisam_data_file.get_row(3)
        myisam_values = [3, 'lastname 3', 'firstname 3', 'address 3', 'city 3']
        self.assertEqual(myisam_record, myisam_values)

    def test_read_dynamic_fourth_row(self):
        """
        Test that we can read the secon row in a dynamically formatted myisam data file.
        """
        myisam_data_file = MyIsamDataFile("dataFiles/tests/examples/test_basics/myisam_table_one.MYD")
        myisam_data_file.column_types = [MYSQL_FIELD_TYPES.MYSQL_TYPE_LONG, MYSQL_FIELD_TYPES.MYSQL_TYPE_VARCHAR, MYSQL_FIELD_TYPES.MYSQL_TYPE_VARCHAR, MYSQL_FIELD_TYPES.MYSQL_TYPE_VARCHAR, MYSQL_FIELD_TYPES.MYSQL_TYPE_VARCHAR]
        myisam_record = myisam_data_file.get_row(4)
        myisam_values = [4, 'lastname 4', 'firstname 4', 'address 4', 'city 4']
        self.assertEqual(myisam_record, myisam_values)

    def test_read_dynamic_fifth_row(self):
        """
        Test that we can read the secon row in a dynamically formatted myisam data file.
        """
        myisam_data_file = MyIsamDataFile("dataFiles/tests/examples/test_basics/myisam_table_one.MYD")
        myisam_data_file.column_types = [MYSQL_FIELD_TYPES.MYSQL_TYPE_LONG, MYSQL_FIELD_TYPES.MYSQL_TYPE_VARCHAR, MYSQL_FIELD_TYPES.MYSQL_TYPE_VARCHAR, MYSQL_FIELD_TYPES.MYSQL_TYPE_VARCHAR, MYSQL_FIELD_TYPES.MYSQL_TYPE_VARCHAR]
        myisam_record = myisam_data_file.get_row(5)
        myisam_values = [5, 'lastname 5', 'firstname 5', 'address 5', 'city 5']
        self.assertEqual(myisam_record, myisam_values)

    def test_read_dynamic_missing_row(self):
        """
        Test that when we try to read a nonexistant row that we get an exception
        """
        myisam_data_file = MyIsamDataFile("dataFiles/tests/examples/test_basics/myisam_table_one.MYD")
        myisam_data_file.column_types = [MYSQL_FIELD_TYPES.MYSQL_TYPE_LONG, MYSQL_FIELD_TYPES.MYSQL_TYPE_VARCHAR, MYSQL_FIELD_TYPES.MYSQL_TYPE_VARCHAR, MYSQL_FIELD_TYPES.MYSQL_TYPE_VARCHAR, MYSQL_FIELD_TYPES.MYSQL_TYPE_VARCHAR]
        self.assertRaises(MyIsamDataFileException, myisam_data_file.get_row, (6))
