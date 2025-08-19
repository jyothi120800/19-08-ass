'''1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
n = 5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j, end=" ")
    print()

2.*
* *
* * *
* * * *
** ** *
n=5
for rows in range(n):
    for cols in range(rows+1):
        print("*", end=" ")
    print()
    
3.1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5 

n=5
for rows in range(1, n+1):
    for cols in range(1, rows+1):
        print(rows, end=" ")
    print()
4.1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 

n=5
for rows in range(1, n+1):
    for cols in range(1,rows+1):
        print(cols, end=" ")
    print()
    
5.* * * * * 
* * * * 
* * * 
* * 
* 

n=5
for rows in range(1, n+1):
    for cols in range(1, n-rows+2):
        print("*", end=" ")
    print()
    
6.1 1 1 1 1 
2 2 2 2 
3 3 3 
4 4 
5 

n=5
for rows in range(1, n+1):
    for cols in range(1, n-rows+2):
        print(rows, end=" ")
    print()

7.1 2 3 4 5 
1 2 3 4 
1 2 3 
1 2 
1 

n=5
for rows in range(1, n+1):
    for cols in range(1, n-rows+2):
        print(cols, end=" ")
    print()
8.      * 
      * * 
    * * * 
  * * * * 
* * * * * 
n=5
for rows in range(1, n+1):
    for space in range(1, n-rows+1):
        print(" ", end=" ")
    for cols in range(1, rows+1):
        print("*", end=" ")
    print()
    
9.5 5 5 5 5 
4 4 4 4 
3 3 3 
2 2 
1 

n = 5
for rows in range(1,n+1):
    for cols in range(1,n-rows+2):
        print(n-rows+1, end=" ")
    print()
    
10.5 4 3 2 1 
5 4 3 2 
5 4 3 
5 4 
5 

n = 5
for rows in range(1,n+1):
    for cols in range(1,n-rows+2):
        print(n-cols+1, end=" ")
    print()
    
11.     1 
      2 2 
    3 3 3 
  4 4 4 4 
5 5 5 5 5 

n=5
for rows in range(1, n+1):
    for space in range(1, n-rows+1):
        print(" ", end=" ")
    for cols in range(1, rows+1):
        print(rows, end=" ")
    print()
12.* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * * 
n=5
for rows in range(n):
    for cols in range(n):
        print("*", end=" ")
    print()
13.1 1 1 1 1 
2 2 2 2 2 
3 3 3 3 3 
4 4 4 4 4 
5 5 5 5 5 
n=5
for rows in range(1, 1+n):
    for cols in range(n):
        print(rows, end=" ")
    print()
14.1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5 
n=5
for rows in range(n):
    for cols in range(1,1+n):
        print(cols, end=" ")
    print()

15.* * * * * 
   * * * * 
     * * * 
       * * 
         * 
n=5
for rows in range(1, n+1):
    for space in range(1, rows+1):
        print(" ", end=" ")
    for cols in range(1, n-rows+2):
        print("*", end=" ")
    print()

 16.      * 
        * * * 
      * * * * * 
    * * * * * * * 
  * * * * * * * * * 
    


n=5
for rows in range(n):
    for cols in range(rows,n):
        print(" ", end=" ")
    for cols in range(rows):
        print("*", end=" ")
    for cols in range(1+rows):
        print("*", end=" ")
    print()
    
17.       * * * * * * * * * 
            * * * * * * * 
              * * * * * 
                * * * 
                  * 
n=5
for rows in range(n):
    for cols in range(rows+n):
        print(" ", end=" ")
    for cols in range(rows,n-1):
        print("*", end=" ")
    for cols in range(rows,n):
        print("*", end=" ")
    print()
         * 
18.    * * * 
      * * * * * 
    * * * * * * * 
  * * * * * * * * * 
    * * * * * * * 
      * * * * * 
        * * * 
          * 
n=5
for rows in range(n-1):
    for cols in range(rows,n):
        print(" ", end=" "
    for cols in range(rows):
        print("*", end=" ")
    for cols in range(1+rows):
        print("*", end=" ")
    print()
for rows in range(n):
    for cols in range(rows+1):
        print(" ", end=" ")
    for cols in range(rows,n-1):
        print("*", end=" ")
    for cols in range(rows,n):
        print("*", end=" ")
    print()'''
n=10
for rows in range(n):
    for cols in range(n):
        print(" ", end=" ")
    for cols in range(rows):
        print("*",end=" ")
    print()




    
