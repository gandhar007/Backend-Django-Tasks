def adjacent_1s(i,n):
    x={}
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

i = int(input('Enter the First Number: '))
n = int(input('Enter the Second Number: '))
adjacent_1s(i,n)



    
    

    








    



    
    