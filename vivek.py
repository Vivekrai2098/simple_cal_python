# simple calculator in python program
print("simple table calculator")
num=eval(input("what you do with your number\n add for 1\nmultiply for 2\nsubtract for 3\n divide for 4\n"))
number=eval(input("enter your number here"))
number2=eval(input("enter your second number here"))
print("*"*20)
if num==1:
    sum=number+number2
    print("your adding number is:=",sum)
elif num==2:
    sum=number*number2
    print("your multiply number is:=",sum)
elif num==3:
    sum=number-number2
    print("your subtract number is:=",sum)
elif num==4:
    sum=number/number2
    print("your divide number is:=",sum)
else:
    print("wrong output")
print("*"*20)