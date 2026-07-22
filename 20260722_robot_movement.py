n,k=map(int,input().split())
for _ in range(k):
   # t=list(map(int,input().split()))这样会报错因为我要取的是ffrrbbll字符串而这样子处理会是整数
  # 所以要分开来写
    x,y,t=input().split () #split（）就是列表了
    x=int(x)
    y=int(y)
    #错误的：q,z=min(s,n),min(k,n)
    #a=t.count('f')
    #b=t.count('b')
    #c=t.count('l')
    #d=t.count('r')
    #xlabel=min(q+d,n)-c
    #ylabel=min(z+a,n)-b
    #print(xlabel,ylabel)#不缩进只产生最后一组结果
    for i in t:
        if i =='f':
            if y < n:
                y+=1
        elif i =='b':
            if y >1:
                y-=1
        elif i=='l':
            if x > 1:
                x-=1
        else:
            if x < n:
                x+=1
    print(x,y)
        
            