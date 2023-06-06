from django.db import models
from django.contrib.auth.models import User
import uuid
app_name = 'accounts'
# Create your models here.
class Staff(models.Model):
    staff_id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    createdby= models.CharField(max_length=250,null=True,blank=True)
    createddate=models.DateTimeField(auto_now_add=True,editable=False)
    updatedby=models.CharField(max_length=250,null=True,blank=True)
    updateddate=models.DateTimeField(auto_now_add=True,editable=False)
    Name=models.TextField(max_length=255)
    Nationality=models.TextField(max_length=255)
    staff_idNo=models.CharField(max_length=250)
    C_Address=models.CharField(max_length=250)
    P_Address=models.CharField(max_length=250)
    C_mobile=models.CharField(max_length=250)
    P_mobile=models.CharField(max_length=250)
    YOUR_CHOICES = [('A+','A+'), ('A-','A-'), ('B+','B+'), ('B-','B-'), ('O+','O-'), ('AB+','AB+'),
                    ('AB-','AB-')]
    BGroup=models.CharField(max_length=50,choices=YOUR_CHOICES)
    PassPort_No=models.CharField(max_length=250,null=True,blank=True)
    PassPort_EXP=models.DateTimeField(auto_now_add=True,editable=False)
    emirate_id=models.CharField(max_length=250,null=True,blank=True)
    Emirate_Exp=models.DateTimeField(auto_now_add=True,editable=False)
    DrivingLicense_No=models.CharField(max_length=250,null=True,blank=True)
    DrivingLicense_EXP=models.DateTimeField(auto_now_add=True,editable=False)
    HealthCerticate_No=models.CharField(max_length=250,null=True,blank=True)
    HealthCerticate_EXP=models.DateTimeField(auto_now_add=True,editable=False)
    Insurance_No=models.CharField(max_length=250,null=True,blank=True)
    Insurance_Exp=models.DateTimeField(auto_now_add=True,editable=False)
    EmergencyContactname=models.CharField(max_length=250,null=True,blank=True)
    EmergencyContactmobile=models.CharField(max_length=250,null=True,blank=True)
    U_id=models.IntegerField
    isdelete=models.BigIntegerField
    StaffPhoto_location=models.CharField(max_length=250,null=True,blank=True)

class AssignStaff_Location(models.Model):
    Assign_id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    createdby=models.CharField(max_length=250,null=True,blank=True)
    createddate=models.DateTimeField(auto_now_add=True,editable=False)
    updatedby=models.CharField(max_length=250,null=True,blank=True)
    updateddate=models.DateTimeField(auto_now_add=True,editable=False)
    Staff_id=models.IntegerField
    Location_id=models.IntegerField
    Status=models.BooleanField

class tbl_Customer(models.Model):
    Cust_id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    createdby=models.CharField(max_length=250,null=True,blank=True)
    createddate=models.DateTimeField(auto_now_add=True,editable=False)
    updatedby=models.CharField(max_length=250,null=True,blank=True)
    updateddate=models.DateTimeField(auto_now_add=True,editable=False)
    Cust_Name=models.CharField(max_length=250,null=True,blank=True)
    Custtype=[('home','home'),('coperate','coperate')]
    CustType_id=models.CharField(max_length=50,choices=Custtype)
    Location_id=models.IntegerField
    BuildinNo=models.CharField(max_length=250,null=True,blank=True)
    RommNo=models.CharField(max_length=250,null=True,blank=True)
    Mobilno=models.CharField(max_length=250,null=True,blank=True)
    Alt_Mobile=models.CharField(max_length=250,null=True,blank=True)
    Whatsapp_no=models.CharField(max_length=250,null=True,blank=True)
    Pricegroupid=models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    Staff_id=models.ForeignKey
    creditlimit=models.FloatField
    creditdays=models.IntegerField
    Credit_Invoices=models.IntegerField
    Gpse=models.CharField(max_length=250,null=True,blank=True)
    Gpsn=models.CharField(max_length=250,null=True,blank=True)
    Username=models.CharField(max_length=250,null=True,blank=True)
    password=models.CharField(max_length=250,null=True,blank=True)
    iisdelete=models.BooleanField



















