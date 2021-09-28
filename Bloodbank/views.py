from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
 return render(request, 'bloodbank/home.html')

def display(request):
 result = {}
 result["Name"]=request.GET["name"]
 result["Age"] = request.GET["age"]
 result["Blood_Group"] = request.GET["bloodgroup"]
 result["Phone_Number"] = request.GET["phonenumber"]
 
 persons=[]
 persons.append(result)

 return render(request, 'bloodbank/display.html', {'persons': persons})