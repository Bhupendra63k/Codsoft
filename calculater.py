print("welcome to calculater")
print("press s to start")
inp=input("enter s here to start :")
if inp!='s':
   print("please try again and press s to star ")
else :
   print("go to operation portal")
operations=('''
            '+'=perform  addition operations between number1 and number2 
             '-'=perform  submission program between number1 and number2
             '*'=perform  multiplication program between number1 and number2
             '/'=perform  divison program between number1 and number2
''')
print(operations)
Number1=int(input("enter first number :"))
Number2=int(input("enter second number :"))
operation=int(input("enter operation yo wnat to do : "))
if operation==1:
   print("the sum of Number1 and Number2 is :",Number1+Number2)
elif operation==2:
   print("the sum of Number1 and Number2 is :", Number1-Number2)
elif operation ==3:
   print("the sum of Number1 and Number2 is :",Number1*Number2)
elif operation==4:
   print("the sum of Number1 and Number2 is :",Number1/Number2)
else :
 print("invalid number entered")
 print("thanks")