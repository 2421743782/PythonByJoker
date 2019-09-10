# #1.几何学：一个五边形的面积
# import math
# r = float(input('请输入五边形的半径：'))
# s = 2*r*math.sin(math.pi/5)
# Area = 5*s*s/(4*math.tan(math.pi/5))
# print('五边形面积为:%.2f'%(Area))



# #2.大圆距离
# import math
# x1,y1 =eval(input('请输入第一个点的经度和纬度：'))
# x2,y2 =eval(input('请输入第二个点的经度和纬度：'))
# radius = 6371.01
# x11 = math.radians(x1)
# y11 = math.radians(y1)
# x22 = math.radians(x2)
# y22 = math.radians(y2)
# d = radius*math.acos(math.sin(x11)*math.sin(x22)+math.cos(x11)*math.cos(x22)*math.cos(y11-y22))
# print('两点之间距离%fkm'%d)




# #3.五角形的面积
# import math
# s = float(input('请输入五角形的边长：'))
# Area = (5*s*s)/(4*math.tan(math.pi/5))
# print('五角形的面积为：%f'%Area)




# #4.一个正多边形的面积
# import math
# s = float(input('请输入正多边形的边长：'))
# n = float(input('请输入多边形有几条边：'))
# Area = (n*s*s)/(4*math.tan(math.pi/n))
# print('正多边形的面积为：%f'%Area)



# #5.找出ASCII码的字符3
# a = int(input('请输入一个ASSCII码(0-127):'))
# print(chr(a))


# #6.工资表
# name = input('Enter employee\'s name:\000\000') 
# number = int(input('Enter number of hours worked in a week:\000\000')) 
# pay = float(input('Enter hourly pay rate:\000\000')) 
# federal = float(input('Enter federal tax withholding rate:\000\000')) 
# state = float(input('Enter state tax withholding rate:\000\000')) 
# print('Employee Name:\000'+name) 
# print('Hours worked:\000%.1f'%(float(number))) 
# print('Pay Rate:\000$'+str(pay)) 
# print('Gross Pay:\000$'+str(number*pay)) 
# print('Deductions:\n\000Federal Withholding(20.0%):\000$'+str(number*pay*0.2)+'\n\000State Withholding(9.0%):\000$'+ 
# str(number*pay*0.09)+'\n\000Total Deduction:\000$%.2f'%((number*pay*0.2)+(number*pay*0.09))) 
# print('Net Pay:\000$%.2f'%(((number*pay)-((number*pay*0.2)+(number*pay*0.09))))) 



# #7.反向数字
# a = input('请输入一个四位数整数：')
# print(a[::-1])


# #8.加密
# import hashlib
# m = hashlib.md5()
# a = input('请输入字符串：')
# m.update(bytes(a,encoding='utf8'))
# with open('password.txt','w')as file:
#     file.write(m.hexdigest())
# print(m.hexdigest())


##################################################################################################################################################


# #1.解一元二次方程
# import math
# a = input('请输入一个a值：')
# b = input('请输入一个b值：')
# c = input('请输入一个c值：')
# panbie = (float(b)*float(b))-(4*float(a)*float(c))
# if panbie>0:
#     x1 = -(-float(b)+math.sqrt(panbie))/2*float(a)
#     x2 = -(-float(b)-math.sqrt(panbie))/2*float(a)
#     print('The roots are %.6f and %.6f'%(x1,x2))
# elif panbie ==0:
#     x1 = (-float(b)+math.sqrt(panbie))/2*float(a)
#     print('The root is %.2f'%(x1))
# elif panbie < 0:
#     print('The equation has no real roots')



# #2.学习加法
# import random
# a = random.randint(0,100)
# b = random.randint(0,100)
# sum_ = int(input('请输入猜测数字：'))
# if sum_==a+b:
#     print('True')
# else:
#     print('False')




# #3.找未来数据
# day = int(input('Enter today\'s day:'))
# number = int(input('Enter the number of days elapsed since today:'))
# day_list=['Sunday','Monday','Tuesday','Wednesday','Thursday','Firday','Saturday']
# sum_ = day+number
# zhou = sum_ % 7
# print('Today is\000'+day_list[day]+'\000and the future day is\000'+day_list[zhou])



# #4.
# def start():
#     a,b,c = map(int,input('请输入三个整数：').split(','))
#     list1 = [a,b,c]
#     math(list1)
#     print(list1)
  
# def math(list1):
#     return list1.sort()
# start()



# #5.比较价钱
# weight1,price1 = input('Enter weight price for package 1:\000').split(',')
# weight2,price2 = input('Enter weight price for package 2:\000').split(',')

# num1 = float(price1)/float(weight1)
# num2 = float(price2)/float(weight2)
# if num1 < num2:
#     print('Package 1 has the better price.')
# else:
#     print('Package 2 has the better price.')






# #6.天数
# def start():
#     year,month = map(int,input('输入年和月：').split(','))
#     math(year,month)
	
# def math(year,month):
#     list1 = [1,3,5,7,8,10,12]
#     if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#         if month == 2:
#             print('这个月有29天')
#         elif month in list1:
#             print('这个月有31天')
#         else:
#             print('这个月有30天')
#     else:
#         if month == 2:
#             print('这个月有28天')
#         elif month in list1:
#             print('这个月有31天')
#         else:
#             print('这个月有30天')


# #7.硬币游戏
# def start():
#     x=int(input('请输入你的猜测（1是正，2是反）：'))
#     math(x)

# def math(x):
#     a = random.randint(1,2)
#     if x == a:
#         print('你猜错了')
#     else:
#         print('你猜对了')

# start()





# #8.猜拳
# import random

# def start():
#     U_res = int(input('0:石头,1:剪刀,2:布>>>'))
#     math(U_res)

# def math(U_res):  
#     C_res = random.randint(0,2)
#     if C_res == U_res:
#         print('平局')
#     else:
#         if C_res == 0 and U_res == 1:
#             print('电脑赢了 ')
#         elif C_res == 1 and U_res == 2:
#             print('电脑赢了 ')
#         elif C_res == 2 and U_res == 0:
#             print('电脑赢了 ')
#         else:
#             print('你赢了 ')

# start()



# #9.
# def main(year,m,d):
#     a = ['周六','周日','周一','周二','周三','周四','周五']
#     if m == 1:
#         m = 13
#         year = year - 1
#     if m ==2:
#         m = 14
#         year = year - 1
#     h = int(d+((26*(m+1))//10)+(year%100)+((year%100)/4)+((year//100)/4)+5*year//100)%7
#     day = a[h]
#     print('那一天是一周中的:%s' %day)
# def Start():
#     year = int(input('输入哪一年:'))
#     m = int(input('输入月份1-12:'))
#     d = int(input('输入月份第几天1-31:'))
#     main(year,m,d)
# Start()




# #10
# def chou():
#     import numpy as np
#     daxiao=np.random.choice(['A','2','3','4','5','6','7','8','9','10','J','Q','K'])
#     huase=np.random.choice(['梅花','红桃','方块','黑桃'])
#     print('你选择的牌是  %s , %s'%(huase,daxiao))
# def Start():
#     a = input("是否决定抽牌y/n:")
#     if a == 'y':
#         chou()
#     else:
#         pass
# Start()



# #11.回文数
# Number = input('请输入一个数：')
# a = Number[::-1]
# if a==Number:
#     print('这个数是回文数')
# else:
#     print('这个数不是回文数')



# #12.
# def main(a,b,c):
#     if a+b>c and a+c>b and b+c>a:
#         L = a+b+c
#         print("其周长为",L)
#     else:
#         print("不是三角形三条边") 
# def Start():
#     a,b,c = map(float,input('请输入三条边长（逗号分隔）：').split(','))
#     main(a,b,c)
# Start()





############################################################################################






# #1
# def main(x,zheng,fu,i,sum1):
#     while x!=0:
#         x = int(input('输入一个整数，以输入值0来结束：'))
#         if(x>0):
#             zheng += 1
#         elif(x<0):
#             fu += 1
#         i += 1
#         sum1 = sum1 + x
#     if sum1 != 0:
#         xxx = sum1/(i-1)
#         print('输入的正数有%d个，输入的负数有%d个，这组数的和为%d，这组数的平均数为%.2f'%(zheng,fu,sum1,xxx))
#     else:
#         print('结束')
#         return   
# def start():
#     x = 1
#     zheng = 0
#     fu = 0
#     i = 0
#     sum1 = 0
#     main(x,zheng,fu,i,sum1)
        
# start()



# #2计算未来学费
# def main(money,sum1):
#     for i in range(1,14):
#         money = money * 0.05 + money
#         if i ==10:
#             print('十年之后的学费：%.2f'%money)
#         if i >= 10: 
#             sum1 += money
#     print('十年后大学四年的总学费为：%.2f'%sum1)

# def start():
#     money = 10000
#     sum1 = 0
#     main(money,sum1)

# start()



# #4.被5、6同时整除的数
# def main(geshu):
#     for i in range(100,1001):
#         if i%5 == 0 and i%6 == 0:
#             print(i,end=' ')
#             geshu += 1
#             if geshu % 10 == 0:
#                 print('\n')
# def start():
#     geshu = 0
#     main(geshu)    

# start() 



# #5.while循环找满足条件的数
# def main():
#     n = 0
#     m = 0
#     math(n,m)
# def math(n,m):
#     while n**2 <= 12000:
#         n += 1
#     print('n的平方大于12000的最小整数n为：%d'%n)

#     while m**3 < 12000:
#         m += 1
#     print('n的立方大于12000的最大整数n为：%d'%(m-1))
# main()




# #7.演示消除错误
# def start():
#     sum1 = 0
#     sum2 = 0
#     main(sum1,sum2)

# def main(sum1,sum2):
#     for i in range(1,50001):
#         sum1 += 1/i
#         i += 1
#     print('从左向右计算为：',sum1)
#     for i in range(50000,0,-1):
#         sum2 += 1/i
#         i -= 1
#     print('从右向左计算为：',sum2)

# start()



# #8.数列求和
# sum1 = 0
# for i in range(3,100,2):
#     sum1 += (i-2)/i
# print('数列的和为：',sum1) 



# #9.计算π
# def start():
#     pi = 0
#     i = int(input('输入i的值：'))
#     main(pi,i)

# def main(pi,i):    
#     for j in range(1,i+1):
#         pi += 4 * ((-1)**(1+j)/(2*j-1))
#     print('π的值为：%f'%pi)

# start()




# #10.完全数
# for i in range(1,10000):
#     x = 0
#     for j in range(1,i):
#         if i % j == 0:
#             x += j
#     if x == i:
#         print('10000以下的完全数有：%d'%x)



# #11.组合
# list1 = []
# for i in range(1,8):
#     for j in range(1,8):
#             if i != j and sorted([i,j]) not in list1:
#                 list1.append([i,j])
# print('所有可能的组合为：',list1)
# print('组合总个数为：',len(list1))



# #12.计算均值和方差
# import numpy as np

# arr=[]
# i = 1
# while i <= 10:
#     x  = float(input('输入十个数字：'))
#     arr.append(x)
#     i += 1
# #求均值
# arr_mean = np.mean(arr)
# #求方差
# arr_var = np.var(arr)
# print("平均值为：%f" % arr_mean)
# print("方差为：%f" % arr_var)