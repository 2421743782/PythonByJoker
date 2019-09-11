# #1.数学方面：五角数
# def getPentagonalNumber(n):
#     count = 0
#     for i in range(1,n+1):
#         num = i * (3 * i-1)/2
#         #数字间以空格隔开
#         print("%d"%num,end = ' ')
#         count += 1
#         #每行显示10个
#         if count % 10 ==0:
#             print('\n')
# getPentagonalNumber(100)


# #2.求一个整数各个数字的和
# word = input('请输入整数：')
# j = len(word)
# list_num = []
# def main1(word):
#     global j
#     global list_num
#     for i in range(len(word)):
#         a = int(word)%10
#         word = str(int(word)//10)
#         list_num.append(a)
#         j -= 1
#         if j==0:
#             sum_= sum(list_num)
#             print(sum_)
# main1(word)


#3.对三个数排序
# def start():
#     a,b,c = map(int,input('请输入三个整数：').split(','))
#     list1 = [a,b,c]
#     math(list1)
#     print(list1)
# def math(list1):
#     return list1.sort()
# start()


# #5.显示字符
# count = 0
# ch1 = 73
# ch2 = 91
# def printChars(ch1,ch2):
#     global count
#     for i in range(ch1,ch2):
#         count += 1
#         print(chr(i),end = " ")
#         if count % 10 ==0:
#             print("\n")
# print(printChars(ch1,ch2))


# #6.一年的天数
# count = 1
# year1 = 2010
# year2 = 2021
# def numberOfDayslnAYear(year1,year2):
#     for i in range(year1,year2):
#         if i%4 ==0 and i%100 !=0 or i%400 == 0:
#             print(i,'年有366天，是闰年')
#         else:
#             print(i,'年有365天，是平年')
# print(numberOfDayslnAYear(year1,year2))


# #7.显示角
# def distance(x1,y1,x2,y2):
#     d=((x1-x2)**2+(y1-y2)**2)**0.5
#     print('两点间距离为：','%.2f'%d)
# distance(2,3,4,5)


#8.梅森素数




# #9.当前时间和日期
# import time
# def main():
#     localtime = time.asctime(time.localtime(time.time()))
#     print('本地时间和日期是:',localtime)
#     ticks = time.time()*1000
#     print('距离当前时间：',ticks)
# main()


#10.掷骰子
import random
def shaizi():
    a=random.choice([1,2,3,4,5,6])
    b=random.choice([1,2,3,4,5,6])
