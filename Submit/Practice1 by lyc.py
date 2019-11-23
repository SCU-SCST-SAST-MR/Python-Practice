import math
import re

def func1 (k,i):
	a = list(str(k))
	s = 0
	for j in a:
		if int(j) <= i:
			s += 1
	return s

def func2 (n):
	a = []
	b = []
	x = n
	while x > 1:
		for i in range(2,x+1):
			if x % i == 0:
				x = x // i
				a.append(i)
				break
	a.sort()
	d = list(str(i) for i in a)
	for i in d:
		b.append(i + "^" + str(d.count(str(i))))
	d = list(set(b))
	d.sort(key=b.index)

	return str(n) + "=" + "*".join(d)

def func3 (lst,v):
	lst2 = []
	for i in lst:
		b = list(str(i))
		s = 0
		for j in b:
			s += int(j)
		if s < v:
			lst2.append(i)
	return lst2

def func4 (k):
	return len(list(set(list(str(k)))))

def func5 (lst):
	return sorted(list(i for i in lst if i % 2 != 0)) + sorted(list(i for i in lst if i % 2 == 0))

def func6 (x):
	return sorted(map(eval,re.findall(r"\([-]*\d+,[-]*\d+\)",x)),key=lambda x: ((x[0]) ** 2 + (x[1]) ** 2, -x[1]))

def func7 (x):
	lst = []
	b = {}
	for i in x.split():
		b[i] = b.get(i,0)+1

	c = sorted(b.items(),key=lambda x: (x[1],x[0]),reverse=True)
	k = 0
	for i in range(len(c)):
		if k <= 2:
			lst.append(c[i][0])
			k += 1
	return lst

if __name__ == '__main__':
	print(func1(23456,5))
	print(func2(56))
	print(func3([1234,2345,5678,8907],15))
	print(func4(232233257895))
	print(func5([1,4,7,3,2,10]))
	print(func6("input(2,3,hello(world,world)and(9,8),(6,4),(-3,4),(4,-3)"))
	print(func7("hello hello apple hi ji ki"))

