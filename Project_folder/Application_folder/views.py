# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
#here is the response to the request and this function is passed in the urls.py file so that this response is
#shown in the web at http://127.0.0.1:8000/
def index(request):
 return render(request,'main.html',{"testvar":"My name is Sanpreet Singh and I am dispalying the result with the help of key-pair."
                                              " Key is taken from the html file and value is passed here."
                                    "HTML is made using Bootstarpping cdn with javaquery, javascript is added"
                                              })
