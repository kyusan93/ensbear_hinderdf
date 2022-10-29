from random import randrange
from datetime import datetime,timedelta
from win32_setctime import setctime
import os
import random
import uuid

def generate_files(d1,d2):
    for i in range(0, 100):
        rand_date = random_date(d1, d2)
        print(rand_date)
        rand_filename = "C:/Tools/" + str(uuid.uuid1()) + ".txt"
        with open(rand_filename, 'w') as f:
            f.write('This is a file')
            f.close()
        setctime(rand_filename, rand_date)
        os.utime(rand_filename, (rand_date, rand_date))

def random_date(start, end):
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    random_millisecs = random.randint(100,500)
    rand_date = start + timedelta(seconds=random_second) + timedelta(milliseconds=random_millisecs)
    print(rand_date)
    rand_date_seconds = rand_date.timestamp()
    return rand_date_seconds

def get_cur_date():
    cur_year = str(datetime.now().year)
    cur_month = str(datetime.now().month)
    cur_day = str(datetime.now().day)
    return cur_day,cur_month,cur_year

cur_day,cur_month,cur_year = get_cur_date()
min_year = str(int(cur_year)-5)
d1 = datetime.strptime('%s/%s/%s 00:00' %(cur_day,cur_month,min_year), '%d/%m/%Y %H:%M')
d2 = datetime.strptime('%s/%s/%s 00:00'%(cur_day,cur_month,cur_year), '%d/%m/%Y %H:%M')
generate_files(d1,d2)
