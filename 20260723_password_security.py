n=int(input())
for _ in range(n):
    ch=input()
    alpha=False
    digit=False
    special=False
    repeat=False
    for i in ch:
        if i.isalpha():
            alpha=True
        elif i.isdigit():
            digit=True
        elif i in'*#':
            special=True
        if ch.count(i)>2:# if+elif是一堆情况选一个 if又是一个独立的事件
            repeat=True#反过来写<=2不行 因为只要有一个比它小 那就是True而做不到每个
    if alpha and digit and special:
        if repeat:
            print(1)
        else:
            print(2)
    else:
        print(0)