import re,string
def func1(s):
    return re.sub('(.)\\1*',lambda m:m.group(1)+str(len(m.group(0))),s)
def func2(s,k):
    return bool(re.search('(.{%d,}).+\\1'%k,s))
def func3(s):
    return int(re.sub('(x+)',lambda m:str(len(m.group(1))),s))==2 or 0 not in [int(re.sub('(x+)',lambda m:str(len(m.group(1))),s))%i for i in range(2,int(re.sub('(x+)',lambda m:str(len(m.group(1))),s)))]
def func4(s):
    return bool(re.match(s[-1:0:-1],s))
def func5(s):
    alist=re.findall('<(.*?).*?( href=)"(.*?)">(.*?)</\\1>',s)
    return {alist[i][-1]:alist[i][-2] for i in range(len(alist))}
def func6(s):
    alist=re.findall('<(.*?)>(.*)?</\\1>',s)
    return [(alist[2*i][1],alist[2*i+1][1]) for i in range(int(len(alist)/2))]
if __name__ == '__main__':
    # print(func1('aaasssddd'))
    # print(func2('allochirally',3))
    # print(func3('xx'))
    # print(func3('xxx'))
    # print(func3('xxxxx'))
    # print(func4('321xxxxxxxxx123'))

    print(func6("""
<P>Mr. Bennet replied that he had not. </P>
<P>班纳特先生回答道，他没有听说过。</P>
<P>"But it is," returned she; "for Mrs. Long has just been here, and she told me all about it." </P>
<P>“的确租出去了，”她说，“朗格太太刚刚上这儿来过，她把这件事的底细，一五一十地告诉了我。”</P>
"""))
    pass