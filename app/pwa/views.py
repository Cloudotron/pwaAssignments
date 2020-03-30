from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'index.html',{"name":"Sumanta Sharma"})
# Create your views here.
def base_layout(request):
	template='index.html'
	return render(request,template)