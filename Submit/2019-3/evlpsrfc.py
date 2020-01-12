import re


def func1(x, y):
    return [1, 0, -1][min(2, max(abs(x), abs(y)))]

def func2(d, l, r):
    if 0 <= d <= 9 and l < r:
        return ''.join(map(str, range(l, r + 1))).count(str(d))

def func3(lst):
    f = lambda n: str(n)[0] + str(n)[-1]
    s = ''.join(map(f, lst))
    lst = re.split('\B(?=[2357])|(?<=[2357])\B', s)
    return list(map(int, lst))

def func4(A):
    m = len(A)
    B = [[0 for j in range(m)] for i in range(2 * m - 1)]
    for i in range(m):
        for j in range(m):
            B[i + j][j - max(0, i + j - m + 1)] = A[i][j]
    return B

def func5(w):
    if re.search('[A-Z]', w):
        return w.title()
    else:
        return w.title()[:-1] + w[-1].upper()

def func6(s):
    pattern = '(?<=\w)\w{4,}(?=\w)'
    repl = lambda m: '*' * len(m[0])
    string = ' '.join(re.findall('[\da-zA-Z]+', s))
    return re.sub(pattern, repl, string)

def func7(words, chars):
    d = dict([[c, chars.count(c)] for c in set(chars)])
    f = lambda s: all(d.get(c, 0) >= s.count(c) for c in set(s))
    return sum(map(f, words))

def func8(lst):
    f = lambda t: re.match('^\d{9}$', t[0]) and 1 <= t[1] <= 3
    g = lambda t: (-t[1], t[0])
    d = dict()
    for stu in filter(f, lst):
        d[stu[0]] = d.get(stu[0], 0) + stu[1]
    return min(d.items(), key=g)


if __name__ == '__main__':
    print('[func1]')
    print(func1(0, 0))
    print(func1(1, 0))
    print(func1(2, 2))
    print('\n[func2]')
    print(func2(0, 0, 11))
    print(func2(1, 3, 4))
    print(func2(1, 4, 4))
    print(func2(12, 3, 6))
    print('\n[func3]')
    print(func3([1, 234, 5, 6, 7, 890]))
    print(func3([12, 34, 56, 78, 90]))
    print(func3([123]))
    print('\n[func4]')
    print(func4([[1,2,3], [4,5,6], [7,8,9]]))
    print(func4([[1,2], [3,4]]))
    print('\n[func5]')
    print(func5('wE'))
    print(func5('comPUtER'))
    print(func5('university'))
    print('\n[func6]')
    print(func6('hello ! world.,Computer. class,54,5w'))
    print(func6('one two:::three, FOUR.., five'))
    print(func6('worldcomputer.,'))
    print(func6('!=-,.'))
    print('\n[func7]')
    print(func7(['cat', 'bt', 'hat', 'tree'], 'atach'))
    print(func7(["hello","world","soochow"], 'welldonehoneyr'))
    print('\n[func8]')
    print(func8([('192740506',3), ('192740101',2), ('192740101',2)]))
    print(func8([('192740506',3), ('192740A01',2), ('192740101',3)]))
    print(func8([('19274056',3), ('192740A01',2), ('192740101',3)]))
    print(func8([('192740101',2), ('192740101',2)]))
