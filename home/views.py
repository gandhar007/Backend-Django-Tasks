from django.shortcuts import render
from django.http import HttpResponse,request
from home import task_1

# Create your views here.
'''
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
    return HttpResponse(x)
'''

pk1 =0
pk2 =0
#task_1.binary_number(request,pk1,pk2)

def output(request,pk1,pk2):
    return(task_1.binary_number(request,pk1,pk2))
    

