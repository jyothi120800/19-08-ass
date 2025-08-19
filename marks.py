print('press 1 to get first sem s.g.p.a')
print('press 2 to get second year s.g.p.a')
print('press 3 to get third sem s.g.p.a')
print('press 4 to get fourth sem s.g.p.a')
print('press 5 to get total c.g.p.a of completed sems')
print('press any key oterthan 1,2,3,4 to exit')
tot=[]
div=[]
while True:
    ch=input('enter your choice :')
    if ch=='3':
        def cgp(g):
            if g=='A+' or g=='a+':
                return 10.0
            elif g=='A' or g=='a':
                return 9.0
            elif g=='B' or g=='b' :
                return 8.0
            elif g=='C' or g=='c':
                return 7.0
            elif g=='D' or g=='d':
                return 6.0
            elif g=='E' or g=='e':
                return 5.0

        sub=['DM','AI','CC','MAD','DEV','MOOCs','DM LAB','MAD LAB','MINI LAB','Intern']
        credit=[4,4,3,4,4,2,2,2,2,2]
        k=sum(credit)
        grades=[]
        cg=[]
        div.append(k)
        for i in sub:
            print("Enter",i," Grade :",end="")
            temp=input()
            grades.append(temp)

        for i in grades:
            temp=cgp(i)
            cg.append(temp)

        cgpa=0
        for i in zip(cg,credit):
            cgpa=cgpa+(i[0]*i[1])

        cgpa=cgpa/29
        per=(cgpa-0.5)*10

        print()
        for i in zip(sub,grades,cg,credit):
            h=0
            print(i[0],'-',i[1],':',i[2],'--->',i[2]*i[3])
            h=h+i[2]*i[3]
            tot.append(h)
        print('\nCGPA:',cgpa)
        print('Percentage :',per)
    elif ch=='1':
        def cgp(g):
            if g=='A+' or g=='a+':
                return 10.0
            elif g=='A' or g=='a':
                return 9.0
            elif g=='B' or g=='b' :
                return 8.0
            elif g=='C' or g=='c':
                return 7.0
            elif g=='D' or g=='d':
                return 6.0
            elif g=='E' or g=='e':
                return 5.0

        sub=['DS','DBMS','OS','CN','DMS','DS LAB','DBMS LAB','CSS LAB']
        credit=[4,4,3,3,4,2,2,2]
        k=sum(credit)
        grades=[]
        cg=[]
        div.append(k)
        for i in sub:
            print("Enter",i," Grade :",end="")
            temp=input()
            grades.append(temp)

        for i in grades:
            temp=cgp(i)
            cg.append(temp)

        cgpa=0
        for i in zip(cg,credit):
            cgpa=cgpa+(i[0]*i[1])

        cgpa=cgpa/24
        per=(cgpa-0.5)*10

        print()
        for i in zip(sub,grades,cg,credit):
            h=0
            print(i[0],'-',i[1],':',i[2],'--->',i[2]*i[3])
            h=h+i[2]*i[3]
            tot.append(h)
        print('\nCGPA:',cgpa)
        print('Percentage :',per)
    elif ch=='2':
        def cgp(g):
            if g=='A+' or g=='a+':
                return 10.0
            elif g=='A' or g=='a':
                return 9.0
            elif g=='B' or g=='b' :
                return 8.0
            elif g=='C' or g=='c':
                return 7.0
            elif g=='D' or g=='d':
                return 6.0
            elif g=='E' or g=='e':
                return 5.0

        sub=['java','wt','python/c++','se','p&s','java LAB','wt LAB','python/c++ LAB']
        credit=[4,4,4,3,3,2,2,2]
        k=sum(credit)
        grades=[]
        cg=[]
        div.append(k)
        for i in sub:
            print("Enter",i," Grade :",end="")
            temp=input()
            grades.append(temp)

        for i in grades:
            temp=cgp(i)
            cg.append(temp)

        cgpa=0
        for i in zip(cg,credit):
            cgpa=cgpa+(i[0]*i[1])

        cgpa=cgpa/24
        per=(cgpa-0.5)*10

        print()
        for i in zip(sub,grades,cg,credit):
            h=0
            print(i[0],'-',i[1],':',i[2],'--->',i[2]*i[3])
            h=h+i[2]*i[3]
            tot.append(h)
        print('\nCGPA:',cgpa)
        print('Percentage :',per)
    elif ch=='4':
        g=input('enter grade you get in project :')
        credit=10
        div.append(credit)
        if g=='A+' or g=='a+':
            tot.append(10*credit)
            print('you get :',(10*credit)/credit)
        elif g=='A' or g=='a':
            tot.append(9*credit)
            print('you get :',(9*credit)/credit)
        elif g=='B' or g=='b' :
            tot.append(8*credit)
            print('you get :',(8*credit)/credit)
        elif g=='C' or g=='c':
            tot.append(7*credit)
            print('you get :',(7*credit)/credit)
        elif g=='D' or g=='d':
            tot.append(6*credit)
            print('you get :',(6*credit)/credit)
        elif g=='E' or g=='e':
            tot.append(5*credit)
            print('you get :',(5*credit)/credit)
    elif ch=='5':
        s=sum(tot)
        m=sum(div)
        c=s/m
        print('total c.g.p.a is :',c)
        print('total percentage is :',(c-0.5)*10)
    else:
        print('exiting...')
        print('exited.')
        break
