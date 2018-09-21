#Parker Gowans
#9/18
#Clock
import time
import calendar
x = calendar.timegm(time.gmtime())
print(x)
x=x*1000
print(x)
def clock():
    total_mil_sce = calendar.timegm(time.gmtime())* 1000
    total_sec = total_mil_sce // 1000
    cur_sec = total_sec % 60
    total_min = total_sec // 60
    cur_min = total_min % 60
    total_hrs = total_min // 60
    cur_hrs = total_hrs % 24
    return cur_hrs,cur_min,cur_sec

    

while True:
    h,m,s = clock()
    print(h,m,s)

