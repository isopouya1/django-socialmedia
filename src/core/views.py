from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')

def Sign_up(request):
    return render(request,'signup.html')