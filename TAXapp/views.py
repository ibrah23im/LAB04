from django.shortcuts import render
from django.http import HttpResponse

Tax_rate=15
def defaultView(request):
    return render (request,"TAXapp/index.html")

def view2(request,number):
    number=number+(Tax_rate/100*number)
    return HttpResponse(number)
def TaxRate(request):
    return render(request,"TAXapp/TAXveiw.html",{"Tax_rate":Tax_rate})

# Create your views here.
