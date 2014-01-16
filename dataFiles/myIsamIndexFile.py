from struct import unpack


class MyIsamIndexFileException(Exception):
    pass


class MyIsamIndexFile:
    """
    Interact with a MySql .MYI file.

    http://dev.mysql.com/doc/internals/en/the-myi-file.html
    """
    def __init__(self, index_filename=None):
        self.index_filename = index_filename
        self.file_handler = open(self.index_filename, 'rb')
        if not self.verify_header():
            raise MyIsamIndexFileException("Invalid Magic Number")

    def verify_header(self):
        """
        Return true if the file has the correct magic characters.
        """
        self.file_handler.seek(0)
        return '\xfe\xfe\x07\x01' == self.file_handler.read(4)


    def parse_header(self):
        """
        Pull information out of the header of the format file.
        """
        self.file_handler.seek(0)
        self.file_version = unpack("I", self.file_handler.read(4))

        self.options = unpack("H", self.file_handler.read(2))
        self.header_length = unpack("H", self.file_handler.read(2))
        self.state_info_length = unpack("H", self.file_handler.read(2))
        self.base_info_length = unpack("H", self.file_handler.read(2))
        self.base_pos = unpack("H", self.file_handler.read(2))
        self.key_parts = unpack("H", self.file_handler.read(2))
        self.unique_key_parts = unpack("H", self.file_handler.read(2))

        self.keys = unpack("b", self.file_handler.read(1))
        self.uniques = unpack("b", self.file_handler.read(1))
        self.languages = unpack("b", self.file_handler.read(1))
        self.max_block_size = unpack("b", self.file_handler.read(1))
        self.full_text_keys = unpack("b", self.file_handler.read(1))
        self.file_handler.read(1) # There is an unused byte here to get to 4 byte alignment

        self.state_open_count = unpack("H", self.file_handler.read(2))
        self.state_changed = unpack("b", self.file_handler.read(1))
        self.state_sortkey = unpack("b", self.file_handler.read(1))
        self.state_records = unpack("Q", self.file_handler.read(8))
        self.state_del = unpack("Q", self.file_handler.read(8))
        self.state_split = unpack("Q", self.file_handler.read(8))
        self.state_dellink = unpack("Q", self.file_handler.read(8))
        
        self.state_key_file_length = unpack("Q", self.file_handler.read(8))
        self.state_data_file_length = unpack("Q", self.file_handler.read(8))
        self.state_empty = unpack("Q", self.file_handler.read(8))
        self.state_key_empty = unpack("Q", self.file_handler.read(8))
        self.state_auto_increment = unpack("Q", self.file_handler.read(8))
        self.state_checksum = unpack("Q", self.file_handler.read(8))

        self.state_process = unpack("I", self.file_handler.read(4))
        self.state_unique = unpack("I", self.file_handler.read(4))
        self.state_status = unpack("I", self.file_handler.read(4))
        self.state_update_count = unpack("I", self.file_handler.read(4))
