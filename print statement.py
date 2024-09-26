#-> # is used to comment the line 
#-> it is also used to define the code meaning 
#-> it can also comment and uncomment multiple lines using ctrl +/

#comment example
#write a program to print ypur name 
printf("my name is sahil thakur")#print function to display statment

#variables can store the value and it can change at any time 
name="sahil"
#pass the variable in the print function 
print("my name is "+ name )# + is used to concatenate the string 

#declear and initialize the multiple variable 
age=33
gender =" male "
#pass the multiple variable in the print function
# this line give the type error
#reason for error str can't be concatenate with integer 
#problem 
#print (" my age is "+name +
#       " my age is "+ age+" and gender)
#solution 1- int variable + replace by,
print("my name is"+name +
       "my age is ",age" gender is "+ gender )
#solution 2 - enclosed the variable inside string statment using f 
#pass the variable in {}       
print (f"my name is {name}my age is {age}and gender is{gender}")
#