'''operators'''
#airthematic operators
a,b=5,8
sum=(a+b)
sum=(a-b)
sum=(a/b)
sum=(a%b)
sum=(a*b)
print("floor division:", a//b)
print("power:",a**b)

#Assignment operator
a,b=1,2 #Assignment Operator
a+=b    #Addition Assignment
print(a)
a-=b    #Subtraction Assignment
print(a)
a*=b    #Multiplication Assignment
print(a)
a/=b    #Division Assignment    
print(a)
a%=b    #Remainder Assignment 
print(a)
a**=b   #Exponent Assignment
print(a)

#comparison operator
a,b=6,7
print('a==b=',a==b)
print('a!=b=',a!=b)
print('a>b=', a>b)
print('a<b=', a<b)

#logical operator
a,b=1,9
print((a>1)and(b>=9))
print((a<1)or(b<=9))
#not true
#Bitwise operator

def sub_total(amount,friends):
    tax=20/100*amount
    total=amount+tax
    amount=total/friends
    return amount




