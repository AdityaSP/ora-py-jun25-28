Python 2.7.12 (v2.7.12:d33e0cf91556, Jun 27 2016, 15:24:40) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> print "Hello World!"
Hello World!
>>> print 'Hello World!'
Hello World!
>>> print '''
hello
again
'''

hello
again

>>> print """
hello
again
"""

hello
again

>>> 
>>> 
>>> 
>>> a = 10
>>> b = 11.2
>>> c = True
>>> d = 'Hello'
>>> 
>>> 
>>> 
>>> #Strongly typed programming language
>>> type(a)
<type 'int'>
>>> print type(a)
<type 'int'>
>>> a
10
>>> a,b,c,d
(10, 11.2, True, 'Hello')
>>> type(a), type(b), type(c), type(d)
(<type 'int'>, <type 'float'>, <type 'bool'>, <type 'str'>)
>>> #int a = 10
>>> a = 10
>>> type(a)
<type 'int'>
>>> a = d
>>> type(a)
<type 'str'>
>>> 
>>> 
>>> 
>>> a = 10
>>> a + 20
30
>>> a = 3
>>> b = 4
>>> a / b
0
>>> a * 1.0/b
0.75
>>> c = a * 1.0/b
>>> c
0.75
>>> type(c)
<type 'float'>
>>> if a/b > 0 :
	print 'Do something'

	
>>> a
3
>>> type(a)
<type 'int'>
>>> float(a)
3.0
>>> a, type(a)
(3, <type 'int'>)
>>> c = float(a)
>>> c, type(c)
(3.0, <type 'float'>)
>>> float(a)/b
0.75
>>> a/float(b)
0.75
>>> 
>>> 
>>> 
>>> 
>>> a = 'Hello'
>>> type(a)
<type 'str'>
>>> b = 'Again'
>>> a + b
'HelloAgain'
>>> a + " " + b
'Hello Again'
>>> c = 3
>>> a + c

Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    a + c
TypeError: cannot concatenate 'str' and 'int' objects
>>> '5' + 5

Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    '5' + 5
TypeError: cannot concatenate 'str' and 'int' objects
>>> int('5') + 5
10
>>> '5' + str(5)
'55'
>>> bool(1)
True
>>> bool(0)
False
>>> 'hello' * 5
'hellohellohellohellohello'
>>> "----------------------------------"
'----------------------------------'
>>> print "-" * 30
------------------------------
>>> 'a'
'a'
>>> type('a')
<type 'str'>
>>> 
>>> 
>>> 
>>> a
'Hello'
>>> a = 'hello world'
>>> a[0]
'h'
>>> a[5]
' '
>>> len(a)
11
>>> a[len(a) - 1]
'd'
>>> a[10]
'd'
>>> a[11]

Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    a[11]
IndexError: string index out of range
>>> a[-1]
'd'
>>> a[-2]
'l'
>>> a[-len(a)]
'h'
>>> a[-11]
'h'
>>> a[-12]

Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    a[-12]
IndexError: string index out of range
>>> a
'hello world'
>>> a[0:5]
'hello'
>>> a[6:9]
'wor'
>>> a[6:100]
'world'
>>> 
>>> 
>>> a
'hello world'
>>> a ='0123456789'
>>> a[0:8]
'01234567'
>>> a[-10:-2]
'01234567'
>>> a[0:-2]
'01234567'
>>> a[8:0]
''
>>> a[8:0:-1]
'87654321'
>>> 
>>> 
>>> a[-1:-10:-1]
'987654321'
>>> a[-1:-11:-1]
'9876543210'
>>> a[5:100]
'56789'
>>> a[5:]
'56789'
>>> a[0:5]
'01234'
>>> a[:5]
'01234'
>>> a[:]
'0123456789'
>>> a[::1]
'0123456789'
>>> a[::-1]
'9876543210'
>>> #8:45PM IST
>>> 
>>> 
>>> len(a)
10
>>> type(a)
<type 'str'>
>>> 
>>> 
>>> 
>>> a
'0123456789'
>>> a = 'hello world'
>>> a.upper()
'HELLO WORLD'
>>> a
'hello world'
>>> b
'Again'
>>> b = 3
>>> b.upper()

Traceback (most recent call last):
  File "<pyshell#127>", line 1, in <module>
    b.upper()
AttributeError: 'int' object has no attribute 'upper'
>>> a.lower()
'hello world'
>>> a.capitalize()
'Hello world'
>>> a.title()
'Hello World'
>>> a = 'the discovery of india'
>>> a.split()
['the', 'discovery', 'of', 'india']
>>> a = '1::2::3::4'
>>> a.split('::')
['1', '2', '3', '4']
>>> li= a.split('::')
>>> type(li)
<type 'list'>
>>> list.__doc__
"list() -> new empty list\nlist(iterable) -> new list initialized from iterable's items"
>>> print list.__doc__
list() -> new empty list
list(iterable) -> new list initialized from iterable's items
>>> help(list)
Help on class list in module __builtin__:

class list(object)
 |  list() -> new empty list
 |  list(iterable) -> new list initialized from iterable's items
 |  
 |  Methods defined here:
 |  
 |  __add__(...)
 |      x.__add__(y) <==> x+y
 |  
 |  __contains__(...)
 |      x.__contains__(y) <==> y in x
 |  
 |  __delitem__(...)
 |      x.__delitem__(y) <==> del x[y]
 |  
 |  __delslice__(...)
 |      x.__delslice__(i, j) <==> del x[i:j]
 |      
 |      Use of negative indices is not supported.
 |  
 |  __eq__(...)
 |      x.__eq__(y) <==> x==y
 |  
 |  __ge__(...)
 |      x.__ge__(y) <==> x>=y
 |  
 |  __getattribute__(...)
 |      x.__getattribute__('name') <==> x.name
 |  
 |  __getitem__(...)
 |      x.__getitem__(y) <==> x[y]
 |  
 |  __getslice__(...)
 |      x.__getslice__(i, j) <==> x[i:j]
 |      
 |      Use of negative indices is not supported.
 |  
 |  __gt__(...)
 |      x.__gt__(y) <==> x>y
 |  
 |  __iadd__(...)
 |      x.__iadd__(y) <==> x+=y
 |  
 |  __imul__(...)
 |      x.__imul__(y) <==> x*=y
 |  
 |  __init__(...)
 |      x.__init__(...) initializes x; see help(type(x)) for signature
 |  
 |  __iter__(...)
 |      x.__iter__() <==> iter(x)
 |  
 |  __le__(...)
 |      x.__le__(y) <==> x<=y
 |  
 |  __len__(...)
 |      x.__len__() <==> len(x)
 |  
 |  __lt__(...)
 |      x.__lt__(y) <==> x<y
 |  
 |  __mul__(...)
 |      x.__mul__(n) <==> x*n
 |  
 |  __ne__(...)
 |      x.__ne__(y) <==> x!=y
 |  
 |  __repr__(...)
 |      x.__repr__() <==> repr(x)
 |  
 |  __reversed__(...)
 |      L.__reversed__() -- return a reverse iterator over the list
 |  
 |  __rmul__(...)
 |      x.__rmul__(n) <==> n*x
 |  
 |  __setitem__(...)
 |      x.__setitem__(i, y) <==> x[i]=y
 |  
 |  __setslice__(...)
 |      x.__setslice__(i, j, y) <==> x[i:j]=y
 |      
 |      Use  of negative indices is not supported.
 |  
 |  __sizeof__(...)
 |      L.__sizeof__() -- size of L in memory, in bytes
 |  
 |  append(...)
 |      L.append(object) -- append object to end
 |  
 |  count(...)
 |      L.count(value) -> integer -- return number of occurrences of value
 |  
 |  extend(...)
 |      L.extend(iterable) -- extend list by appending elements from the iterable
 |  
 |  index(...)
 |      L.index(value, [start, [stop]]) -> integer -- return first index of value.
 |      Raises ValueError if the value is not present.
 |  
 |  insert(...)
 |      L.insert(index, object) -- insert object before index
 |  
 |  pop(...)
 |      L.pop([index]) -> item -- remove and return item at index (default last).
 |      Raises IndexError if list is empty or index is out of range.
 |  
 |  remove(...)
 |      L.remove(value) -- remove first occurrence of value.
 |      Raises ValueError if the value is not present.
 |  
 |  reverse(...)
 |      L.reverse() -- reverse *IN PLACE*
 |  
 |  sort(...)
 |      L.sort(cmp=None, key=None, reverse=False) -- stable sort *IN PLACE*;
 |      cmp(x, y) -> -1, 0, 1
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __hash__ = None
 |  
 |  __new__ = <built-in method __new__ of type object>
 |      T.__new__(S, ...) -> a new object with type S, a subtype of T

>>> li= a.split('::')
>>> type(li)
<type 'list'>
>>> 
>>> 
>>> 
>>> 
>>> 
>>> li = []
>>> li = ['Brazil','Burma','SL']
>>> li
['Brazil', 'Burma', 'SL']
>>> len(li)
3
>>> li[0]
'Brazil'
>>> li[4]

Traceback (most recent call last):
  File "<pyshell#152>", line 1, in <module>
    li[4]
IndexError: list index out of range
>>> li[2:]
['SL']
>>> li[::-1]
['SL', 'Burma', 'Brazil']
>>> a
'1::2::3::4'
>>> a[1]=','

Traceback (most recent call last):
  File "<pyshell#156>", line 1, in <module>
    a[1]=','
TypeError: 'str' object does not support item assignment
>>> a = '1::2::3::4'
>>> a = '1234'
>>> a
'1234'
>>> a = 'hello world
SyntaxError: EOL while scanning string literal
>>> a = 'hello world'
>>> a.upper()
'HELLO WORLD'
>>> a
'hello world'
>>> id(a)
50548480L
>>> a = a.upper()
>>> id(a)
44614832L
>>> a
'HELLO WORLD'
>>> 
>>> 
>>> li
['Brazil', 'Burma', 'SL']
>>> id(li)
50322632L
>>> li[1] = 'UK'
>>> li
['Brazil', 'UK', 'SL']
>>> id(li)
50322632L
>>> li
['Brazil', 'UK', 'SL']
>>> li.append('USA')
>>> li
['Brazil', 'UK', 'SL', 'USA']
>>> b = ['Kenya','Canada','India']
>>> li
['Brazil', 'UK', 'SL', 'USA']
>>> b
['Kenya', 'Canada', 'India']
>>> li.extend(b)
>>> li
['Brazil', 'UK', 'SL', 'USA', 'Kenya', 'Canada', 'India']
>>> li[2]='China'
>>> li
['Brazil', 'UK', 'China', 'USA', 'Kenya', 'Canada', 'India']
>>> li.insert(4,'Germany')
>>> li
['Brazil', 'UK', 'China', 'USA', 'Germany', 'Kenya', 'Canada', 'India']
>>> li
['Brazil', 'UK', 'China', 'USA', 'Germany', 'Kenya', 'Canada', 'India']
>>> li.remove('Kenya')
>>> li
['Brazil', 'UK', 'China', 'USA', 'Germany', 'Canada', 'India']
>>> li.pop()
'India'
>>> li
['Brazil', 'UK', 'China', 'USA', 'Germany', 'Canada']
>>> c= li.pop()
>>> c
'Canada'
>>> li.pop(1)
'UK'
>>> li
['Brazil', 'China', 'USA', 'Germany']
>>> b
['Kenya', 'Canada', 'India']
>>> del b
>>> b

Traceback (most recent call last):
  File "<pyshell#198>", line 1, in <module>
    b
NameError: name 'b' is not defined
>>> del li[3]
>>> li
['Brazil', 'China', 'USA']
>>> 
>>> a = True
>>> if a:
	print "Truthful"

	
Truthful
>>> a = 10
>>> if a < 10:
	print "Single digit"

	
>>> if a < 10:
	print "Single digit"
else:
	print "Double digit"

	
Double digit
>>> if a < 10 :
	print "Single digit"
elif a < 100:
	print "Double digit"
else:
	print "2 + digits"

	
Double digit
>>> a = 100
>>> if a < 10 :
	print "Single digit"
elif a < 100:
	print "Double digit"
else:
	print "2 + digits"

	
2 + digits
>>> a < 10
False
>>> x = 3
>>> y = 8
>>> x < y
True
>>> x < y and y < 10
True
>>> x < y or y < 10
True
>>> x < y
True
>>> not x < y
False
>>> li
['Brazil', 'China', 'USA']
>>> 'USA' in li
True
>>> a
100
>>> s

Traceback (most recent call last):
  File "<pyshell#237>", line 1, in <module>
    s
NameError: name 's' is not defined
>>> s = 'Hello World'
>>> 'Hello' in s
True
>>> x
3
>>> y
8
>>> x > 2 and x < 10
True
>>> 2 < x < 10
True
>>> 2 < x < y < 20
True
>>> 2 < x and x < y and y<20
True
>>> li
['Brazil', 'China', 'USA']
>>> for country in li:
	print country

	
Brazil
China
USA
>>> count = 0
>>> while count < len(li):
	print li[count]
	count += 1

	
Brazil
China
USA
>>> import random
>>> random.randint(1,5)
2
>>> random.randint(1,5)
3
>>> random.randint(1,5)
5
>>> random.randint(1,5)
4
>>> random.randint(1,5)
5
>>> random.randint(1,5)
1
>>> x = random.randint(1,5)
>>> type(x)
<type 'int'>
>>> 
>>> a = 'the discovery of india'
>>> a.split()
['the', 'discovery', 'of', 'india']
>>> li = a.split()
>>> li
['the', 'discovery', 'of', 'india']
>>> delim = ","
>>> delim.join(li)
'the,discovery,of,india'
>>> "::".join(li)
'the::discovery::of::india'
>>> li = [45,67,89]
>>> '-->'.join(li)

Traceback (most recent call last):
  File "<pyshell#273>", line 1, in <module>
    '-->'.join(li)
TypeError: sequence item 0: expected string, int found
>>> s = '10.30.23.78'
>>> li = s.split('.')
>>> li
['10', '30', '23', '78']
>>> len(li)
4
>>> int(li[-1])
78
>>> int(li[-1]) + 1
79
>>> str(int(li[-1]) + 1)
'79'
>>> li[-1] = str(int(li[-1]) + 1)
>>> li
['10', '30', '23', '79']
>>> ".".join(li)
'10.30.23.79'
>>> 
>>> 
>>> 
>>> li
['10', '30', '23', '79']
>>> li = ['the', 'discovery', 'of', 'india']
>>> li
['the', 'discovery', 'of', 'india']
>>> t = ('batman', 'superman', 'spiderman')
>>> type(t)
<type 'tuple'>
>>> t[0] = 'ironman'

Traceback (most recent call last):
  File "<pyshell#292>", line 1, in <module>
    t[0] = 'ironman'
TypeError: 'tuple' object does not support item assignment
>>> t = 'batman', 'superman', 'spiderman'
>>> type(t)
<type 'tuple'>
>>> t
('batman', 'superman', 'spiderman')
>>> a,b,c = t
>>> print a , b , c
batman superman spiderman
>>> 
>>> 
>>> 
>>> a
'batman'
>>> b
'superman'
>>> a, b = b, a
>>> a
'superman'
>>> b
'batman'
>>> 
>>> 
>>> 
>>> 
>>> t
('batman', 'superman', 'spiderman')
>>> t[0]
'batman'
>>> t[1:]
('superman', 'spiderman')
>>> len(t)
3
>>> l[5]

Traceback (most recent call last):
  File "<pyshell#314>", line 1, in <module>
    l[5]
NameError: name 'l' is not defined
>>> t[6]

Traceback (most recent call last):
  File "<pyshell#315>", line 1, in <module>
    t[6]
IndexError: tuple index out of range
>>> d = { 'name': 'Aditya', 'email':'sp.aditya@gmail.com'}
>>> d[0]

Traceback (most recent call last):
  File "<pyshell#317>", line 1, in <module>
    d[0]
KeyError: 0
>>> d['name']
'Aditya'
>>> d['email']
'sp.aditya@gmail.com'
>>> d['city']

Traceback (most recent call last):
  File "<pyshell#320>", line 1, in <module>
    d['city']
KeyError: 'city'
>>> d
{'name': 'Aditya', 'email': 'sp.aditya@gmail.com'}
>>> d['city'] = 'Bangalore'
>>> d
{'city': 'Bangalore', 'name': 'Aditya', 'email': 'sp.aditya@gmail.com'}
>>> d['city'] ='New York'
>>> d
{'city': 'New York', 'name': 'Aditya', 'email': 'sp.aditya@gmail.com'}
>>> d.keys()
['city', 'name', 'email']
>>> d.values()
['New York', 'Aditya', 'sp.aditya@gmail.com']
>>> d.items()
[('city', 'New York'), ('name', 'Aditya'), ('email', 'sp.aditya@gmail.com')]
>>> 
>>> 
>>> d
{'city': 'New York', 'name': 'Aditya', 'email': 'sp.aditya@gmail.com'}
>>> d['phone'] = ['345356753', '345345567']
>>> d
{'city': 'New York', 'name': 'Aditya', 'phone': ['345356753', '345345567'], 'email': 'sp.aditya@gmail.com'}
>>> d['phone'][0]
'345356753'
>>> d['address'] = {'home': 'asdfqwerfd asdfa', 'work' : 'esdfsd asdf a'}
>>> d
{'city': 'New York', 'address': {'home': 'asdfqwerfd asdfa', 'work': 'esdfsd asdf a'}, 'name': 'Aditya', 'phone': ['345356753', '345345567'], 'email': 'sp.aditya@gmail.com'}
>>> d['address']['home']
'asdfqwerfd asdfa'
>>> 
>>> 
>>> 
>>> 
>>> def sayhi():
	print "Hi"

	
>>> sayhi()
Hi
>>> sayhi()
Hi
>>> def sayhi():
	return 'Hi'

>>> x = sayhi()
>>> x
'Hi'
>>> x = len(s)
>>> x
11
>>> x = sayhi()
>>> 
>>> 
>>> 
>>> 
>>> 
>>> len.__doc__
'len(object) -> integer\n\nReturn the number of items of a sequence or collection.'
>>> def sayhi():
	'This function says a cheerful Hi'
	return 'Hi'

>>> x= sayhi()
>>> x
'Hi'
>>> sayhi.__doc__
'This function says a cheerful Hi'
>>> random.__doc__
'Random variable generators.\n\n    integers\n    --------\n           uniform within range\n\n    sequences\n    ---------\n           pick random element\n           pick random sample\n           generate random permutation\n\n    distributions on the real line:\n    ------------------------------\n           uniform\n           triangular\n           normal (Gaussian)\n           lognormal\n           negative exponential\n           gamma\n           beta\n           pareto\n           Weibull\n\n    distributions on the circle (angles 0 to 2pi)\n    ---------------------------------------------\n           circular uniform\n           von Mises\n\nGeneral notes on the underlying Mersenne Twister core generator:\n\n* The period is 2**19937-1.\n* It is one of the most extensively tested generators in existence.\n* Without a direct way to compute N steps forward, the semantics of\n  jumpahead(n) are weakened to simply jump to another distant state and rely\n  on the large period to avoid overlapping sequences.\n* The random() method is implemented in C, executes in a single Python step,\n  and is, therefore, threadsafe.\n\n'
>>> print random.__doc__
Random variable generators.

    integers
    --------
           uniform within range

    sequences
    ---------
           pick random element
           pick random sample
           generate random permutation

    distributions on the real line:
    ------------------------------
           uniform
           triangular
           normal (Gaussian)
           lognormal
           negative exponential
           gamma
           beta
           pareto
           Weibull

    distributions on the circle (angles 0 to 2pi)
    ---------------------------------------------
           circular uniform
           von Mises

General notes on the underlying Mersenne Twister core generator:

* The period is 2**19937-1.
* It is one of the most extensively tested generators in existence.
* Without a direct way to compute N steps forward, the semantics of
  jumpahead(n) are weakened to simply jump to another distant state and rely
  on the large period to avoid overlapping sequences.
* The random() method is implemented in C, executes in a single Python step,
  and is, therefore, threadsafe.


>>> 
>>> 
>>> def full_name(fn, ln):
	return fn + " " + ln

>>> full_name('Aditya', 'SP')
'Aditya SP'
>>> full_name(fn = 'Aditya', ln = 'SP')
'Aditya SP'
>>> full_name(ln = 'SP', fn = 'Aditya')
'Aditya SP'
>>> def full_name(fn, ln, title):
	return title+ "." + fn + " " + ln

>>> full_name(ln = 'SP', fn = 'Aditya', title = 'Mr')
'Mr.Aditya SP'
>>> def full_name(fn, ln, title = 'Mr'):
	return title+ "." + fn + " " + ln

>>> full_name('Aditya', 'SP')
'Mr.Aditya SP'
>>> full_name('Aditya', 'SP', 'Dr')
'Dr.Aditya SP'
>>> full_name(fn = 'Aditya', ln ='SP', title ='Dr')
'Dr.Aditya SP'
>>> 
>>> 
>>> l

Traceback (most recent call last):
  File "<pyshell#386>", line 1, in <module>
    l
NameError: name 'l' is not defined
>>> li
['the', 'discovery', 'of', 'india']
>>> sorted(li)
['discovery', 'india', 'of', 'the']
>>> sorted(li, reverse = True)
['the', 'of', 'india', 'discovery']
>>> n = [1,3,45,23,56,343,89,2]
>>> sorted(n)
[1, 2, 3, 23, 45, 56, 89, 343]
>>> sorted(n, reverse= True)
[343, 89, 56, 45, 23, 3, 2, 1]
>>> 
>>> 
>>> 
>>> 
>>> def add(x,y):
	return x + y

>>> c = add(3,4)
>>> c
7
>>> if c == 7:
	print "Test success"
else:
	print "Test failed"

	
Test success
>>> 
>>> 
>>> 
>>> 
>>> 
>>> def sayhi():
	return "Hi"

>>> a = 10
>>> type(a)
<type 'int'>
>>> type(sayhi)
<type 'function'>
>>> 
>>> 
>>> b = a
>>> type(b)
<type 'int'>
>>> greet = sayhi
>>> type(greet)
<type 'function'>
>>> greet()
'Hi'
>>> sayhi()
'Hi'
>>> 
>>> def execother(f):
	print type(f)

	
>>> execother(a)
<type 'int'>
>>> execother(sayhi)
<type 'function'>
>>> def execother(f):
	f()

	
>>> execother(f)

Traceback (most recent call last):
  File "<pyshell#434>", line 1, in <module>
    execother(f)
NameError: name 'f' is not defined
>>> execother(sayhi)
>>> def execother(f):
	print f()

	
>>> execother(sayhi)
Hi
>>> 
>>> 
>>> 
>>> kms = [5,10,21,42]
>>> def kmtomi(x):
	return x * 0.62

>>> mi = []
>>> for km in kms:
	miles = kmtomi(km)
	mi.append(miles)

	
>>> mi
[3.1, 6.2, 13.02, 26.04]
>>> mi = map(kmtomi, kms)
>>> mi
[3.1, 6.2, 13.02, 26.04]
>>> ages = [12,34,56,78,89,90]
>>> age_inrange = []
>>> for age in ages:
	if 30 < age < 80:
		age_inrange.append(age)

		
>>> age_inrange
[34, 56, 78]
>>> def inrange(x):
	return 30 < age < 80

>>> 30 < 40 < 80
True
>>> age_inrange = filter(inrange, ages)
>>> age_inrange
[]
>>> ages
[12, 34, 56, 78, 89, 90]
>>> def inrange(x):
	return 30 < x < 80

>>> age_inrange = filter(inrange, ages)
>>> age_inrange
[34, 56, 78]
>>> 
>>> 
>>> 
>>> range(5)
[0, 1, 2, 3, 4]
>>> #li = [ <expr> <for statement>  ]
>>> li = [
	for i in range(50)]
SyntaxError: invalid syntax
>>> li = [ i * i for i in range(50)]
>>> li
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900, 961, 1024, 1089, 1156, 1225, 1296, 1369, 1444, 1521, 1600, 1681, 1764, 1849, 1936, 2025, 2116, 2209, 2304, 2401]
>>> #li = [ <expr> <for statement> <if statement> ]
>>> li = [ i * i for i in range(50) if i % 2 == 0]
>>> li
[0, 4, 16, 36, 64, 100, 144, 196, 256, 324, 400, 484, 576, 676, 784, 900, 1024, 1156, 1296, 1444, 1600, 1764, 1936, 2116, 2304]
>>> 
>>> 
>>> 
>>> 10
10
>>> 'Hello'
'Hello'
>>> #literals - integer literal and string literal
>>> def kmtomi(x):
	return x * 0.62

>>> lambda x : x * 0.62
<function <lambda> at 0x000000000312FCF8>
>>> y = lambda x : x * 0.62
>>> type(y)
<type 'function'>
>>> y(5)
3.1
>>> def add(x,y):
	return x + y

>>> m = 3
>>> n = 4
>>> add(m,n)
7
>>> add(3,4)
7
>>> kms
[5, 10, 21, 42]
>>> map(lambda x : x * 0.62 , kms)
[3.1, 6.2, 13.02, 26.04]
>>> y = lambda x, y: x + y
>>> y(4,5)
9
>>> add = lambda x, y: x + y
>>> add(4,5)
9
>>> s = 'chrome.exe                    5664 Console                    1    280,220 K\r'
>>> s.split()
['chrome.exe', '5664', 'Console', '1', '280,220', 'K']
>>> s.split()[1]
'5664'
>>> 
>>> 
>>> ages
[12, 34, 56, 78, 89, 90]
>>> age_in = [ age for age in ages if 30 < age < 80]
>>> age_in
[34, 56, 78]
>>> final_ans = [ age * 12 for age in age_in]
>>> final_ans
[408, 672, 936]
>>> 
>>> 
>>> [age * 12 for age in ages if 30 < age < 80]
[408, 672, 936]
>>> 
>>> 
>>> 
>>> import requests
>>> requests.__file__
'D:\\sw\\Python27\\lib\\site-packages\\requests\\__init__.pyc'
>>> 
>>> 
