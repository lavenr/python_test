# import requests
# import urllib3
# urllib3.disable_warnings()
#
# url  = "https://dev.hypeloves.com/account/match"
# headers = {"Content-Type" :"application/x-www-form-urlencoded",
#            "Authorization":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsb2dpblR5cGUiOiJsb2dpbiIsImxvZ2luSWQiOiIxNjMwNDI2MzkzNDU5Mzk2NjA5Iiwicm5TdHIiOiIzOHY4NGdvcDRrM21HZmhMN1BVbEtLUTdmVGlib2VudSIsInVzZXJUeXBlIjoidXNlciIsImF1ZGl0TW9kZSI6ZmFsc2V9.87ntTYuZx8MW-T88jDAPoD7ZtYCuG9JoMTqrFt8nDJU"}
# r = requests.post(url=url,headers=headers,verify=False)
# print(r.status_code)


# number = 7
# guess = "A"
# print("数字猜谜游戏!")
# while guess != number:
#     guess = int(input("请输入你猜的数字："))
#
#     if guess == number:
#         print("恭喜，你猜对了！")
#     elif guess < number:
#         print("猜的数字小了...")
#     elif guess > number:
#         print("猜的数字大了...")


# num = int(input("请输入一个数字："))
# if num%2==0:
#     if num%3==0:
#         print("你输入的数字可以整除2和3")
#     else:
#         print("你输入的数字只能整除2，不能整除3")
# else:
#     if num%3==0:
#         print("你输入的数字只能整除3，不能整除2")
#     else:
#         print('你输入的数字不能整除2和3')




# a = 1
# while a<10:
#     print(a)
#     a+=2

# n = 100
# sum = 0
# counter =1
# while counter <=n:
#     sum= sum +counter
#     counter+=1
# print("1到%d之和为：%d"%(n,sum)) #%d是字符串格式化的占位符，第一个%d代表的是n,第二个代表的sum


# var =1
# while var ==1:
#     num = int(input("请输入一个数字："))
#     print("你输入的数字是：",num)
# print('good bye')
#这种属于无限循环，用于服务端在客户端实时请求时

#
# count = 0
# while count<5:
#     print(count,"小于 5")
# #     count +=1
# # else:
# #     print(count,"大于或等于5")
# sites = ["Baidu", "Google","Runoob","Taobao"]
# for site in sites:
#     print(site)
# for number in range(9):
#     print(number)

# for i in range(6):
#     print(i)
# else:
#     print("end")

# sites = ["Baidu", "Google","Runoob","Taobao"]
# for i in sites:
#     if i =="Google":
#         print("菜鸟")
#         break
#     print('循环数据'+i)
# else:
#     print('没有完成循环数据')
# print('完成循环!')

# a = ['Google', 'Baidu', 'Runoob', 'Taobao', 'QQ']
# for i in range(len(a)):
#     print(i,a[i])

# for i in range(6):
#     print(i)



# n = 10
# a, b=0,1
# for i in range(n):
#     print(b,end=" ")
#     a,b = b,a+b

# a,b =0,1
# while b < 1000:
#     print(b,end=',')
#     a,b = b,a+b



# python 推导式
# 列表推导式：
# names = ['Bob', 'Tom', 'alice', 'Jerry', 'Wendy', 'Smith']
# new_names = [name.upper() for name in names if len(name)>3]
# print(new_names)
#
# j = [i for i in range(30) if i %3 ==0]
# print(j)

# list=[1, 2, 3, 4, 5]
# new_list = list+[6,7,8,9]
# print(new_list)
# print(new_list[0])

# 字典推导式：
# listdemo = ['Google','Runoob', 'Taobao']
# newdict = {key:len(key) for key in listdemo}
# print(newdict)
#
# dic = {x:x**2 for x in (2,4,6)}
# print(dic)
# print(type(dic))

# 集合推导式：




































