import re
# from requests import get

def func1(s):
    return re.sub(r'(\w)\1*',lambda x:x.group(1)+str(len(x.group(0))),s)

def func2(s,k):
    return bool(re.search(r'(\w{'+str(k)+r'}).*\1',s))

def func3(s):
    return not bool(re.match(r'^(xx+)\1+$',s))

def func4(s):
    return bool(re.match(r'^(.?)(.?)(.?)(.?)(.?)(.?)(.?)(.?)(.?)(.?).?\10\9\8\7\6\5\4\3\2\1$',s))

def func5(s):
    return {x[3]:x[2] for x in re.findall(r'<(?P<tag>\w+) [^>]*href=(?P<quote>[\"\'])([^>]+?)(?P=quote)[^>]*>((?:.|\n|\t)*?)</(?P=tag)>',s)}

def func6(s):
    return re.findall(r'<P>(.*?)</P>\n<P>(.*?)</P>',s)

if __name__=="__main__":
    with open("node.html") as f:
        html1=f.read()
    with open('func6.txt',encoding='utf-8') as f:
        html2=f.read()
    with open('func5.txt',encoding='utf-8') as f:
        html3=f.read()

    print('#1')
    print(func1('aaaabbbbbbbccd'))
    print(func1('aba'))
    print('#2')
    print(func2('allochirally',3))
    print(func2('gummage',2))
    print(func2('gummage', 1))
    print('#3')
    print(func3('xxxx'))
    print(func3('xx'))
    print(func3('x'*13))
    print(func3('x'*18))
    print('#4')
    print(func4('aba'))
    print(func4('abba'))
    print(func4('abccca'))
    print(func4('abcccba'))
    print('#5','='*100)
    print(*(f'{content} : {link}' for content,link in func5(html1).items()),sep='\n')
    print('  ','='*100)
    print(*(f'{content} : {link}' for content,link in func5(html3).items()),sep='\n')
    print('#6','='*100)
    print(*func6(html2),sep='\n')