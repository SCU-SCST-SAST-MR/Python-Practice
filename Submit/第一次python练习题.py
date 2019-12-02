import re
def func1(k, i):
    return len([p for p in str(k) if int(p)<=i])

def func2(n):
    z = [p for p in range(2, 100) if 0 not in [p % d for d in range(2, p)]]
    lst = []
    s = '{}='.format(n)
    while n > 1:
        for i in z:
            if n % i == 0:
                lst.append(i)
                n //= i
                break
    for i in sorted(list(set(lst))):
        s += '{}^{}*'.format(i, lst.count(i))
    return s.rstrip('*')


def func3(lst, v):
    lst = [i for i in lst if sum(map(int, list(str(i)))) < v]
    lst.sort(reverse=True)
    return lst


def func4(k):
    return len(list(set(str(k))))


def func5(lst):
    a = [i for i in lst if i % 2 == 1]
    b = [i for i in lst if i % 2 == 0]
    a.sort()
    b.sort(reverse=True)
    return a + b


def func6(s):
    con = re.findall(r'[(](?:[-][\d]|[\d])[,](?:[-][\d]|[\d])[)]', s)
    con = list(map(eval, con))
    con.sort(key=lambda z: ((list(z)[0]) ** 2 + (list(z)[1]) ** 2, -list(z)[1]))
    return con


def func7(s):
    a = s.split(' ')
    d = dict(zip(a, list(map(lambda x: a.count(x), a))))
    lst = sorted(d.items(), key=lambda x: x[1], reverse=True)
    lst1 = [i[0] for i in lst]
    return lst1[:3]


if __name__ == '__main__':
    print(func1(23789,5))
    print(func2(84))
    print(func2(56))
    print(func3([1234,2345,5678,8907],15))
    print(func4(23389))
    print(func5([1,4,7,3,2,10]))
    print(func6("input(2,3),hello(word,world)and(9,8)"))
    print(func6("(-3,4)(4,-3)(-4,-3)(3,4)"))
    print(func7("hello hi hello apple"))
    print(func7('a'))