from django.shortcuts import render
from django.http import HttpResponse
import requests
# Create your views here.
def homepage(request):
    return render(request,'index.html')



def index(request):
    data = True
    result = None
    while(data):
        try:
            result = requests.get('https://api.covid19api.com/summary') # get summary data from api
            json = result.json()
            result = json['Global']
            countries = json['Countries']
            data = False
        except:
            data = True

    return render(request,'index.html', {'result':result,'country':countries})
