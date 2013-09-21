class MyIsamFormatFileException(Exception):
    pass

class MyIsamFormatFile:
    """
    Interact with a MySql .frm file.

    http://dev.mysql.com/doc/internals/en/frm-file-format.html
    """

    def __init__(self, format_filename=None):
        self.format_filename = format_filename
        self.file_handler = open(format_filename, "rb")
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
        self.mysql_version = header_string[51:55]

