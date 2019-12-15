def func1(k,i):
    alist=[]
    for j in list(str(k)):
        if int(j)<=i:
            alist.append(j)
    return len(alist)


def func2(n):
    s = str(n) + "="
    dic = {}
    while(n>1):
        for i in range(2,n+1):
            if n%i==0:
                dic[i]=dic.get(i,0)+1
                n//=i
                break
    a = sorted(dic.items(), key=lambda x: x[0])
    for i in a:
        s += (str(i[0]) + "^" + str(i[1]) + "*")
    return s[:-1]


def func3(lst,v):
    return sorted([int(x) for x in lst if sum(map(int,list(str(x))))<v])


def func4(k):
    return len(list(set([x for x in map(int,list(str(k)))])))


def func5(lst):
    alist=list(sorted([x for x in lst if x%2!=0]))
    blist=list(sorted([y for y in lst if y%2==0],reverse=True))
    alist.extend(blist)
    return alist


def func6(s):
    a='我还不会'
    return a


def func7(s):
    a = s.split()
    dic = {}
    for i in a:
        dic[i] = dic.get(i, 0) + 1
    b = sorted(dic.items(), key=lambda e: (e[1], e[0]), reverse=True)
    return [b[i][0] for i in range(len(b))][0:3]


if __name__ == "__main__":
    print(func6((2,3)))
    pass