from django.shortcuts import render
app_name='welcomeApp'

# Create your views here.
def welcome(request):
    return render(request ,'welcome.html')