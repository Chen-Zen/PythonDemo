
#import keyword

# print(keyword.kwlist)

# print(2+2)

# 注释
# a,b=0,1

# while b<10:
#   print(b)
#   a,b=b,a+b

# a,b,c,d,=20,5.5,True,4+3j

# print(type(a),type(b),type(c),type(d))

# 转义
#s='Yes,he desn\'t'

# print(s)

# print(s,type(s),len(s))

# 不转义
# print('c:\some\name')

# print(r'C:\some\name')

# 字符串索引
'''word='Python'
print(word[0],word[5])

print(word[-1],word[-6])'''

# 列表
'''a=['him',25,100,'her']
print(a)

a=[1,2,3,4,5]
a+[6,7,8]

print(a)

a=[1,2,3,4,5]
a[0]=9
print(a[0])

a[2:5]=[11,12,13]#新增
# print(a)
a[2:4]=[] #删除
print(a)'''

# Tuple(元组)
'''
a=(1998,2018,'physics','math')
print(a,type(a),len(a))
'''
# while 循环
'''
i = 100
sum = 0
counter = 1
while counter <= i:
    sum += counter
    counter += 1
    print("Sum of q until %d: %d" % (i, sum))
'''
# for 循环
'''
languages = ["C", "C++", "C#", "Python"]
for x in languages:
    print(x)
'''
# for break
'''
edibles = ["ham", "spam", "eggs", "nuts"]
for food in edibles:
    if food == "spam":
        print("No more spam please!")
        break
    print("Great,delicious"+food)
else:
    print("I am so glad: No spam!")
    print("Finally, I finished stuffing myself")
'''

# range()函数
# 0-5
'''
for i in range(5):
    print(i)
'''
# 区间
'''
for i in range(5, 9):
    print(i)
'''
# 也可以使range以指定数字开始并指定不同的增量(甚至可以是负数;有时这也叫做'步长')
'''
for i in range(0, 10, 3):
    print(i)
'''
# 负数
'''
for i in range(-10, -100, -30):
    print(i)
'''
# 结合range()和len()函数以遍历一个序列的索引
'''
a = ["Mary", "had", "a", "little", "lamb"]
for i in range(len(a)):
    print(i, a[i])
'''
# 可以使用range()函数来创建一个列表
a = list(range(5))
for i in a:
    print(a[i])
