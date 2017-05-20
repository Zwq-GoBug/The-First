# 上传至github的python程序
import random
def rand_int(end_number):
    temp = random.randint(0,end_number)
    return temp
theEndnum = int( input("请输入一个数：") )
printRandnumber = rand_int(theEndnum)
print(printRandnumber)


