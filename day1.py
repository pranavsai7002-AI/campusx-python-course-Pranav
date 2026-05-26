# #  # sep - seperator parameter which gives space between each word or character in output
# comment in python is used to explain the code and it is ignored by the interpreter
# we can use # for single line comment and ''' ''' or """ """ for multi line comment for python no mutli line comment but we can use multi line string as multi line comment
# #  # example
# # print("India",5,"Nepal")
# # # in output we got India 5 Nepal see the space is given my paqrameter sep
# # # we can change sep for example 
# # print("India",5,"Nepal",sep='/')
# # #India/5/Nepal
# # print("India",5,"Nepal",sep='-')
# # #India-5-Nepal
# print("hello")
# print("world")
# hello
# world
# # now here we printed each at different line but if we want to print both in same line then we can use end parameter
# print("hello",end=' ')
# print("hi") see here we got hello hi both in same line using that paramenter end ('\n'is deafult parameter for end )
# hello hi
#python supports 3 categories of datatypes 
#1. basic types - int, float, bool, str, complex
#2. collection types - list, tuple, set, dict
#3. user defined types - class
# 1) integers
# print(4)
# print(1e309) # inf
# print(-1e309) # -inf
# print(1e308) 
# 2) float
# print(3.14)
# print(1.7e309) # inf
# print(-1.7e309) # -inf
# print(1.7e308)
# 3) bool
# print(True)
# print(False)
# 4) string
# print("hello world")
# 5) complex
# print(2+3j) here 2 is real part and 3 is imaginary part of complex number
# 6) list
# # mylist = [1,2,3,4,5]
# # print(mylist)
# we use square brackets [] to define list and we can store any type of data in list
# mylist = [1,2.5,"hello",True]
# print(mylist)
# 7) tuple
# mytuple = (1,2.5,"hello",True)  we use parenthesis () to define tuple and we can store any type of data in tuple
# print(mytuple) 
# 8) set
# myset = {1,2.5,"hello",True} we use curly braces {} to define set and we can store any type of data in set but set is unordered and unindexed collection of data
# print(myset) 
# 9) dict
# mydict = {"name":"John","age":30,"city":"New York"} we use curly braces {} to define dict and we can store data in key value pair in dict
# print(mydict)   
# variables in python are used to store data and we can use any name for variable but it should not start with number and it should not be a keyword in python
# # we can assign value to variable using = operator
# name = "John"
# age = 30
# print(name)
# print(age)
# name = nitish # here we reassigning value to variable name
# print(name) but here we got error because we forgot to put quotes around nitish as it is a string value so we should put quotes around it
# name = "nitish" 
# print(name) 
# in python no variable declaration is required we can directly assign value to variable and it will automatically create variable for us this called dynamic typing in python and we can also change the type of variable by assigning different type of value to it
# dynamic binding means that the type of variable is determined at runtime and we can change the type of variable by assigning different type of value to it
# age = "thirty" # here we changed the type of variable age from int to str
# print(age)  
# we use special syntax in python for multiple variables in a line 
# name;age;city = "John";30;"New York" here we assigned value to multiple variables in a line
# Keywords 
# python is case sensitive language so we should be careful while using variable names and keywords in python keywords are reserved words in python that have special meaning and we cannot use them as variable names or function names in python for example if we try to use keyword as variable name we will get error
# for example
# if = 10 # here we got error because if is a keyword in python and we cannot use it as variable name
# print(if)
#in programming we use keywords to perform certain operations and we cannot use them as variable names or function names in python for example if we try to use keyword as variable name we will get error
# python has 35 keywords and they are as follows
# import keyword
# print(keyword.kwlist) 
# output : ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']  
# identifiers in python are used to name variables, functions, classes, modules and other objects in python and they should follow certain rules. 
# for example they should start with a letter or underscore and they can contain letters, digits and underscores but they cannot start with a digit and they cannot be a keyword in python. 
# for example if we try to use keyword as variable name we will get error.
# rules for identifiers in python are as follows:
# 1. An identifier can only contain letters, digits and underscores.
# 2. An identifier cannot start with a digit.
# 3. An identifier cannot be a keyword in python.
# 4. An identifier cannot contain spaces.
# 5. An identifier cannot contain special characters like @, #, $, %, etc.
# 6. An identifier cannot be the same as a built-in function in python.
# example of valid identifiers in python are as follows:
# name = "John"
# age = 30
# city = "New York"
# _name = "John"
# name1 = "John"
# example of invalid identifiers in python are as follows:
# 1name = "John" # here we got error because identifier cannot start with a digit
# name@ = "John" # here we got error because identifier cannot contain special characters
# Their are 2 types of softwares 
# static software and dynamic software
# static software is the software that is installed on a computer and it runs on that computer only for example operating system, office suite, etc.
# dynamic software is the software that is accessed through the internet and it runs on a remote server for example google docs, facebook, etc.
# dynamic software - user gives input and it gives output based on that input for example google search, facebook, etc.
# input() - here what we write inside input() will be shown as a prompt to the user and it will wait for the user to enter some input and then it will return that input as a string.
name = input("Enter your name: ") # here we are asking user to enter their name 
print("Hello",name) # here we are printing the name entered by user
age = input("Enter your age: ") # here we are asking user to enter their age
print("Your age is",age) # here we are printing the age entered by user


    





