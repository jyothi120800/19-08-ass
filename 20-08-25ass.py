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

