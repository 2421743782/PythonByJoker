# #1
# C=float(input('请输入一个摄氏温度：'))
# F=(9/5)*C+32
# print('摄氏温度转华氏温度为：%.2f'%(F))


# #2
# r=float(input('请输入半径的数值：'))
# l=float(input('请输入高的数值：'))
# area=r*r*3.14
# volume=area*l
# print('圆柱的底面积为：%.2f'%area)
# print('圆柱的体积为：%.2f'%volume)



# #3
# feet=float(input('英尺转换成米数，请输入英尺：'))
# meters=feet/0.304841
# print('英尺转换成米数为：%.4f'%meters)


# #4
# M=float(input('请输入水量（千克）：'))
# initialTemperature=float(input('水的初始温度：'))
# finalTemperature=float(input('水的最终温度：'))
# Q=str(M * (finalTemperature - initialTemperature) * 4184)
# print('加热所需要的能量：'+Q)


# ##5
# blance=float(input('差额：'))
# interest_rate=float(input('年利率：'))
# interest=blance*(interest_rate/1200)
# print('利息为：%.5f'%interest)



# #6
# v0=float(input('请输入初始速度：'))
# v1=float(input('请输入末速度：'))
# t=float(input('请输入速度变化所占用的时间：'))
# a=(v1-v0)/t
# print('平均加速度为：%.4f'%a)




#7
mouth=['1','2','3','4','5','6','7']
shumu=0
monthly=float(input('Enter the monthly saving amount:'))
for i in mouth:
    if int(i)<=6:
        shumu=(shumu+monthly)*(1+0.00417)
    else:
        print(shumu)


# #8
# Number=input('请在0-1000之间输入一个数值：')
# a=int(Number[0])
# b=int(Number[1])
# c=int(Number[2])
# sum=str(a+b+c)
# print('各位数字之和为：'+sum)




