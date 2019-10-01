or _ in range(int(input())):
    a,b=map(str,input().split())
    l1=[]
    l2=[]
    p=int(a)
    q=int(b)
    f=0
    if p*q<0:
        f=1
    for i in range(len(a)):
        if a[i]=='-':
            continue
        if a[i]!='0':
            l1.append(a[i]+'0'*(len(a)-i-1))
 
    for i in range(len(b)):
        if b[i]=='-':
            continue
        if b[i]!='0':
            l2.append(b[i]+'0'*(len(b)-i-1))
 
    flag=True
    if f==1:
        print(0,'x',0,end=" ")
        flag=False
    for i in l1:
        for j in l2:
            if flag:
                print(i,'x',j,end=" ")
                flag=False
            else:
                if f==0:
                    print('+',i,'x',j,end=" ")
                else:
                    print('-',i,'x',j,end=" ")
                    
 
    print()