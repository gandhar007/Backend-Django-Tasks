from django.http import HttpResponse,request

def binary_number(request,pk1,pk2):
    x = {}
    for i in range(int(pk1),int(pk2)):
        binary = bin(i)[2:]
        c = 0 
        for index in binary:
            if(index=='1' and c=='1'):  
                x[i]=True
                break
            else:
                x[i]=False
            c=index    
    return HttpResponse(str(x))