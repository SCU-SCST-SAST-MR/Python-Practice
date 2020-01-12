def func1(k,i):
    alist=[]
    for j in list(str(k)):
        if int(j)<=i:
            alist.append(j)
    return len(alist)
def func2(n):
    nu=int(n)
    alist=[2]
    for j in range(2,nu):
        for k in range(2,j):
            if j%k==0:
                break
        else:
            alist.append(j)
    blist = list(set(alist))
    clist = []
    for t in range(nu):
        for k in blist:
            if nu%k==0:
                clist.append(k)
                nu=nu/k
    dlist=[]
    for i in clist:
        dlist.append(clist.count(i))
    elist=list(set(list(zip(clist,dlist))))
    hlist=[]
    for i in elist:
        hlist.append([i[0],i[1]])
    hlist.sort(key=lambda x:x[0])
    ilist=[str(n),'=']
    for i in hlist:
        ilist.append(str(i[0]))
        ilist.append('^')
        ilist.append(str(i[1]))
        ilist.append('*')
    del(ilist[-1])
    return str(''.join(ilist))

def func3(lst,v):
    alist=sorted([int(x) for x in lst if sum(map(int,list(str(x))))<v])
    return alist

def func4(k):
    alist=len(list(set([x for x in map(int,list(str(k)))])))
    return alist
def func5(lst):
    alist=list(sorted([x for x in lst if x%2!=0]))
    blist=list(sorted([y for y in lst if y%2==0],reverse=True))
    alist.extend(blist)
    return alist
def func6(s):
    alist=s.split('(')
    dlist=[]
    for ele in alist:
        blist=list(alist)
        clist=[]
        for i in ele:
            if i!=')':
                clist.append(i)
            if i.isalpha() or i==')':
                break
        dlist.append(''.join(clist))
    for i in dlist:
        for j in list(i):
            # if j.isalpha():
            #     dlist.remove(i)
            if ord(j) not in range(48,58) and j!=',':
                dlist.remove(i)
    elist=[]
    for i in dlist:
        ele=i.split(',')
        elist.append((int(ele[0]),int(ele[1])))
    elist.sort(key=lambda x:x[0]**2+x[1]**2)
    return elist

def func7(s):
    lst = s.split()
    if len(lst) >= 3:
        alst = []
        for i in lst:
            alst.append(lst.count(i))
        blst = list(zip(alst, lst))
        clst = list(set(blst))
        clst.sort(key=lambda x: x[0], reverse=True)
        for i in range(2):
            if clst[i][0]==clst[i+1][0]:
                for j in range(len(list(clst[i][1]))):
                    if ord(list(clst[i][1])[j])<ord(list(clst[i+1][1])[j]):
                        clst[i],clst[i+1]=clst[i+1],clst[i]
        return [clst[0][1], clst[1][1], clst[2][1]]
    elif len(lst) == 2:
        if lst[0] == lst[1]:
            return [lst[0]]
        elif lst[0] != lst[1]:
            lstt = []
            lsttt = []
            for i in list(str(lst[0])):
                lstt.append(ord(i))
            al = sum(lstt)
            for i in list(str(lst[1])):
                lsttt.append(ord(i))
            bl = sum(lsttt)
            return [chr(max(al, bl))]
    elif len(lst)==1:
        return lst
if __name__ == "__main__":
    print(func2(66))
    print(func2(56))
    #print(func7('hello hi hello apple'))
    # print(func6('input(1,1)asd(1,22),fddu(2,3)(1,4)'))
    #print(func6('fd(1,11)sd(1,4)fjsda(1,3)fds'))
    #print(func7('al'))
    #print(func3([1234,2345,5678,8907],15))
    #print(func4(23389))
    #print(func5([1,4,7,3,2,10]))
    pass