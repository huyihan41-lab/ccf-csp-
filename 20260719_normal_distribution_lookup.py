n=int(input())
for i in range(n):
    a,b,c=list(map(int,input().split()))
    s=(c-a)*100//b#/号出来必是浮点数 整数需用//
    x=s//10+1
    y=s%10+1
    print(x,y)#不缩进会只显示最后一个结果
    
