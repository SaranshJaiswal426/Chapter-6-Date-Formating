#try outdatting of datetime object of string
from datetime import datetime
datetime_for_string = datetime(2016,10,1,0,0)

datetime_string_format = '%b %d %Y, %H:%M:%S'
datetime_for_string.strftime(datetime_string_format)


