'''attributes=["hi","hello"]
cars=["audi","telsa"]
for attribute in attributes:
    for car in cars:
        print(car,attribute)
    print("______")'''
'''# iterate from i=0 to 6
for _ in range(0,7):
    print("jyothi")

# iterate from i = 0 to 3
for _ in range(0, 4):
    print('Hi')'''

'''num1=int(input('enter a number:'))
if num1%15==0:
    print('FizzBuzz')
elif num1%5==0:
    print('Buzz')
elif num1%3==0:
    print('Fizz')
else:
    print('invalid')'''

'''units=int(input('enter current bill units:'))
if units>=100:
    print(units*2)
else:
    if units>=200:
        print(units*3)
    else:
        if units>=300:
            print(units*5)
        else:
            if units>0:
                print(units*0)'''

'''num1=int(input('enter a number:'))
num2=int(input('enter a number:'))
op=input('enter a operator:')
if op=='+':
    print(num1+num2)
elif op=='-':
    print(num1-num2)
elif op=='*':
    print(num1*num2)
elif op=='/':
    if num2 !=0:
        print(num1/num2)
    else:
        print('division by zero is not possible')
else:
    print('Invalid operator')'''
#loops
# for loop
#while loop
#Advantages
'''save time,save space,flexibility i-iteration,in-membership operator
for i in -string,list,tuple,dict,set,range'''
'''for i in 'good morning':
    print(i)
    print('hello')'''
#print 1 to n natural nubers
'''n=100
for i in range(1,n+1):
    if i%2==0:
        print(i)'''
'''num1=100
for num1 in range(1,101):
    if num1%15==0:
        print('FizzBuzz')
    elif num1%5==0:
        print('Buzz')
    elif num1%3==0:
        print('Fizz')
    else:
        print('invalid')'''

'''str1='happy birthday'
for i in str1:
    if i in 'a e i o u':
        print(i)
str1='happy birthday'
for i in str1:
    if i not in 'a e i o u':
        print(i)
str1='happy bithday'
for i in str1:
    if i in '[a],[e],[i],[o],[u]':
        print(i)'''
#while loop
'''num1=25
while num1<30:
    print('kingdom ela undhi')
    print(num1)
    (num1)+=1'''
#print 1 to 10 no
'''num1=1
while num1<101:
    print(num1)
    num1+=1'''
#print even num
'''num1=2
while num1<101:
    print(num1)
    num1+=2'''
#17 table for loop
#and while loop
#17*1=17
'''num1=int(input('enter a number:'))
for i in range(1,21):
    print(num1,'x',i,'=',num1*i)'''
'''i=1
print()
while i<21:
    print(i,'x',i,'=',n*1)
    i+=1'''
#class 1 roll 1
#class 1 roll 2
#class 1 roll 3

'''for class_no in range(1,11):
    print(class_no,'CLASS')
    if class_no%2==1:
        for roll_no in range(1,32):
            print('class',class_no,'roll_no',roll_no)'''
            
'''class_no=1
while class_no<11:
    roll_no=1
    while roll_no<31:
        print('class',class_no,'roll_no',roll_no)
        roll_no+=1
    class_no+=1'''
#jump statements-break,continue and pass



