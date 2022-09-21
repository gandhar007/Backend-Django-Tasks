def adjacent_1s():
    x={}
    i = int(input('Enter the First Number: '))
    n = int(input('Enter the Second Number: '))

    for a in range(i,n):
        binary = bin(a)[2:]
        c=0
        for index in binary:
            if(index=='1' and c=='1'):
                x[a]=True
                break
            else:
                x[a]=False
            c=index
    print(x)

adjacent_1s()



    
    

    








    



    
    