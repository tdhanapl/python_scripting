#####################python#############
####special characters#######
Write special charcters only inside of quotes-->'', ""
\n --> new line 
\b -->back space
\t -->tab
\  -->escape sysmbol
\a -->alert sound

###################variable#############
A variable is nothing but a reserved mermory location to store values.
##declare variable
x=10
print(x)
Note:-
	Do not write quotes around the variable name.

##define mutliple variable in single line
x=3;y=5.6;z=5
## All variable at time 
print(x,y,z)	
##Delete a variable
del x
##rule to define a variable name 
1.It contains letters, numbers and underscore.
2.It should not a keyword or pre-define variable.
3.Can not  contains spaces
4.It should not start  with a numbers
5.Case-sensitive

########################variable data types####################
Every value in python has data type
Since everthing is an object in python programming.
Data types are actually classes and variable are instance(object) of the classes.

##Basic Data type are:
1.Numeric(int, float and complex)
2.Strings
3.Boolean

1.Numeric(int, float and complex)
#input
x=5 --->integer
y=7 --->float
z=3+y -->complex
v="value or content"-->string
print(x, type(x))
print(y, type(y))
print(z, type(z))
print(v, type(v))
#output
5 <class 'int'>
7 <class 'int'>
10 <class 'int'>
2.strings type
my_name="dhanapal"
java_verssion="1.8"
print(my_name, type(my_name))
print(java_verssion)
#output
dhanapal <class 'str'>
1.8 <class 'str'>

3.Boolean
##input
my_value=True
my_new_value=False
print(my_value, type(my_value))
print(my_new_value,type(my_new_value))
##output
True <class 'bool'>
False <class 'bool'>
Note:-
1. In Boolean except for True and False remaining all string we have write quotetation.
2. Any data type can be converted into boolean
3. bool(empty)= False -->bool(0),bool(None),bool([]),bool(()),bool({})
4. bool(non-empty)=True -->bool(100)
5. Any data type can be converted into a string but reverse is not always true

##typecasting or type Conversion
#input
x=56
print(x, type(x))
y=str(x)
print(y, type(y))
z=bool(x)
print(z, type(z))
p=0
print(p, type(p))
q=bool(p)
print(q, type(q))
#output
56 <class 'int'>
56 <class 'str'>
True <class 'bool'>
0 <class 'int'>
False <class 'bool'>

####################Pirnt with variable(s) and strings(s)########
##input 
#x=3;y=5.7;lang_name="python scripting"
x=3
y=5.7
lang_name="python scripting"
print(x,y,lang_name)
print(f"{x},{y},{lang_name}")
print(f"the value of x is={x}\nthe value of y is={y}")
##output
3 5.7 python scripting
3,5.7,python scripting
the value of x is=3
the value of y is=5.7

############input and output statement#################
##input
#simple addition cal
a=(input("Enter a value: "))
b=input("Enter b value: ")
result=a+b
print(f"the addition of {a} and {b} is= {result}")
##output
Enter a value: 10
Enter b value: 34
the addition of 10 and 34 is= 1034
Note:-
1.In this input given as  number but in output comes as string not as integer
2.if you want input  number as integer need use eval[Ex:- a=eval(input("Enter a value: "))]

##using eval in input method
a=eval((input("Enter a value: ")))
b=eval(input("Enter b value: "))
result=a+b
print(f"the addition of {a} and {b} is= {result}")
##output
Enter a value: 4
Enter b value: 9
the addition of 4 and 9 is= 13
## using integer in input menthod (it is for only integer)
##input
a=int((input("Enter a value: ")))
b=int(input("Enter b value: "))
result=a+b
print(f"the addition of {a} and {b} is= {result}")
##output
Enter a value: 5
Enter b value: 6
the addition of 5 and 6 is= 11

##################Strings in python################
1. Formating
##input
my_name="Narendra"
my_job="linux admin"
job_role="""
I started my carrier as an linux admin and 
now learning devops team
""" 
print(f'my name is: {my_name}\nmy_job name is :{my_job}\njob_role is :{job_role}')
##output
my name is: Narendra
my_job name is :linux admin
job_role is :
I started my carrier as an admin and 
now learning devops team

2.##input
my_str=""
my_new_str=" "
print(f'{bool(my_str)}')
print(f'{bool(my_new_str)}')
##output
False
True
Note:-
    Here empty space also a one string that why in bool value its true

3. ##slice and  index get particular words in string)
###Index 
my_name=dhanapal
print(my_name)
print(my_name[0])
print(my_name[1])
print(my_name[-1])  # -1 last character in the given  string
print(my_name[0:])  # : from starting starting to end all character in the given string
print(my_name[0:5]) #  0:5 from 0 to 5  character calling in the given  string
print(my_name[0:5])
##output
dhanapal
d
h
l
dhanapal
dhana
##Slice
 declaring the string
str ="Geeks for Geeks !"
 # slicing using indexing sequence
print(str[: 3])
print(str[1 : 5 : 2])
print(str[-1 : -12 : -2])
##output
Output
Gee
ek
!seGrf
Note:-    
1.String are immutable and it cannot changed once it has been assigned.
2.We can simply reassgin different strings to the same 

4.##Find length of string
##input
my_name="dhanapal"
print(f'Length of string is: {len(my_name)}')
print(my_name[-8: 4])
## output
Length of string is: 8

5. Adding/concatenate two variable (string)
##input
my_first_name="t"
my_last_name="dhanapal"
full_name=my_first_name+my_last_name
#full_name=my_first_name+" "my_last_name
full_name_1=my_first_name+" "+my_last_name
full_name_2=my_first_name+" "+my_last_name+" is from tirupati"
print(full_name)
print(full_name_1)
print(full_name_2)
##output
tdhanapal
t dhanapal
t dhanapal is from tirupati

################Case Conversion operation on strings##################
##input
my_string="Python Scripting"
my_string_lower=my_string.lower()
print(my_string_lower)
print(my_string.lower())
print(my_string.upper())
print(my_string.swapcase())
print(my_string.title())
print(my_string.capitalize())
print(my_string.casefold())
#print(dir(my_string))

##output
python scripting
python scripting
PYTHON SCRIPTING
pYTHON sCRIPTING
Python Scripting
Python scripting
python scripting

#####################Boolean operation on strings################
##input
my_string="Python Scripting"
my_string_lower=my_string.lower()
print(my_string_lower)
print(my_string.startswith('P'))
print(my_string.startswith('Pyt'))
print(my_string.endswith('ing'))
print(my_string.istitle())
print(my_string.islower())
print(my_string.isupper())
print(my_string.isspace())
#print(dir(my_string))
##output
ython scripting
True
True
True
True
False
False
False

###############join, center and zfill string operation#######
1. join string
##input
x="python"
y="-".join(x)
print(y)
print(x)
print("*".join(x))
print("\n".join(x))
##output
p-y-t-h-o-n
python
p*y*t*h*o*n
p
y
t
h
o
n
2. center string
##input
x="python"
y="python scritping"
z="learn python scripting"
print(x.center(20))
print(f"{x.center(20)}\n{y.center(20)}\n{z.center(20)}")
##output
python       
       python       
  python scritping  
learn python scripting
3. Zfill string
##input
x="python"
y="python scritping"
print(x.zfill(10))
print(y.zfill(20))
##output
0000python
0000python scritping

#################Strip and split operation on strings##############
1. striping on strings
##input
x="python is easy"
y="python scritping"
print(x.strip())
print(y.strip('p')) # It will delete p" in start or ending
print(y.strip('g')) # It will delete "g" in start or ending
print(x.strip('easy')) # It will delete "easy" in start or ending
##output
ython is easy
ython scritping
python scritpin
python is  

2. spliting on strings
##input 
x="python scripting is easy"
##split
print(x.split()) ##here space is variable that will sperate words 
print(x.split('is')) ##here is the  variable that will sperate words
##output
['python', 'scripting', 'is', 'easy']
['python scripting ', ' easy'] 

##########count, index and find operations on strings################
##input
x="python scripting is easy and  is popular language "
##split
print(x.count('p'))
print(x.index('is')
print(x.find('p'))
print(x.find('p', 2))
print(x.find(-z))
##output
4
17
0
-1
-1
##############Data structure of python################
https://tanaya.hashnode.dev/introduction-to-python-day-13-task

Data structure are used to store a collection of data.
There are four buil-in data structures. they are 
1. List--->[]
2. Tuple--->()
3. Dictionary--->{} with kay value pair
4. set--->{}

1. list data type
##input
x=5
my_value=[3,4,5,'python','devops',5.6]
print(len(my_value),type(my_value))
print(my_value[0])
print(my_value[4])
print(my_value[-1])
print(my_value[3][1])
print(my_value[:])
print(my_value[0:])
print(my_value[1:4])
my_value[0]=30 ## modify the value of 3 as 30
print(my_value)

my_list=[3,5,2,7,3,8,5,9]
print(my_list.index(5))
print(my_list.index(5,2))
print(my_list.count(5))
#print(my_list.index(10))
print(my_list)
my_list.append(30) ##append  value add in only last index
print(my_list)
my_list.insert(1,45) ##insert we can add value wherever you want like in 1st index
print(my_list)
my_list.remove(9) ##modify operation doesn't required print
print(my_list)
print(my_list.pop()) ##pop will delete by default last index value or number
print(my_list.pop(4)) 
print(my_list)
my_list.reverse() ##reverse the values in list
print(my_list) 
my_list.clear() ##modify operation doesn't required print
print(my_list)

##output
6 <class 'list'>
3
devops
5.6
y
[3, 4, 5, 'python', 'devops', 5.6]
[3, 4, 5, 'python', 'devops', 5.6]
[4, 5, 'python']
[30, 4, 5, 'python', 'devops', 5.6]
1
6
2
[3, 5, 2, 7, 3, 8, 5, 9]
[3, 5, 2, 7, 3, 8, 5, 9, 30]
[3, 45, 5, 2, 7, 3, 8, 5, 9, 30]
[3, 45, 5, 2, 7, 3, 8, 5, 30]
30
7
[3, 45, 5, 2, 3, 8, 5]
[5, 8, 3, 2, 5, 45, 3]
[]

2.tuple data type
##input
#Tuple and strings are immutable
my_empty=()
my_tuple=(3,4,[5,6,7],8,9,10)
print(my_tuple)
print(bool(my_tuple))
print(bool(my_empty))
print(my_tuple[2:]) #from 2nd index to last index
print(my_tuple[:2]) ##up to 2nd index 
print(my_tuple[2][1],type(my_tuple))
len(my_tuple)
##output
(3, 4, [5, 6, 7], 8, 9, 10)
True
False
([5, 6, 7], 8, 9, 10)
(3, 4)
6 <class 'tuple'>

3. dictionary data structure 
##input
#Dictionary is also called as  map in terraform
#Dictionary type is key value represnation
my_dict={'name':'dhanapal', 'age':24, 'job':'software',  'plcae':'banglore'} 
print(my_dict['name'], type(my_dict))
print(my_dict.get('age'))
print(my_dict)
#my_dict.clear()
my_dict['age']=25 #adding or replacing the age value
my_dict['designation']='Linux' #adding the value
print(my_dict)
print(my_dict.keys()) ##here it will list keys only
print(my_dict.values())
print(my_dict.items())
y=my_dict.copy() ##copiny my_dict to y variable
print(id(y), id(my_dict))
print(y)
my_new_dict={'company':"Zee"}
my_dict.update(my_new_dict) ##updating the new variable into older variable of my_new_dict
print(my_dict)
my_dict.pop('company') ##pop will delete company key value
my_dict.popitem() ##pop will delete default last item
print(my_dict)
keys=['a','e','i','o','u'] 
new_dict=dict.fromkeys(keys) ##conert the list into dictonary
print(new_dict)
new_dict['a']="first alpha"
print(new_dict)
##output
dhanapal <class 'dict'>
24
{'name': 'dhanapal', 'age': 24, 'job': 'software', 'plcae': 'banglore'}
{'name': 'dhanapal', 'age': 25, 'job': 'software', 'plcae': 'banglore', 'designation': 'Linux'}
dict_keys(['name', 'age', 'job', 'plcae', 'designation'])
dict_values(['dhanapal', 25, 'software', 'banglore', 'Linux'])
dict_items([('name', 'dhanapal'), ('age', 25), ('job', 'software'), ('plcae', 'banglore'), ('designation', 'Linux')])
140347630034176 140347630034048
{'name': 'dhanapal', 'age': 25, 'job': 'software', 'plcae': 'banglore', 'designation': 'Linux'}
{'name': 'dhanapal', 'age': 25, 'job': 'software', 'plcae': 'banglore', 'designation': 'Linux', 'company': 'Zee'}
{'name': 'dhanapal', 'age': 25, 'job': 'software', 'plcae': 'banglore'}
{'a': None, 'e': None, 'i': None, 'o': None, 'u': None}
{'a': 'first alpha', 'e': None, 'i': None, 'o': None, 'u': None}

4. set data type
A set is an unordered collection of items. 
Every set element is unique (no duplicates) and must be immutable (cannot be changed).
##input
my_set = {1, 2, 3, 4, 3, 2}
print(my_set)
# we can make set from a list
my_set = set([1, 2, 3, 2])
print(my_set)
# set cannot have mutable items
# initialize my_set
my_set = {1, 3}
print(my_set)
# add an element
my_set.add(2)
print(my_set)
# add multiple elements
my_set.update([2, 3, 4])
print(my_set)
# add list and set
my_set.update([4, 5], {1, 6, 8})
print(my_set)

##output
{1, 2, 3, 4}
{1, 2, 3}
{1, 3}
{1, 2, 3}
{1, 2, 3, 4}
{1, 2, 3, 4, 5, 6, 8}

############Swap Two Variables###########
Given two variables x and y, write a Python program to swap(exchange) their values.
##Method-1(Using Naive approach)
# swapping of two variables
x = 10
y = 50
 # Swapping of two variables
# Using third variable
temp = x
x = y
y = temp
print("Value of x:", x)
print("Value of y:", y)
##output
Value of x: 50
Value of y: 10

##Method-2(Using comma operator)
##input
# swapping of two variables
x = 10
y = 50
# Swapping of two variables
# without using third variable
x, y = y, x
print("Value of x:", x)
print("Value of y:", y)
##output
Value of x: 50
Value of y: 10

##Method 3(Using XOR)
The bitwise XOR operator can be used to swap two variables. 
The XOR of two numbers x and y returns a number which has all the bits as 1 wherever bits of x and y differ. For example XOR of 10 (In Binary 1010) and 5 (In Binary 0101) is 1111 and XOR of 7 (0111) and 5 (0101) is (0010).
##Input
# Swapping of two variables
x = 10
y = 50
 # Swapping using xor
x = x ^ y
y = x ^ y
x = x ^ y
print("Value of x:", x)
print("Value of y:", y)
##Output
Value of x: 50
Value of y: 10

