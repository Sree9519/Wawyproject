from django.shortcuts import render
from .models import Staff,tbl_Customer,AssignStaff_Location
# Create your views here.
def login(request):
    return render(request,'login.html')
