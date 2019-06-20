

def get_num(target_num):
    num=0
    if len(list(str(target_num))) == 1:
        num = target_num
    elif len(list(str(target_num))) == 2:
        num = target_num % 10 #取余　个位
        num += target_num // 10 #地板除取整取整　十位
    elif len(list(str(target_num))) == 3:
        num = target_num % 10 #取余　个位
        num += target_num // 100 #地板除取整　百位
        num += (target_num % 100) // 10 #取余数后两位再地板除取整　十位
    elif len(list(str(target_num))) == 4:
        num = target_num % 10
        num += target_num // 1000 #千位
        num += (target_num % 100) // 10 #十位
        num += (target_num // 100) % 10 #百位
    return num

def list_num(target_num):
    num = 0
    for i in list(str(target_num)):
        num += int(i)
    return num

if __name__=="__main__":
    a=get_num(38)
    b=list_num(38)
    print(a)
    print(b)