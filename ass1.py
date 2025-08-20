#Factorial program:
num = int(input())
factorial = 1
n = num
while n > 1:
    factorial *= n
    n -= 1
print(f"Factorial of {num} is {factorial}")
#Reverse a number using a while loop.
def reverse(num):
    rev=0
    while num>0:
        rem=num%10
        rev=rev*10+rem
        num=num//10
    return rev
num=int(input())
result=reverse(num)
print(result)

#prinr all numbers that are divisible by a and 5 from 1 to 100
num=1
while num<=100:
    if num%3==0 and num%5==0:
        print(num,end=' ')
    num+=1

# Login page:
def login():
    username=input("Enter your username: ")
    savedPassword="123456"
    count=1
    while count<4:
        count+=1
        password=input("Enter your password here: ")
        if password==savedPassword:
            print("Login Successfull")
            break
        elif password!=savedPassword:
            print(f"Wrong Password, You have {4-count} more attempts left")
            if count==4:
                print("You have exhaused your login attempts. Revisit after 24hrs.")
        else:
            print("Something went wrong")
            break
login()