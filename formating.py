from datetime import datetime
a = datetime(2016,10,6,0,0,0)
b = datetime(2016,10,1,23,59,59)
a-b
# datetime.timedelta(4, 1)
(a-b).days
# 4
(a-b).total_seconds()