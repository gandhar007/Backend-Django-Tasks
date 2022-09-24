from django.shortcuts import render
import requests
from django.http import HttpResponse

# Create your views here.

def search(request):
    return render(request, 'search.html')

def result(request):
    userid = request.GET["userid"]
    url = "https://instagram130.p.rapidapi.com/username-by-id"
    querystring = {"userid":userid}
    headers = {
	    "X-RapidAPI-Key": "8839b057acmsh50c079b90cc09a3p1efacbjsncb420c663ec6",
	    "X-RapidAPI-Host": "instagram130.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers, params=querystring).json()
    return render(request, 'result.html', {"response":response})
    #return HttpResponse(response["data"]["username"])
    
    
    
