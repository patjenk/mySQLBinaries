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


# this one i made up
MYISAM_DATA_FILE_FORMATS = enum('MYISAM_FIXED', 'MYISAM_DYNAMIC', 'MYISAM_PACKED', 'MYISAM_BLOB')

# optionbits for database, Defined in include/my_base.h
HA_OPTION_PACK_RECORD           = 1
HA_OPTION_PACK_KEYS             = 2
HA_OPTION_COMPRESS_RECORD       = 4
HA_OPTION_LONG_BLOB_PTR         = 8 # new ISAM format */
HA_OPTION_TMP_TABLE             = 16
HA_OPTION_CHECKSUM              = 32
HA_OPTION_DELAY_KEY_WRITE       = 64
HA_OPTION_NO_PACK_KEYS          = 128 # Reserved for MySQL */
HA_OPTION_CREATE_FROM_ENGINE    = 256
HA_OPTION_RELIES_ON_SQL_LAYER   = 512
HA_OPTION_NULL_FIELDS           = 1024
HA_OPTION_PAGE_CHECKSUM         = 2048
HA_OPTION_TEMP_COMPRESS_RECORD  = 16384 # set by isamchk */
HA_OPTION_READ_ONLY_DATA        = 32768 # Set by isamchk */

# Bits in flag to create(), Defined in include/my_base.h
HA_DONT_TOUCH_DATA      = 1       # Don't empty datafile (isamchk) */
HA_PACK_RECORD          = 2       # Request packed record format */
HA_CREATE_TMP_TABLE     = 4
HA_CREATE_CHECKSUM      = 8
HA_CREATE_KEEP_FILES    = 16      # don't overwrite .MYD and MYI */
HA_CREATE_PAGE_CHECKSUM = 32
HA_CREATE_DELAY_KEY_WRITE = 64
HA_CREATE_RELIES_ON_SQL_LAYER = 128
