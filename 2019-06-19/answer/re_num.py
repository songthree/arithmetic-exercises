

def reverse(num):
    if -10<num<10:
        return num
    elif num>9:
        str_num=str(num)[::-1].lstrip('0')
        int_num=int(str_num)
        return int_num
    elif num<-9:
        num=str(num)[1:]
        str_num = str(num)[::-1].lstrip('0')
        int_num = int('-'+str_num)
        return int_num
