
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
'''
a = list(range(5))
for i in a:
    print(a[i])
'''
# break和continue语句及循环中的else子句
# break语句可以跳出for和while的循环体。如果你从for或while循环中终止，任何对应的循环else块将不执行。
# continue语句被用来告诉Python跳过当前循环块中的剩余语句，然后继续进行下一轮循环。
# 循环语句可以有else子句;它在穷尽列表(以for循环)或条件变为假(以while循环)循环终止时被执行,但循环被break终止时不执行.如下查寻质数的循环例子:
'''
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, "equals", x, "*", n//x)
            break
    else:
        # 循环中没有找到元素
        print(n, "is a prime number")
'''

# 迭代器
# 迭代器是一个可以记住遍历的位置的对象。
# 迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结#束。迭代器只能往前不会后退。
# 迭代器有两个基本的方法：iter() 和 next()。
# 字符串，列表或元组对象都可用于创建迭代器：
'''
list = [1, 2, 3, 4]
it = iter(list)
print(next(it))
print(next(it))
print(next(it))
'''

# 迭代器对象可以使用常规for语句进行遍历：
'''
list = [1, 2, 3, 4]
it = iter(list)
for x in it:
    #print(x, end=" ")
    print(x)
'''
# 使用 next() 函数：
'''
import sys

list=[1,2,3,4]
it=iter(list)
while True:
    try:
        print(next(it))
    except StopIteration:
        sys.exit()
'''

# 生成器
'''
import sys
#生成器函数 - 斐波那契数列


def fibonacci(n):
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield a
        a, b = b, a+b
        counter += 1

# f是一个迭代器，由生成器返回生成
f = fibonacci(10)

while True:
    try:
        print(next(f), end=" ")
    except StopIteration:
        sys.exit()
'''

# Python 函数
# 函数的声明及调用

'''
def Say(n):
    print(n)


Say("w qu")


def area(width, height):
    return width * height


def print_welcome(name):
    print("Welcome", name)


print_welcome("Fred")
w = 4
h = 5
print("width =", w, " height =", h, " area =", area(w, h))
'''

# 函数变量作用域
# 定义在函数内部的变量拥有一个局部作用域，定义在函数外的拥有全局作用域。
# 通过以下实例，你可以清楚了解Python函数变量的作用域：


a = 4  # 全局变量


def print_func1():
    # 局部变量
    a = 17
    print("in print_func a = ", a)


def print_func2():
    print("in print_func a = ", a)


print_func1()
print_func2()
print("a = ", a)
