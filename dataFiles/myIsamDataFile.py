from .types import MYISAM_DATA_FILE_BLOCK_TYPES, MYISAM_DATA_FILE_FORMATS, MYSQL_FIELD_TYPES
from struct import unpack


class MyIsamRecord:
    """
    Encapsulate a record from a MyIsam data file.
    """
    column_data = []
    block_type = None

    def __init__(self):
        pass


class MyIsamDataFileException(Exception):
    pass


class MyIsamDataFile:
    """
    Interact with a MySql .MYD file.

    http://dev.mysql.com/doc/internals/en/myisam-introduction.html

    Dynamic File Structure:
    http://dev.mysql.com/doc/internals/en/myisam-dynamic-data-file-layout.html
    """

    def __init__(self, data_filename=None, myisam_format_file_obj=None):
        self.data_filename = data_filename
        self.myisam_format_file_obj = myisam_format_file_obj
        self.file_handler = open(self.data_filename, 'rb')
        self.column_types = None

    def guess_row_format_type(self):
        """
        Look at the structure of the datafile and try to determine if which 
        type of row format we're dealing with.
        """
        return MYISAM_DATA_FILE_FORMATS.MYISAM_DYNAMIC

    def get_row(self, number):
        """
        Return the nth row (starting at 0) in the file.
        """
        self.file_handler.seek(0)
        row_values = []
        for x in range(number):
            row_values = []
            beginning_offset = self.file_handler.tell()
            ending_offset = -1
            part_header_raw = self.file_handler.read(1)
            if "" == part_header_raw:
                raise MyIsamDataFileException("End of File Reached")
            part_header = ord(part_header_raw)
            record_type = self.record_part_record_block(part_header)
            if record_type == MYISAM_DATA_FILE_BLOCK_TYPES.FULL_SMALL_RECORD_WITH_UNUSED_SPACE:
                record_length = ord(self.file_handler.read(1))
                data_len = ord(self.file_handler.read(1))
                unused_len = ord(self.file_handler.read(1))
                header_length = 4
                flags_and_overflow_pointer = self.file_handler.read(2)
                for column_type in self.column_types:
                    if column_type == MYSQL_FIELD_TYPES.MYSQL_TYPE_LONG:
                        row_values.append(unpack("<i", self.file_handler.read(4))[0])
                    elif column_type == MYSQL_FIELD_TYPES.MYSQL_TYPE_VARCHAR:
                        varchar_length = ord(self.file_handler.read(1))
                        row_values.append(self.file_handler.read(varchar_length))
                    else:
                        raise MyIsamDataFileException("Unrecognized Column Data Type: %02d" % column_type)
                ending_offset = self.file_handler.tell()
                self.file_handler.read(unused_len) # unused portion
            else:
                raise MyIsamDataFileException("%02d myisam record type is unsupported" % record_type)
        return row_values


    def record_part_record_block(self, part_header):
        """
        Return the MYISAM_DATA_FILE_BLOCK_TYPE
        """
        if 0 == part_header:
            return MYISAM_DATA_FILE_BLOCK_TYPES.DELETED_BLOCK
        elif 1 == part_header:
            return MYISAM_DATA_FILE_BLOCK_TYPES.FULL_SMALL_RECORD_WITH_FULL_BLOCK
        elif 2 == part_header:
            return MYISAM_DATA_FILE_BLOCK_TYPES.FULL_BIG_RECORD_WITH_FULL_BLOCK
        elif 3 == part_header:
            return MYISAM_DATA_FILE_BLOCK_TYPES.FULL_SMALL_RECORD_WITH_UNUSED_SPACE
        elif 4 == part_header:
            return MYISAM_DATA_FILE_BLOCK_TYPES.FULL_BIG_RECORD_WITH_UNUSED_SPACE
        elif 5 == part_header:
            return MYISAM_DATA_FILE_BLOCK_TYPES.START_SMALL_RECORD
        elif 6 == part_header:
            return MYISAM_DATA_FILE_BLOCK_TYPES.START_BIG_RECORD
        elif 7 == part_header:
            return MYISAM_DATA_FILE_BLOCK_TYPES.END_SMALL_RECORD_WITH_FULL_BLOCK
        elif 8 == part_header:
            return MYISAM_DATA_FILE_BLOCK_TYPES.END_BIG_RECORD_WITH_FULL_BLOCK
        elif 9 == part_header:
            return MYISAM_DATA_FILE_BLOCK_TYPES.END_SMALL_RECORD_WITH_UNUSED_SPACE
        elif 10 == part_header:
            return MYISAM_DATA_FILE_BLOCK_TYPES.END_BIG_RECORD_WITH_UNUSED_SPACE
        elif 11 == part_header:
            return MYISAM_DATA_FILE_BLOCK_TYPES.CONTINUE_SMALL_RECORD
        elif 12 == part_header:
            return MYISAM_DATA_FILE_BLOCK_TYPES.CONTINUE_BIG_RECORD
        elif 13 == part_header:
            return MYISAM_DATA_FILE_BLOCK_TYPES.START_GIANT_RECORD
        else:
            raise MyIsamDataFileException("Unrecognized myisam record type: %02d" % part_header)
