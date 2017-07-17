import time

tme1 = time.localtime()

print tme1

# use \
print \
    tme1.tm_year, '/', \
    tme1.tm_mon, '/', \
    tme1.tm_mday, '/', \
    tme1.tm_wday, '/', \
    tme1.tm_hour, '/', \
    tme1.tm_min, '/', \
    tme1.tm_sec

str1 = time.ctime()
print str1

str2 = time.time()
time.sleep(5)
str3 = time.time()
print str3, ' - ', str2, ' = ', str3 - str2