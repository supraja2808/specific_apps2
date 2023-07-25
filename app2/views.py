from django.shortcuts import render

# Create your views here.
def h3(request):
    return render(request,'h3.html')

def h4(request):
    return render(request,'h4.html')