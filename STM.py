def triangle(side1,side2,side3):
    if side1 + side2 > side3 and side2 + side3 > side1 and side1 + side3 > side2:
        print('traiangle is possible')
        if side1 == side2 or side1 == side3 or side2 == side3 or side2 == side1 :
            print('isolated traingle')
        elif side1 == side2== side3:
            print('equlaterial triangle')
        elif side1 != side2 != side3:
            print('scalar traingle')
    elif (side1**2 + side2**2 == side3**2) or (side2**2 + side3**2 == side1**2) or (side1**2 + side3**2 == side2**2):
        print("right angled triangle")
    else:
        print('not possible')
    

triangle(3,4,5)
triangle(25,45,32)
