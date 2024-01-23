# models.py
from django.db import models

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

    # CharField for EnquirySource

    college_Name = models.CharField(max_length=100,default='Default_college_Name')
    year_of_pass = models.IntegerField()
    roll_no = models.CharField(max_length=15)
    registration_number = models.CharField(max_length=15)
    photo = models.ImageField(upload_to='student_photos/')


    def __str__(self):
        return self.student_name