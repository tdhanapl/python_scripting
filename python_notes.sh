#####################python#############
####special characters#######
Write special charcters only inside of quotes-->'', ""
\n --> new line 
\b -->back space
\t -->tab
\  -->escape sysmbol
\a -->alert sound

##############variable#############
A variable is nothing but a reserved but a reserved mermory location to store values.
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
########variable data types########
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

#########Pirnt with variable(s) and strings(s)########

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
I started my carrier as an admin and 
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
#################

