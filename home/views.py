from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "home/home.html")


from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def parent(request):
    return render(request, "home/parent.html")

