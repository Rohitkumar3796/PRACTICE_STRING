# abc=input("enter the file name")
# extn=abc.split(".")
# print("extension is "+repr(extn[1]))
#how to make file and keep the name depends on user
# abc=input("enter the file name")
# f33=open(abc+".txt","w")
#length of the string
# a="rohit is a good boy and he is a 24 years old now he is doing nothing, he is only preparing for python"
# print(len(a))
# b="google is a world"
# print((b.count("o"),(b.count("g"))))
# string=input("enter the name")
#Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string
# length is less than 2, return instead of the empty string.
# string="rohitgood"
# string1=string[0:2]
# string2=string[-2::]
# string3=string1+string2
# print(string3)
# if len(string1)<2:
#     print("empty")
# else:
#     print("bigger")
#2nd way FROM FUNCTION
# def check(str):
#     str1=str[0:2]+str[-3::]
#     print(str1)
#     if len(str1)<2:
#         return "empty"
#     else:
#         return "big"
# print(check("goodboy"))
#3rd way first check length than take first 2 char and last two char
# print("""_________""")
# def check1(string):
#     if len(string)<2:
#         return ""
#     return string[0:2] +string[-2::]
# print(check1("goodboy"))
# =============================
# Write a Python program to get a string from a given string where all occurrences of its first char have been changed
# to '$', except the first char itself. Go to the editor
# Sample String : 'restart'
# Expected Result : 'resta$t'
# string="restart"
# print(string.replace("s","$"))
#from function
# def change(str):
#     str1=str
#     print(str1.replace("s","$"))
# change("restart")
#======================================
# Write a Python program to get a single string from two given strings, separated by a space and swap the first two
# characters of each string
# name = "rohit amit"
# New_Name = name.split(" ")
# name1 = New_Name[0]
# name2 = New_Name[1]
# N_Name1=name1[0:2]
# N_Name2=name2[0:2]
# temp=N_Name1
# N_Name1=N_Name2
# N_Name2=temp
# print(N_Name1,N_Name2)
# print(name1.replace("ro",N_Name1))
# print(name2.replace("am",N_Name2))
#INPUT FROM USER
# name =input("enter the two name")
# New_Name = name.split(" ")
# name1 = New_Name[0]
# name2 = New_Name[1]
# N_Name1=name1[0:2]
# N_Name2=name2[0:2]
# temp=N_Name1
# N_Name1=N_Name2
# N_Name2=temp
# print(N_Name1,N_Name2)
# print(name1.replace("ro",N_Name1))
# print(name2.replace("am",N_Name2))
#=================================================================
# Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
# If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is
# less than 3, leave it unchanged. Go to the editor
# Sample String : 'abc' Expected Result : 'abcing'
# Sample String : 'string' Expected Result : 'stringly'
# str='nam'
# N_str=str.__add__("ing")
# print(N_str)
# print(N_str.__add__("ly"))
# ===================================================================
# ===================2nd WAY===================
# string="The lyrics is not that poor!'The lyrics is poor!"
# string2=string.replace(string[14:24+4],"good")
# print(string2)
# =====/=/==/=/=/=/=/=/=/=/=/==/=/=/=/=/=/=/===============//////////////////////===========
# Write a Python function that takes a list of words and returns the length of the longest one
# def longest_lenth(list):
#     word=[]
#     for i in list:
#         word.append((len(i),i))
#         word.sort()
#     return word[2][1]
#
# print(longest_lenth(["studet","emple","teacher"]))
# /=//==/=/=/=/=/=/=/=/=/=/=/====/=//==/=/=/=/=/=/=/=/=/=/=/=/==/=/=/=/=/=/=/===////////////////////////====
# Python: Remove the nth index character from a nonempty string
# def string(str,n):
#     str1=list(str)
#     str1.pop(n)
#     print(str1)
#
# print(string("Employee",4))
# =/=/===//==/=//=/=/===================================////////////
# remove vowels from string
# string="hello this is rohit now, i am just writing a code to be programmer" #rht s gd by
# vowels=["a", "e", "i", "o", "u"]
# for x in string:
#     if x not in vowels:
#         print(x,end="")
# /=====/=//=/=//=/==//===//=/=/=/=//==/=====/==/
# 2nd way by function
# def remove_vowels(str):
#     vowels = ["a", "e", "i", "o", "u"]
#     for x in str:
#         if x not in vowels:
#             print(x,end="")
#
# remove_vowels("rohit is a good boy")
# ========================..............;;;;;;;;;;;;;;,,,,,,,,,,,///////////
# call a funtion inside an aother function and print
# def add(x):
#     return x+1
#
# def add_mul(z,y):
#     print(z+y)
#     print(add(x=5))
#
# add_mul(3,4)
# ===============//[==/=/=///=/==]/////////////======
# how to find factorial number  n!=n*(n-1)*n*(n-1)*n*n(n-1)........n
# 4!=4*(4-1)*3(3-1)*2(2-1)*1(1-1)*0*(0-1)(0-1=1) 4*3*2*1=24
# def fact(n):
#     if n == 0:
#         return 1
#     else:
#
#         return n * fact(n - 1)
#
# num = int(input("enter the number"))
# result = fact(num)
# print(result)
# =/=/==/==/=//==/=//==/=/=/==/=/==/=/===/=///==/=/==/=/===/=//=/=
# check_fermat
# def check_fermat(a,b,c,n):
#      if n>2 and (a**n+b**n==c**n):
#          print("Holy Smokes Fernats was wrong")
#      else:
#          print("No, that doesn't work")
#
# check_fermat(2,4,6,6)
# ===/===//===/=/==/==/===/=/=//=/=/==//===/==//==/==/==/=/=/==/==
# ===================///////////////==/=/=/==/==/=/=/=/
# RECURSION WE CALL OUR OWN FUNCTION INSIDE THE FUNCTION
# def num1(n):
#     if n<=0:
#         print("blast off")
#     else:
#         print(n)
#         num1(n-1)
# num=int(input("enter the number"))
# num1(num)
# STRING,
# def string1(na,nb):
#     if nb<=0:
#         return
#     print(na,nb)
#     string1(na,nb-1)
# string1(1,4)
# =========================
# i pass the string in function and print the string by index by the use of recursion
# def string(s,n):
#     if n==5:
#         return
#     print(s[n],n)
#     string(s, n+1)
#
# string("amit ",0)
# /==/=/==/===/=/===/====/==/=/=/===============================//////////
# def fun(x):
#     if x<0:
#         return -x
#     else:
#         return x
#
# y=fun(-1)
# print(y) (the Output is 1 because -,- is positive)
# ========================================
# x=7
# y=6
# if (x+y)>10:
#     print(1)
# else:
#     print(0)
# =================================================
# import math
# def area(radius):
#     a=math.pi*radius**2
#     return a
# b=area(4)
# print(b)
#
# def distance(x1,x2,y1,y2):
#     distance1=x2-x1
#     result1=distance1**2
#     distance2=y2-y1
#     result2=distance2**2
#     result3=result1+result2
#     Exact=math.sqrt(result3)
#     return Exact
# a=distance(1,2,4,6)
# print(a)
#
# def area_of_circle(xc,yc,xp,yp):
#     radius=distance(xc,yc,xp,yp)
#     result=area(radius)
#     return result
#
# a=area_of_circle(2,6,4,8)
# print(a)
# ==========================================////////////////////=====================
# def factorial(n):
#     space=" "*(n*n)
#     print(space,"factorial",n)
#     if n==0:
#         print(space, "return 1")
#         return 1
#     else:
#         recurse=n*factorial(n-1)
#         result=n*recurse
#         print(space,"returning",result)
#         return result
# factorial(4)
# =/==/==//==//===/=/==//==/=//===/==/=====/==
# import turtle
# bob=turtle.Turtle()
# print(bob)
# a=turtle.mainloop()
# print(a)
# for i in range(10):
#     bob.fd(100)
#     bob.lt(90)
# =/=/==/=/==/======/===/=/=/===/==/=/===/=
# a="rohit"
# for i in (0,len(a)):
#     print(i)
# =/==/=/=/==/=/=====//=/=/=/=/=/=/==//=/=/==
# def fact(n):
#     print(n)
#     if n==0:
#         return 1
#     else:
#         a=n*fact(n-1)
#         return a
#
# z=fact(5)
# print("the factorial of 5 is",z)
# =====BY THE USE OF USER==================
# def fact(n):
#     print(n)
#     if n<0:
#         print("sorry u enter negative number")
#     elif n==0:
#         return 1
#     else:
#         a=n*fact(n-1)
#         return a
# num=int(input("enter the number"))
# z=fact(num)
# print(z)
# /==/=/=/==//==/=/==/==/===/=/===/=/==/==/====/=/====/=/=
# check number is even or not
# def count_down(n):
#     while n!=1:
#         if n==0:
#             return "done"
#         elif n%2==0:
#             print(n," is even")
#             n=n-1
#         else:
#             print(n," is odd")
#             n=n-1
#
# num=int(input("enter the number"))
# result=count_down(num)
# print(result)
# /==/=/=/==//==/=/==/==/===/=/===/=/==/==/====/=/====/=/=
# /==/=/=/==//==/==/==/=//=/=/=/==/==/===/====/=
# odd_even in different way
# def odd_even(n):
#     while n!=1:
#         if n==0:
#             return "done"
#
#         elif n % 2==0:
#             n=n/2
#             print(n)
#         else:
#             n=n*3+1
#             print(n)
#
# odd_even(20)
# whem we want to pass two argument in one parameter then use two open and close brackets and u can also use , then ur
# argument looks like one argument pass in a parameter
# def name1(n):
#     return "hello"
#
# x=name1(("rohit","kumar"),)
# print(x)
# //==/==/====/==/=/=/==/=/=//=/=/==/==/==/==/=/==/
# use of map
# a=1232321
# b=str(a)
# d=map(list,b)
# v=list(d)
# print(v)
# for i in v:
#     print(i)
# /===/=//=/=/==//=/====/=//=/==/=/=======/=/=
# use of break:
# while True:
#     line=7
#     if line == "done":
#         break
#     print("hey")
#     break
# print("done")
# ===========================================================
# def hypotenuse(horizontal,vrtical):
#     ho_ve=horizontal**2+vrtical**2
#     print(ho_ve)
#     h1=math.sqrt(ho_ve)
#     return h1
#
# a=hypotenuse(6,4)
# print(a)
# statement1 if expression1 else (statement2 if expression2 else statement3)
# =-=-=-=-=-=-=-=-===-=-=-/-=-=-=/=-/=-=/-=/-=/-=/=-/-=-=/-=-=/-/
# import array as  arr
# my_array=arr.array("h",[1,2,3,4,5])
# print(my_array[::-1])