#-> it is used to comment the line 
#-> it is also used to define the code meaning 
#-> it can also comment and uncomment multiple lines using ctrl + /

# comment example 
# write a program to print your name 
print("My name is sahil thakur ") # print function to display statement 

# variables can store the value and it can change at any time
name = "sahil thakur"
#pass the variable  in the print function 
print("My name is "+name) # + is used to concatenate the strings 

#declare and initialize the multiple variables 
#email=himanshu0201pal@gmail.com
age = 33
gender ="male"
#pass the multiple variable in print function 
# this line give the type error 
#reason for error str can't be concatenate with integer 
# problem
#print(" my name is "+name+
#" my age is "+age + " and gender is "+ gender )
# solution 1 - int variable + replace by , 
print("my name is "+ name +
      " my age is ",age ," and gender is "+ gender)
# solution 2 - enclosed the variable inside string statement using f
# pass the variable in {}
print(" my name is {name} my age is {age} and gender is {gender}")


#data type is python 
print (type (name))#type function return datatype of variable 
print (type(age) )
#1. str -> it can store the string data eg. name ="sahil"
#2. int -> it can store the decimal no e.g. percentage =75.43

#typecasting in python:- convert one datatype to another datatypes
#e.g. sometime when we purchase item in float we paid in integer 
purchaseitemprice =90.99
purchaseitemprice= int(purchase itemprice)
print("paid amount is",paiditemprice)





#note -> string can't be converted into int reason string not ascii

#to get the input from user using input()function 
collegename=input("enter your collage name")
collegefee= input ("enter your college fee"))
print("my college name is "+collegename+collegefee)
#note:- the input function has default return type str 
#add scholarship of 25000 in fee
collegefee= collegefee -25000
print("after scholarship my fee" collegefee)
#find the age in year when bornyear and currentyear given by user  

