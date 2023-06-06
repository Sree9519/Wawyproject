# Generated by Django 4.1.7 on 2023-06-06 10:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AssignStaff_Location',
            fields=[
                ('Assign_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('createdby', models.CharField(blank=True, max_length=250, null=True)),
                ('createddate', models.DateTimeField(auto_now_add=True)),
                ('updatedby', models.CharField(blank=True, max_length=250, null=True)),
                ('updateddate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('staff_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('createdby', models.CharField(blank=True, max_length=250, null=True)),
                ('createddate', models.DateTimeField(auto_now_add=True)),
                ('updatedby', models.CharField(blank=True, max_length=250, null=True)),
                ('updateddate', models.DateTimeField(auto_now_add=True)),
                ('Name', models.TextField(max_length=255)),
                ('Nationality', models.TextField(max_length=255)),
                ('staff_idNo', models.CharField(max_length=250)),
                ('C_Address', models.CharField(max_length=250)),
                ('P_Address', models.CharField(max_length=250)),
                ('C_mobile', models.CharField(max_length=250)),
                ('P_mobile', models.CharField(max_length=250)),
                ('BGroup', models.CharField(choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('O+', 'O-'), ('AB+', 'AB+'), ('AB-', 'AB-')], max_length=50)),
                ('PassPort_No', models.CharField(blank=True, max_length=250, null=True)),
                ('PassPort_EXP', models.DateTimeField(auto_now_add=True)),
                ('emirate_id', models.CharField(blank=True, max_length=250, null=True)),
                ('Emirate_Exp', models.DateTimeField(auto_now_add=True)),
                ('DrivingLicense_No', models.CharField(blank=True, max_length=250, null=True)),
                ('DrivingLicense_EXP', models.DateTimeField(auto_now_add=True)),
                ('HealthCerticate_No', models.CharField(blank=True, max_length=250, null=True)),
                ('HealthCerticate_EXP', models.DateTimeField(auto_now_add=True)),
                ('Insurance_No', models.CharField(blank=True, max_length=250, null=True)),
                ('Insurance_Exp', models.DateTimeField(auto_now_add=True)),
                ('EmergencyContactname', models.CharField(blank=True, max_length=250, null=True)),
                ('EmergencyContactmobile', models.CharField(blank=True, max_length=250, null=True)),
                ('StaffPhoto_location', models.CharField(blank=True, max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='tbl_Customer',
            fields=[
                ('Cust_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('createdby', models.CharField(blank=True, max_length=250, null=True)),
                ('createddate', models.DateTimeField(auto_now_add=True)),
                ('updatedby', models.CharField(blank=True, max_length=250, null=True)),
                ('updateddate', models.DateTimeField(auto_now_add=True)),
                ('Cust_Name', models.CharField(blank=True, max_length=250, null=True)),
                ('CustType_id', models.CharField(choices=[('home', 'home'), ('coperate', 'coperate')], max_length=50)),
                ('BuildinNo', models.CharField(blank=True, max_length=250, null=True)),
                ('RommNo', models.CharField(blank=True, max_length=250, null=True)),
                ('Mobilno', models.CharField(blank=True, max_length=250, null=True)),
                ('Alt_Mobile', models.CharField(blank=True, max_length=250, null=True)),
                ('Whatsapp_no', models.CharField(blank=True, max_length=250, null=True)),
                ('Gpse', models.CharField(blank=True, max_length=250, null=True)),
                ('Gpsn', models.CharField(blank=True, max_length=250, null=True)),
                ('Username', models.CharField(blank=True, max_length=250, null=True)),
                ('password', models.CharField(blank=True, max_length=250, null=True)),
                ('Pricegroupid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]