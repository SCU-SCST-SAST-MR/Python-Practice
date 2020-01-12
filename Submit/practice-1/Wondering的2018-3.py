import re
def func1(y,m,d):
    if m==1:
        if d in range(1,32):
            return d
        else:
            return -1
    if m==2:
        if (y % 4 == 0 and y % 100 != 0 or y % 400 == 0) and d in range(1,29):
            return 31+d
        if not (y % 4 == 0 and y % 100 != 0 or y % 400 == 0) and d in range(1,28):
            return 31+d
        else:
            return -1
    if m in [3,5,7,8,10,12] and d in range(1,32) or m in[4,6,9,11] and d in range(1,31):
        dig=0
        i=1
        while i<m:
            if i in [1,3,5,7,8,10,12]:
                dig+=31
            if i==2:
                dig+=29
            else:
                dig+=30
            if (y % 4 == 0 and y % 100 != 0 or y % 400 == 0) and m != 1:
                return dig
            else:
                return dig-1
    else:
        return -1
def func2(m,n):
    if m<0 or n<0:
        return None
    else:
        for i in range(m+1):
            if (n-i*2)%4==0 and (n-i*2)/4+i==m:
                if i>=0 and (n-i*2)/4>=0:
                    return (i,int((n-i*2)/4))
                else:
                    return None
def func3(lst):
    if len(lst)==1:
        return False
    if len(lst)==2:
        return True
    else:
        alist=list(sorted(lst))
        diff=alist[1]-alist[0]
        for i in range(1,len(alist)):
            if alist[i]-alist[i-1]!=diff:
                return False
        else:
            return True
def func4(lst):
    for i in lst:
        if type(i)!=int:
            return None
    else:
        alist=list(sorted(lst))
        if len(lst)%2==0:
            return int((alist[int(len(alist)/2)]+alist[int(len(alist)/2)-1])/2)
        else:
            return alist[int((len(alist)-1)/2)]



def func5(s):
    alist,blist=s.lower().split(),[]
    adict={'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'zero':0}
    for i in alist:
        blist.append(str(adict[i]))
    return '"'+''.join(blist)+'"'
def func6(a,b,c,d):
    return len(set([x/y for x in range(a,b+1) for y in range(c,d+1)]))
def func7(s1,s2,n):
    while len(s1)%n!=0:
        s1+=' '
    return re.sub('(.{%d})'%n,'\g<0>'+s2,s1)
def func8(s):
    return re.sub("<([a-zA-Z0-9_]*)>",lambda m:'['+m.group(1).upper()+'-'+str(len(m.group(1)))+']',s)

if __name__=='__main__':
    print(func1(2019,3,1))
    print(func2(100,100))
    print(func3([33,-7,3,13,43,53,23]))
    print(func3([19,-1,100]))
    print(func4([19,-1,100]))
    print(func4([19,-1,1000,101]))
    print(func5('one one four'))
    print(func6(10, 10, 1, 10))
    print(func7('abcd','#',1))
    print(func7('abcd', '##', 2))
    print(func7('abcd', '##', 5))
    print(func8('president<4t>'))
    print(func8('he defended <_abc>, his decision to <43>'))
    pass