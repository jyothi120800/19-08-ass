#eligible vote
'''def eligible_age(age):
    print('eligible')if age>=19 else print('not eligible')
eligible_age(22)'''
#simple calculator
'''def simple_clac(operator,num1,num2):
    if operator== '+':
        return num1+num2
    elif operator== '-':
        return num1-num2
    elif operato== '*':
        return num1*num2
    elif operator== '%':
        return num1/num2 if num2!=0 else 'invalid denominator'
    else:
        return 'invalid operator'
operator=(input('enter a operator:'))
num1=int(input('enter a number:'))
num2=int(input('enter a number:'))
res=simple_clac(operator,num1,num1)
print(res)'''
#two largest number
'''num1=int(input('enter a number:'))
num2=int(input('enter a number:'))
if num1>num2:
    print(num1)
else:
    print(num2)
      or
num1=int(input('enter a number:'))
num2=int(input('enter a number:'))
print(num1)if num1>num2 else print(num2)'''
# check even or odd
'''num1=10
print(True)if num1%2==0 else print(False)'''
# greatest three number
'''num1,num2,num3=5,7,9
if num1>num2 and num1>num3:
    print(num1)
elif num2>num3:
    print(num2)
else:
    print(num3)'''
#check if a year i a leap year
'''year=2024
if year%400 == 0:
    print('leap year')
elif (year % 100 !=0 and year% 4 == 0):
    print('leap year')
else:
    print('Not a leap yaer')'''
#satisfy or not in pythogoris thoe
#character
#some of first n natural numbers
'''n=25
sum=0
for i in range(1,n+1):
    sum=sum+i# add **2
print(sum)
#same outputs diff stmnt
print((n *(n+1))/2)'''
#print even numbers b/w 1 &50 using while loop
'''num1=2
while num1<=50:
    print(num1)
    num1 += 2'''
# true or false
'''while True:
    num1=int(input('enter a number'))
    print(num1)
    if num1<=0:
        print('Non positive number enter a number')
        break'''
'''while True:
    print('1. square 2. cube. Anyother option will exit the code')
    choice=input('Enter your choice')
    if choice =='1' or choice== 'square':
        input_num=float(input('Enter the number to square'))
        print(input_num**2)
    elif choice =='2' or choice== 'cube':
        input_num=float(input('Enter the number to cube'))
        print(input_num**3)
    else:
        print('No valid option picked')
        print('---------Exiting--------')
        break'''

while True:
    print('1.add 2.sub 3.multiplication 4.division .Another option will wxit the code')
    choice=input('enter your choice: ')
    if choice == '1' or choice== 'add':
        input_num1=float(input('Enter the number to add: '))
        input_num2=float(input('Enter the number to add: '))
        print(input_num1+input_num2)
    elif choice == '2' or choice== 'sub':
        input_num1=float(input('Enter the number to sub: '))
        input_num2=float(input('Enter the number to sub: '))
        print(input_num1-input_num2)
    elif choice == '3' or choice== 'multiplication':
        input_num1=float(input('Enter the number to multiplication: '))
        input_num2=float(input('Enter the number to multiplication: '))
        print(input_num1*input_num2)
    elif choice == '4' or choice== 'division':
        input_num1=float(input('Enter the number to division: '))
        input_num2=float(input('Enter the number to division: '))
        print(input_num1%input_num2)
    else:
        print('No valid option picked')
        print('----------Exiting---------')
    
        
          
    





        
