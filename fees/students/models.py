# models.py
from django.db import models
from new_app.models import *
from django.core.validators import RegexValidator

class Students(models.Model):
    student_name = models.CharField(max_length=200)
    
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('trans', 'Transgender'),
        ('others', 'Others'),
    ]
    
    gender = models.CharField(max_length=15, choices=GENDER_CHOICES, default='null')
    email = models.CharField(max_length=100)
    alternative_email = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    alternative_address = models.CharField(max_length=200)
    dob = models.DateField()
    mobile = models.CharField(max_length=10)
    street = models.CharField(max_length=100)
    pincodes = models.CharField(max_length=7)
    whatsapp = models.CharField(max_length=20, null=True)

    

    college_Name = models.CharField(max_length=100,default='Default_college_Name')
    year_of_pass = models.IntegerField()
    roll_no = models.CharField(max_length=15)
    qualification = models.ForeignKey(Qualification, on_delete=models.SET_NULL, null=True, blank=True)
    registration_number = models.CharField(max_length=15)
    photo = models.ImageField(upload_to='student_photos/',null=True)
    Enquirysource = models.ForeignKey(Enquirysource, on_delete=models.SET_NULL, null=True, blank=True)
    
    phone = models.CharField(
        max_length=15, null=True,
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
            )
        ]
    )
    COURSE= models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, blank=True)



    def __str__(self):
        return self.student_name