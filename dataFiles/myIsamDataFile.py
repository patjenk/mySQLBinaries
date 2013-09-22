class MyIsamDataFileException(Exception):
    pass


class MyIsamDataFile:
    """
    Interact with a MySql .MYD file.

    http://dev.mysql.com/doc/internals/en/myisam-introduction.html
    """

    def __init__(self, data_filename=None):
        self.data_filename = data_filename
        self.file_handler = open(self.data_filename, 'rb')
        if not self.verify_header():
            raise MyIsamDataFileException("Invalid Magic Number")

    def verify_header(self):
        """
        Return true if the file has the correct magic characters.
        """
        self.file_handler.seek(0)
        return '\xfe\x01' == self.file_handler.read(2)

