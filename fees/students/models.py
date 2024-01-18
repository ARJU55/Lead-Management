from django.db import models

# Create your models here.
# models.py
from django.db import models

class Students(models.Model):
#personal_info    

    student_name= models.CharField(max_length=200)
    
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
    
    def __str__(self):
        return self.student_name
    
     

        
  
