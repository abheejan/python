Python 3.10.8 (tags/v3.10.8:aaaf517, Oct 11 2022, 16:50:30) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
4+6
10
5/5
1.0
55/5
11.0
63*5
315
Binav Sigdel
SyntaxError: incomplete input
2/0
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    2/0
ZeroDivisionError: division by zero
10/55
0.18181818181818182
0/1
0.0
0/0
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    0/0
ZeroDivisionError: division by zero
2/a
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    2/a
NameError: name 'a' is not defined
2+a
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    2+a
NameError: name 'a' is not defined
a+a
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    a+a
NameError: name 'a' is not defined
name=Binav Sigdel
SyntaxError: incomplete input
name=Binav,
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    name=Binav,
NameError: name 'Binav' is not defined
name="binav"
a="hello"
10$2
SyntaxError: invalid syntax
10%2
0
10%3
1
10\3
SyntaxError: unexpected character after line continuation character
a,f
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    a,f
NameError: name 'f' is not defined
a,"f"
('hello', 'f')
,"b"
SyntaxError: invalid syntax
"c,
SyntaxError: incomplete input
"c","g"
('c', 'g')
c
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    c
NameError: name 'c' is not defined
10@2
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    10@2
TypeError: unsupported operand type(s) for @: 'int' and 'int'
4%2
0
5*5
25
5*a
'hellohellohellohellohello'
a*5
'hellohellohellohellohello'
5*b
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    5*b
NameError: name 'b' is not defined
5*"a"
'aaaaa'
5*"a"*5
'aaaaaaaaaaaaaaaaaaaaaaaaa'
a="2"
5*2
10
5*a
'22222'
5+a
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    5+a
TypeError: unsupported operand type(s) for +: 'int' and 'str'
"a"*2
'aa'
x="a"
x
'a'
print x\
      
SyntaxError: unexpected character after line continuation character
print x;
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
print (x)
a
print(a)
2
x=3.11
print(x)
3.11
a="x"
\
print(a)
x
print(x)
3.11
a=x
print(a)
3.11
y="f"
first="Binav"
last="Sigdel"
age=19
first,last,age
('Binav', 'Sigdel', 19)
first last age
SyntaxError: invalid syntax
print(first,last,age)
Binav Sigdel 19
print(first,last,:age)
SyntaxError: invalid syntax
print(first last age)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print(first,last,_age)
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    print(first,last,_age)
NameError: name '_age' is not defined. Did you mean: 'age'?
print(first,last,age)
Binav Sigdel 19
print"My name is"(first,last)
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
"my name is"print(first,last)
SyntaxError: invalid syntax
print("My name is",first,last,"and my age is",age)
My name is Binav Sigdel and my age is 19
print"My name is",(first,last)
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
print(first+age)
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    print(first+age)
TypeError: can only concatenate str (not "int") to str
>>> print(first+age)
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    print(first+age)
TypeError: can only concatenate str (not "int") to str
>>> print(first+last)
BinavSigdel
>>> print(last+first)
SigdelBinav
>>> type(age)
<class 'int'>
>>> type(first)
<class 'str'>
>>> type(last)
<class 'str'>
\
>>> newage=str(age)
>>> type(newage)
<class 'str'>
>>> print(first+last+newage)
BinavSigdel19
>>> print(age)
19
>>> print(newage)
19
>>> type(newage)
<class 'str'>
>>> newage
'19'
>>> aGE
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    aGE
NameError: name 'aGE' is not defined. Did you mean: 'age'?
>>> age
19
