from django.shortcuts import render

# Create your views here.
def gowns(request):
    return render(request,'gowns.html')
