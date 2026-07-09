n=int(input())
ans=0
a = list(map(int, input().split()))
for i in a:
    x=bin(int(i))[2:]
    one=x.count('1')
    zero=x.count('0')
    if one==zero:
            ans+=1
        
print(ans)
        
        