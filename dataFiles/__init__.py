from struct import unpack


def enum(*sequential, **named):
    """
    Taken from http://stackoverflow.com/questions/36932/how-can-i-represent-an-enum-in-python
    """
    enums = dict(zip(sequential, range(len(sequential))), **named)
    reverse = dict((value, key) for key, value in enums.iteritems())
    enums['reverse_mapping'] = reverse
    return type('Enum', (), enums)


# Taken from include/mysql_com.h
MYSQL_FIELD_TYPES = enum('MYSQL_TYPE_DECIMAL', 'MYSQL_TYPE_TINY',
                        'MYSQL_TYPE_SHORT',  'MYSQL_TYPE_LONG',
                        'MYSQL_TYPE_FLOAT',  'MYSQL_TYPE_DOUBLE',
                        'MYSQL_TYPE_NULL',   'MYSQL_TYPE_TIMESTAMP',
                        'MYSQL_TYPE_LONGLONG','MYSQL_TYPE_INT24',
                        'MYSQL_TYPE_DATE',   'MYSQL_TYPE_TIME',
                        'MYSQL_TYPE_DATETIME', 'MYSQL_TYPE_YEAR',
                        'MYSQL_TYPE_NEWDATE', 'MYSQL_TYPE_VARCHAR',
                        'MYSQL_TYPE_BIT',
                        MYSQL_TYPE_NEWDECIMAL=246,
                        MYSQL_TYPE_ENUM=247,
                        MYSQL_TYPE_SET=248,
                        MYSQL_TYPE_TINY_BLOB=249,
                        MYSQL_TYPE_MEDIUM_BLOB=250,
                        MYSQL_TYPE_LONG_BLOB=251,
                        MYSQL_TYPE_BLOB=252,
                        MYSQL_TYPE_VAR_STRING=253,
                        MYSQL_TYPE_STRING=254,
                        MYSQL_TYPE_GEOMETRY=255)


class MyIsamFormatFileException(Exception):
    pass

class MyIsamFormatFile:
    """
    Interact with a MySql .frm file.

    http://dev.mysql.com/doc/internals/en/frm-file-format.html
    """

    def __init__(self, format_filename=None):
        self.format_filename = format_filename
        self.file_handler = open(self.format_filename, "rb")
        if not self.verify_header():
            raise MyIsamFormatFileException("Invalid Magic Number")

    def verify_header(self):
        """
        Return true if the file has the correct magic characters.
        """
        self.file_handler.seek(0)
        return '\xfe\x01' == self.file_handler.read(2)

    def parse_header(self):
        """
        Pull information out of the header of the format file.
        """
        self.file_handler.seek(0)
        header_string = self.file_handler.read(62)
        self.frm_ver = header_string[3]
        self.legacy_db_type = header_string[4]
        self.iosize = header_string[6:8]
        self.length = header_string[10:14]
        self.rec_length = header_string[16:18]
        self.max_rows = header_string[18:22]
        self.min_rows = header_string[22:26]
        self.key_info_length = header_string[30:32]
        # Are the rest of these right?
        self.mysql_version = header_string[50:54]

        self.file_handler.seek(8238)
        self.comment_length = ord(self.file_handler.read(1))
        self.comment = self.file_handler.read(self.comment_length)

        self.file_handler.seek(8450)
        self.number_of_columns = unpack("<H", self.file_handler.read(2))[0]

        self.file_handler.seek(8460)
        self.n_length = unpack("<H", self.file_handler.read(2))[0]

        self.file_handler.seek(8530)
        self.column_names = []
        for column_number in range(self.number_of_columns):
            current_column_name_length = ord(self.file_handler.read(1))
            self.column_names.append(self.file_handler.read(current_column_name_length-1))
            self.file_handler.read(1) # Null terminator for string column name
            self.file_handler.read(1) # Unknown Value 1
            self.file_handler.read(1) # Unknown Value 2

        # Wtf are these two columns? The documentation doesn't describe them well
        self.number_of_bytes_in_a_column = ord(self.file_handler.read(1))
        self.file_handler.read(1) # this is the same value as the previous byte

        self.file_handler.read(4) # \00\02\00\00 Unknown according to the docs 

        self.first_flags = self.file_handler.read(1)
        self.second_flags = self.file_handler.read(1)

        self.file_handler.read(3) # Not described by the docs. Probably left open for future changes

        self.column_types = []
        self.column_character_sets = []
        for column_number in range(self.number_of_columns):
            self.column_types.append(MYSQL_FIELD_TYPES.reverse_mapping[ord(self.file_handler.read(1))])
            self.column_character_sets.append(ord(self.file_handler.read(1)))
            self.file_handler.read(15) # unknown bytes
