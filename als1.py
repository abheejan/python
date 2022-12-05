Python 3.10.8 (tags/v3.10.8:aaaf517, Oct 11 2022, 16:50:30) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
help(x.split)
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    help(x.split)
NameError: name 'x' is not defined
x="we are stdying python"
help(x.split)
Help on built-in function split:

split(sep=None, maxsplit=-1) method of builtins.str instance
    Return a list of the substrings in the string, using sep as the separator string.
    
      sep
        The separator used to split the string.
    
        When set to None (the default value), will split on any whitespace
        character (including \\n \\r \\t \\f and spaces) and will discard
        empty strings from the result.
      maxsplit
        Maximum number of splits (starting from the left).
        -1 (the default value) means no limit.
    
    Note, str.split() is mainly useful for data that has been intentionally
    delimited.  With natural text that includes punctuation, consider using
    the regular expression module.

#x
    
x
'we are stdying python'
#name
name="Abheejan"
name.split()
['Abheejan']
a="this is ncitand it is located in balkumari""
SyntaxError: incomplete input
a="this is nci tand it is located in balkumari""
SyntaxError: incomplete input
a="this is nci tand it is located in balkumari"
a.split()
['this', 'is', 'nci', 'tand', 'it', 'is', 'located', 'in', 'balkumari']
name="This is ncit \n college"
print(name)
This is ncit 
 college
location="This college is in \n Balkumari"
print(location)
This college is in 
 Balkumari
location="This \n college \n is\n in \n Balkumari"
print(location)
This 
 college 
 is
 in 
 Balkumari
location=" This \n college \n is\n in \n Balkumari"
print(location)
 This 
 college 
 is
 in 
 Balkumari
location="This college\tis in \n Balkumari"
print(location)
This college	is in 
 Balkumari
name.count(space)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    name.count(space)
NameError: name 'space' is not defined. Did you mean: 'slice'?
location.count(space)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    location.count(space)
NameError: name 'space' is not defined. Did you mean: 'slice'?
location.count("")
31
location="This college\tis in \n Balkumari"
location.count(" ")
4
location.count("\t")
1
a="this\is"
print(a)
this\is
a="this\Sis"
print(a)
this\Sis
b="
KeyboardInterrupt
b="good evening good eveninggood eveninggood eveninggood eveninggood eveninggood eveninggood eveninggood eveninggood eveninggood eveninggood eveninggood eveninggood eveninggood eveninggood eveninggood evening"
print(b)
good evening good eveninggood eveninggood eveninggood eveninggood eveninggood eveninggood eveninggood eveninggood eveninggood eveninggood eveninggood eveninggood eveninggood eveninggood eveninggood evening
letters=""" hi hello bye hi hello bye hi """
print(letters)
 hi hello bye hi hello bye hi 
b="good evening good eveninggood eveninggood eveninggood eveninggood eveninggood eveninggood eveninggood eveninggood eveninggood eveninggood eveninggood eveninggood eveninggood eveninggood eveninggood evening"
b="good evening good eveninggood eveninggood eveninggood eveninggood eveninggood eveninggood eveninggood eveninggood eveninggood eveninggood eveninggood eveninggood eveninggood eveninggood eveninggood evening
SyntaxError: incomplete input

SyntaxError: incomplete input
SyntaxError: incomplete input
name=(b="good evening good eveninggood eveninggood eveninggood eveninggood eveninggood eveninggood eveninggood eveninggood eveninggood eveninggood eveninggood eveninggood eveninggood eveninggood eveninggood evening"
      
SyntaxError: '(' was never closed
name="""good evening good eveninggood eveninggood eveninggood
eveninggood eveninggood eveninggood eveninggood eveninggood
eveninggood eveninggood eveninggood eveninggood eveninggood eveninggood eveninggood evening"""
      
print(name)
      
good evening good eveninggood eveninggood eveninggood
eveninggood eveninggood eveninggood eveninggood eveninggood
eveninggood eveninggood eveninggood eveninggood eveninggood eveninggood eveninggood evening
age=20
      
if age <=20:
      print("age is < or = 20")

      
age is < or = 20

if age <30:
      print("okay")

      
okay
else:
    
SyntaxError: invalid syntax
if age <=20:
    print("age is < or = 20")
else:
    print("age is greater than 20")

    
age is < or = 20
age=21
if age <=20:
    print("age is < or = 20")
else:
    print("age is greater than 20")

    
age is greater than 20
a=5
if a==6
SyntaxError: incomplete input
if a==6:
    print("true")
else:
    print("false")

    
false
age=5
if a==6:
    print("true")
else:
    print("false")

    
false
age=6
if a==6:
    print("true")
else:
    print("false")

    
false
age=10
if a==10:
    print("true")
else:
    print("false")

    
false
if a==10:
    print("yes")
else:
    print("no")

    
no
a=10
if a==10:
    print("yes")
else:
    print("no")

    
yes
a="11"
if a==10:
    print("yes")
else:
    print("no")

    
no
a==7
False
a==10
False
a=10
a==10
True
a==10|| a<=10
SyntaxError: invalid syntax
a==10| a<=10
True
a==10 or a<=10
True
a==10 & a<=10
True
a==10 and a<=10
True
a=2
a==10 and a<=10
False
a==10 & a<=10
True
if a==10 and a<=10
SyntaxError: incomplete input
if a==10 and a<=10:
    print("okay")

    
if a==10 and a<=10:
    print("okay")
else print("not okay")
SyntaxError: expected ':'
if a==10 and a<=10:
    print("okay")
else
SyntaxError: incomplete input
if a==10 and a<=10:
    print("okay")
else:
    print("not okay")

    
not okay
a=10


if a==10 and a<=10:
    print("okay")
else:
    print("not okay")

    
okay
if a==10 and a<=10:
    print("okay")
else
SyntaxError: incomplete input
if a==10 and a<=10:
    print("okay")
elif(a==12 or a>10):
    print(more than or equal to 12)
    
SyntaxError: invalid syntax. Perhaps you forgot a comma?
if a==10 and a<=10:
    print("okay")
elif(a==12 or a>10):
    print("more than or equal to 12")
elif(a=20 or a<30):
    
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
if a==10 and a<=10:
    print("okay")
elif(a==12 or a>10):
    print("more than or equal to 12")
elif(a==20 or a<30):
    print("more than or equal to 20")
elif(a==30 or a<40):
    print("more than or equal to 30")

    
okay
a=33
if a==10 and a<=10:
    print("okay")
elif(a==12 or a>10):
    print("more than or equal to 12")
elif(a==20 or a<30):
    print("more than or equal to 20")
elif(a==30 or a<40):
    print("more than or equal to 30")

    
more than or equal to 12
name="python"
't' in name
True
y in name
Traceback (most recent call last):
  File "<pyshell#140>", line 1, in <module>
    y in name
NameError: name 'y' is not defined
'y' in name
True
's' in name
False
for x in name
SyntaxError: incomplete input
for x in name:
    print("true")

    
true
true
true
true
true
true
for a in name:
    print(a)

    
p
y
t
h
o
n
for x in range(1):
    print(x)

    
0
for x in range(10):
    print(x)

    
0
1
2
3
4
5
6
7
8
9
for x in range(15):
    print(x)

    
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
for i in ramge(5,100):
    if i>25:
        print(i+"25")
    if (i==50):
        print("fifty")
    if (i>80)
    
SyntaxError: incomplete input
for i in ramge(5,100):
    if i>25:
        print(i+"25")
    if (i==50):
        print("fifty")
    if (i>=80)
    
SyntaxError: incomplete input
for i in ramge(5,100):
    if i>25:
        print(i+"25")
    if (i==50):
        print("fifty")
    if (i>=80):
        print("more than eighty")

        
Traceback (most recent call last):
  File "<pyshell#166>", line 1, in <module>
    for i in ramge(5,100):
NameError: name 'ramge' is not defined. Did you mean: 'name'?
for i in ramge(5,100):
    if i>25:
        print(i+25)
    if (i==50):
        print("fifty")
    if (i>=80):
        print("more than eighty")

        
Traceback (most recent call last):
  File "<pyshell#168>", line 1, in <module>
    for i in ramge(5,100):
NameError: name 'ramge' is not defined. Did you mean: 'name'?
for i in range(5,100):
    if i>25:
        print(i+25)
    if (i==50):
        print("fifty")
    if (i>=80):
        print("more than eighty")

        
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
fifty
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
101
102
103
104
105
more than eighty
106
more than eighty
107
more than eighty
108
more than eighty
109
more than eighty
110
more than eighty
111
more than eighty
112
more than eighty
113
more than eighty
114
more than eighty
115
more than eighty
116
more than eighty
117
more than eighty
118
more than eighty
119
more than eighty
120
more than eighty
121
more than eighty
122
more than eighty
123
more than eighty
124
more than eighty
for i in range(5,100):
    if i>25:
        print(i+str(25))
    if (i==50):
        print("fifty")
    if (i>=80):
        print("more than eighty")

        
Traceback (most recent call last):
  File "<pyshell#172>", line 3, in <module>
    print(i+str(25))
TypeError: unsupported operand type(s) for +: 'int' and 'str'
for i in range(5,100):
    if i>25:
        print(i+int(25))
    if (i==50):
        print("fifty")
    if (i>=80):
        print("more than eighty")

        
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
fifty
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
101
102
103
104
105
more than eighty
106
more than eighty
107
more than eighty
108
more than eighty
109
more than eighty
110
more than eighty
111
more than eighty
112
more than eighty
113
more than eighty
114
more than eighty
115
more than eighty
116
more than eighty
117
more than eighty
118
more than eighty
119
more than eighty
120
more than eighty
121
more than eighty
122
more than eighty
123
more than eighty
124
more than eighty
for i in range(5,100):
    if i>25:
        print(i+int(25))
    if (i==50):
        print("fifty")
   if(if (i>=80)):
        print("more than eighty")
        
SyntaxError: unindent does not match any outer indentation level
for i in range(5,100):
    if i>25:
        print(i+int(25))
    if (i==50):
        print("fifty")
   if (i>=80):
       if (i<=90):
        print(i)
        
SyntaxError: unindent does not match any outer indentation level
for i in range(5,100):
    if i>25:
        print(i+int(25))
    if (i==50):
        print("fifty")
   if (i>=80):
       if (i<=90):
           
SyntaxError: unindent does not match any outer indentation level
for i in range(5,100):
    if i>25:
        print(i+int(25))
    if (i==50):
        print("fifty")
   if (i>=80):
       if (i<=90):
           
SyntaxError: unindent does not match any outer indentation level
pfor i in range(5,100):
    if i>25:
        print(i+25)
    if (i==50):
        print("fifty")
   if (i>=80):
       if (i<=90):
           
SyntaxError: invalid syntax
for i in range(5,100):
    if i>25:
        print(i+25)
    if (i==50):
        print("fifty")
   if (i>=80):
       if (i<=90):
           
SyntaxError: unindent does not match any outer indentation level
for i in range(5,100):
    if i>25:
        print(i+25)
    if (i==50):
        print("fifty")
   if (i>=80):
       if (i<=90):
           
SyntaxError: unindent does not match any outer indentation level
for i in range(5,100):
    if i>25:
        print(i+25)
    if (i==50):
        print("fifty")
   if (i>=80):
       if (i<=90):
           
SyntaxError: unindent does not match any outer indentation level
for i in range(5,100):
    if i>25:
        print(i+25)
    if (i==50):
        print("fifty")
   if (i>=80):
       
SyntaxError: unindent does not match any outer indentation level
for i in range(5,100):
    if i>25:
        print(i+int(25))
    if (i==50):
        print("fifty")
    if (i>=80):
        if (i<=90):
            print(i)

            
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
fifty
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
101
102
103
104
105
80
106
81
107
82
108
83
109
84
110
85
111
86
112
87
113
88
114
89
115
90
116
117
118
119
120
121
122
123
124
for i in range(5,100):
    if i>25:
        print(str(i)+int(25))
    if (i==50):
        print("fifty")
    if (i>=80):
        if (i<=90):
            print(i)

            
Traceback (most recent call last):
  File "<pyshell#188>", line 3, in <module>
    print(str(i)+int(25))
TypeError: can only concatenate str (not "int") to str
for i in range(5,100):
    if i>25:
        print(str(i)+25)
    if (i==50):
        print("fifty")
    if (i>=80):
        if (i<=90):
            print(i)

            
Traceback (most recent call last):
  File "<pyshell#190>", line 3, in <module>
    print(str(i)+25)
TypeError: can only concatenate str (not "int") to str
for i in range(5,100):
    if i>25:
        print(i+25)
    if (i==50):
        print("fifty")
    if (i>=80):
        if (i<=90):
            print(i)

            
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
fifty
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
101
102
103
104
105
80
106
81
107
82
108
83
109
84
110
85
111
86
112
87
113
88
114
89
115
90
116
117
118
119
120
121
122
123
124
for i in range(10):
    if(i%2==0):
        print("**")
        print(i)
        # for x in range(i):
        #print("++",x)
else
SyntaxError: incomplete input
for i in range(10):
    if(i%2==0):
        print("**")
        print(i)
        # for x in range(i):
        #print("++",x)
else:
    print("fail")

    
**
0
**
2
**
4
**
6
**
8
fail
for i in range(10):
    if(i%2==0):
        print("**")
        print(i)
        # for x in range(i):
        #print("++",x)
else:
    print("fail",i)

    
**
0
**
2
**
4
**
6
**
8
fail 9
for i in range(10):
    if(i%2==0):
        print("**",i)
        # for x in range(i):
        #print("++",x)
else:
    print("fail",i)

    
** 0
** 2
** 4
** 6
** 8
fail 9
for i in range(10):
    if(i%2==0):
        print("**",i)
else:
    print("fail",i)

    
** 0
** 2
** 4
** 6
** 8
fail 9
for i in range(10):
    if(i%2==0):
        print("**",i)
    else:
        print("fail",i)

        
** 0
fail 1
** 2
fail 3
** 4
fail 5
** 6
fail 7
** 8
fail 9
for num in range(1,100):
    if (i%2==0):
        print("number is even")
    else:
        print("number is odd")

        
number is odd
number is odd
number is odd
number is odd
number is odd
number is odd
number is odd
number is odd
number is odd
number is odd
number is odd
number is odd
number is odd
number is odd
number is odd
number is odd
number is odd
number is odd
number is odd
number is odd
number is odd
number is odd
number is odd
number is odd
number is odd
number is odd
number is odd
number is odd
number is odd
number is odd
number is odd
number is odd
number is odd
number is odd
number is odd
number is odd
number is odd
number is odd
number is odd
number is odd
number is odd
number is odd
number is odd
number is odd
number is odd
number is odd
number is odd
number is odd
number is odd
number is odd
number is odd
number is odd
number is odd
number is odd
number is odd
number is odd
number is odd
number is odd
number is odd
number is odd
number is odd
number is odd
number is odd
number is odd
number is odd
number is odd
number is odd
number is odd
number is odd
number is odd
number is odd
number is odd
number is odd
number is odd
number is odd
number is odd
number is odd
number is odd
number is odd
number is odd
number is odd
number is odd
number is odd
number is odd
number is odd
number is odd
number is odd
number is odd
number is odd
number is odd
number is odd
number is odd
number is odd
number is odd
number is odd
number is odd
number is odd
number is odd
number is odd
for i in range(1,100):
    if (i%2==0):
        print("number is even")
    else:
        print("number is odd")

        
number is odd
number is even
number is odd
number is even
number is odd
number is even
number is odd
number is even
number is odd
number is even
number is odd
number is even
number is odd
number is even
number is odd
number is even
number is odd
number is even
number is odd
number is even
number is odd
number is even
number is odd
number is even
number is odd
number is even
number is odd
number is even
number is odd
number is even
number is odd
number is even
number is odd
number is even
number is odd
number is even
number is odd
number is even
number is odd
number is even
number is odd
number is even
number is odd
number is even
number is odd
number is even
number is odd
number is even
number is odd
number is even
number is odd
number is even
number is odd
number is even
number is odd
number is even
number is odd
number is even
number is odd
number is even
number is odd
number is even
number is odd
number is even
number is odd
number is even
number is odd
number is even
number is odd
number is even
number is odd
number is even
number is odd
number is even
number is odd
number is even
number is odd
number is even
number is odd
number is even
number is odd
number is even
number is odd
number is even
number is odd
number is even
number is odd
number is even
number is odd
number is even
number is odd
number is even
number is odd
number is even
number is odd
number is even
number is odd
number is even
number is odd
for i in range(1,100):
    if (i%2==0):
        print("number is even",i)
    else:
        print("number is odd",i)

        
number is odd 1
number is even 2
number is odd 3
number is even 4
number is odd 5
number is even 6
number is odd 7
number is even 8
number is odd 9
number is even 10
number is odd 11
number is even 12
number is odd 13
number is even 14
number is odd 15
number is even 16
number is odd 17
number is even 18
number is odd 19
number is even 20
number is odd 21
number is even 22
number is odd 23
number is even 24
number is odd 25
number is even 26
number is odd 27
number is even 28
number is odd 29
number is even 30
number is odd 31
number is even 32
number is odd 33
number is even 34
number is odd 35
number is even 36
number is odd 37
number is even 38
number is odd 39
number is even 40
number is odd 41
number is even 42
number is odd 43
number is even 44
number is odd 45
number is even 46
number is odd 47
number is even 48
number is odd 49
number is even 50
number is odd 51
number is even 52
number is odd 53
number is even 54
number is odd 55
number is even 56
number is odd 57
number is even 58
number is odd 59
number is even 60
number is odd 61
number is even 62
number is odd 63
number is even 64
number is odd 65
number is even 66
number is odd 67
number is even 68
number is odd 69
number is even 70
number is odd 71
number is even 72
number is odd 73
number is even 74
number is odd 75
number is even 76
number is odd 77
number is even 78
number is odd 79
number is even 80
number is odd 81
number is even 82
number is odd 83
number is even 84
number is odd 85
number is even 86
number is odd 87
number is even 88
number is odd 89
number is even 90
number is odd 91
number is even 92
number is odd 93
number is even 94
number is odd 95
number is even 96
number is odd 97
number is even 98
number is odd 99
for i in range(1,100):
    if (i%2==0):
        print(i,"number is even")
    else:
        print(i,"number is odd")

        
1 number is odd
2 number is even
3 number is odd
4 number is even
5 number is odd
6 number is even
7 number is odd
8 number is even
9 number is odd
10 number is even
11 number is odd
12 number is even
13 number is odd
14 number is even
15 number is odd
16 number is even
17 number is odd
18 number is even
19 number is odd
20 number is even
21 number is odd
22 number is even
23 number is odd
24 number is even
25 number is odd
26 number is even
27 number is odd
28 number is even
29 number is odd
30 number is even
31 number is odd
32 number is even
33 number is odd
34 number is even
35 number is odd
36 number is even
37 number is odd
38 number is even
39 number is odd
40 number is even
41 number is odd
42 number is even
43 number is odd
44 number is even
45 number is odd
46 number is even
47 number is odd
48 number is even
49 number is odd
50 number is even
51 number is odd
52 number is even
53 number is odd
54 number is even
55 number is odd
56 number is even
57 number is odd
58 number is even
59 number is odd
60 number is even
61 number is odd
62 number is even
63 number is odd
64 number is even
65 number is odd
66 number is even
67 number is odd
68 number is even
69 number is odd
70 number is even
71 number is odd
72 number is even
73 number is odd
74 number is even
75 number is odd
76 number is even
77 number is odd
78 number is even
79 number is odd
80 number is even
81 number is odd
82 number is even
83 number is odd
84 number is even
85 number is odd
86 number is even
87 number is odd
88 number is even
89 number is odd
90 number is even
91 number is odd
92 number is even
93 number is odd
94 number is even
95 number is odd
96 number is even
97 number is odd
98 number is even
99 number is odd
for i not in range(1,100):
    if (i%2==0):
        print(i,"number is even")
    else:
        print(i,"number is odd")
        
SyntaxError: invalid syntax
for i in range(1,100):
    if (num%2!=0):
        print(i,"number is even")
    else:
        print(i,"number is odd")

        
1 number is even
2 number is even
3 number is even
4 number is even
5 number is even
6 number is even
7 number is even
8 number is even
9 number is even
10 number is even
11 number is even
12 number is even
13 number is even
14 number is even
15 number is even
16 number is even
17 number is even
18 number is even
19 number is even
20 number is even
21 number is even
22 number is even
23 number is even
24 number is even
25 number is even
26 number is even
27 number is even
28 number is even
29 number is even
30 number is even
31 number is even
32 number is even
33 number is even
34 number is even
35 number is even
36 number is even
37 number is even
38 number is even
39 number is even
40 number is even
41 number is even
42 number is even
43 number is even
44 number is even
45 number is even
46 number is even
47 number is even
48 number is even
49 number is even
50 number is even
51 number is even
52 number is even
53 number is even
54 number is even
55 number is even
56 number is even
57 number is even
58 number is even
59 number is even
60 number is even
61 number is even
62 number is even
63 number is even
64 number is even
65 number is even
66 number is even
67 number is even
68 number is even
69 number is even
70 number is even
71 number is even
72 number is even
73 number is even
74 number is even
75 number is even
76 number is even
77 number is even
78 number is even
79 number is even
80 number is even
81 number is even
82 number is even
83 number is even
84 number is even
85 number is even
86 number is even
87 number is even
88 number is even
89 number is even
90 number is even
91 number is even
92 number is even
93 number is even
94 number is even
95 number is even
96 number is even
97 number is even
98 number is even
99 number is even
for i in range(1,100):
    if (1%2==0):
        print(i,"number is even")
    else:
        print(i,"number is odd")

        
1 number is odd
2 number is odd
3 number is odd
4 number is odd
5 number is odd
6 number is odd
7 number is odd
8 number is odd
9 number is odd
10 number is odd
11 number is odd
12 number is odd
13 number is odd
14 number is odd
15 number is odd
16 number is odd
17 number is odd
18 number is odd
19 number is odd
20 number is odd
21 number is odd
22 number is odd
23 number is odd
24 number is odd
25 number is odd
26 number is odd
27 number is odd
28 number is odd
29 number is odd
30 number is odd
31 number is odd
32 number is odd
33 number is odd
34 number is odd
35 number is odd
36 number is odd
37 number is odd
38 number is odd
39 number is odd
40 number is odd
41 number is odd
42 number is odd
43 number is odd
44 number is odd
45 number is odd
46 number is odd
47 number is odd
48 number is odd
49 number is odd
50 number is odd
51 number is odd
52 number is odd
53 number is odd
54 number is odd
55 number is odd
56 number is odd
57 number is odd
58 number is odd
59 number is odd
60 number is odd
61 number is odd
62 number is odd
63 number is odd
64 number is odd
65 number is odd
66 number is odd
67 number is odd
68 number is odd
69 number is odd
70 number is odd
71 number is odd
72 number is odd
73 number is odd
74 number is odd
75 number is odd
76 number is odd
77 number is odd
78 number is odd
79 number is odd
80 number is odd
81 number is odd
82 number is odd
83 number is odd
84 number is odd
85 number is odd
86 number is odd
87 number is odd
88 number is odd
89 number is odd
90 number is odd
91 number is odd
92 number is odd
93 number is odd
94 number is odd
95 number is odd
96 number is odd
97 number is odd
98 number is odd
99 number is odd
for i in range(1,100):
    if (i%2==0):
        print(i,"number is even")
    else:
        print(i,"number is odd")

        
1 number is odd
2 number is even
3 number is odd
4 number is even
5 number is odd
6 number is even
7 number is odd
8 number is even
9 number is odd
10 number is even
11 number is odd
12 number is even
13 number is odd
14 number is even
15 number is odd
16 number is even
17 number is odd
18 number is even
19 number is odd
20 number is even
21 number is odd
22 number is even
23 number is odd
24 number is even
25 number is odd
26 number is even
27 number is odd
28 number is even
29 number is odd
30 number is even
31 number is odd
32 number is even
33 number is odd
34 number is even
35 number is odd
36 number is even
37 number is odd
38 number is even
39 number is odd
40 number is even
41 number is odd
42 number is even
43 number is odd
44 number is even
45 number is odd
46 number is even
47 number is odd
48 number is even
49 number is odd
50 number is even
51 number is odd
52 number is even
53 number is odd
54 number is even
55 number is odd
56 number is even
57 number is odd
58 number is even
59 number is odd
60 number is even
61 number is odd
62 number is even
63 number is odd
64 number is even
65 number is odd
66 number is even
67 number is odd
68 number is even
69 number is odd
70 number is even
71 number is odd
72 number is even
73 number is odd
74 number is even
75 number is odd
76 number is even
77 number is odd
78 number is even
79 number is odd
80 number is even
81 number is odd
82 number is even
83 number is odd
84 number is even
85 number is odd
86 number is even
87 number is odd
88 number is even
89 number is odd
90 number is even
91 number is odd
92 number is even
93 number is odd
94 number is even
95 number is odd
96 number is even
97 number is odd
98 number is even
99 number is odd
list(range(o,100,5))
Traceback (most recent call last):
  File "<pyshell#233>", line 1, in <module>
    list(range(o,100,5))
NameError: name 'o' is not defined
list(range(0,100,5))
[0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
list(range(0,100,1))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
list(range(0,100,2))
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]
list(range(0,100,3))
[0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99]
list(range(1,100,1))
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
list(range(1,100,2))
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]
list(range(1,100,10))
[1, 11, 21, 31, 41, 51, 61, 71, 81, 91]
list(range(1,100,19))
[1, 20, 39, 58, 77, 96]
list(range(1,100,9))
[1, 10, 19, 28, 37, 46, 55, 64, 73, 82, 91]
list(range(0,100,9))
[0, 9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99]
list(range(0,100,10))
[0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
list(range(10,100,10))
[10, 20, 30, 40, 50, 60, 70, 80, 90]
list(range(10,101,10))
[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
nums=[1,1,5,8,9,10,2,3]
dir(nums)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
print(name)
python
print(nums)
[1, 1, 5, 8, 9, 10, 2, 3]
help(nums)
Help on list object:

class list(object)
 |  list(iterable=(), /)
 |  
 |  Built-in mutable sequence.
 |  
 |  If no argument is given, the constructor creates a new empty list.
 |  The argument must be an iterable if specified.
 |  
 |  Built-in subclasses:
 |      MyList
 |  
 |  Methods defined here:
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
 |  
 |  __delitem__(self, key, /)
 |      Delete self[key].
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(...)
 |      x.__getitem__(y) <==> x[y]
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __iadd__(self, value, /)
 |      Implement self+=value.
 |  
 |  __imul__(self, value, /)
 |      Implement self*=value.
 |  
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __mul__(self, value, /)
 |      Return self*value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __reversed__(self, /)
 |      Return a reverse iterator over the list.
 |  
 |  __rmul__(self, value, /)
 |      Return value*self.
 |  
 |  __setitem__(self, key, value, /)
 |      Set self[key] to value.
 |  
 |  __sizeof__(self, /)
 |      Return the size of the list in memory, in bytes.
 |  
 |  append(self, object, /)
 |      Append object to the end of the list.
 |  
 |  clear(self, /)
 |      Remove all items from list.
 |  
 |  copy(self, /)
 |      Return a shallow copy of the list.
 |  
 |  count(self, value, /)
 |      Return number of occurrences of value.
 |  
 |  extend(self, iterable, /)
 |      Extend list by appending elements from the iterable.
 |  
 |  index(self, value, start=0, stop=9223372036854775807, /)
 |      Return first index of value.
 |      
 |      Raises ValueError if the value is not present.
 |  
 |  insert(self, index, object, /)
 |      Insert object before index.
 |  
 |  pop(self, index=-1, /)
 |      Remove and return item at index (default last).
 |      
 |      Raises IndexError if list is empty or index is out of range.
 |  
 |  remove(self, value, /)
 |      Remove first occurrence of value.
 |      
 |      Raises ValueError if the value is not present.
 |  
 |  reverse(self, /)
 |      Reverse *IN PLACE*.
 |  
 |  sort(self, /, *, key=None, reverse=False)
 |      Sort the list in ascending order and return None.
 |      
 |      The sort is in-place (i.e. the list itself is modified) and stable (i.e. the
 |      order of two equal elements is maintained).
 |      
 |      If a key function is given, apply it once to each list item and sort them,
 |      ascending or descending, according to their function values.
 |      
 |      The reverse flag can be set to sort in descending order.
 |  
 |  ----------------------------------------------------------------------
 |  Class methods defined here:
 |  
 |  __class_getitem__(...) from builtins.type
 |      See PEP 585
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __hash__ = None

>>> type(nums)
<class 'list'>
