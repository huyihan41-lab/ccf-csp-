n,m=map(int,input().split())#输入两个用空格隔开的数字，分别放进 n 和 m
a=[0]+list(map(int,input().split()))#map(要执行的函数, 一组数据):int("2")   # 2
x_elements=[]
x_xors=[]
for _ in range(m):
    data=list(map(int,input().split()))
    size=data[0]
    elements=data[1:]
    x=0#0对任何数的异或都为其本身
    for number in elements:
        x=x^a[number]
    x_elements.append(elements)
    x_xors.append(x)
for i in range(m):
    data=list(map(int,input().split()))# 意思是把新的东西放进 data 盒子里。盒子里原来的内容会被替换。
    size=data[0]#size、elements、x 也都是同一个变量名反复使用，每次循环都会被新值覆盖。 那之前的 elements 为什么没丢？因为在覆盖之前，程序执行了：S_elements.append(elements)
    elements=data[1:]
    x=0
    for number in elements:
        x=x^a[number]
    real_equal=x_elements[i]==elements#append(elements) 把每个集合存进大列表；S_elements[i] 再把其中第 i 个集合取出来  S_elements = [[3], [3, 4], [3, 5]]
    real_xors=x_xors[i]==x
    if real_equal==real_xors:
        print('correct')
    else:
        print('wrong')

    

