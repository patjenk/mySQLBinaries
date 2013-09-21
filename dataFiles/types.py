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
