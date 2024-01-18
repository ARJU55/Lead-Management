from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User




class State(models.Model):
   name = models.CharField(max_length=200)
   def __str__(self):
            return self.name

class District(models.Model):
   name = models.CharField(max_length=200)
   state = models.ForeignKey('State', on_delete=models.CASCADE)
   def __str__(self):
        return self.name



class Branches(models.Model):
    branch_name = models.CharField(max_length=200)
    branch_code = models.CharField(max_length=200)  
    address = models.TextField()
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    pincode = models.IntegerField()
    mobile_number = models.CharField(max_length=10)
    email_id = models.EmailField()
   
    
    def clean(self):
       if self.state is None and self.district is not None:
           raise ValidationError("State cannot be null when District is filled")
    def __str__(self):
            return self.branch_name
      
      
   
class Enquirysource(models.Model):
   name = models.CharField(max_length=200)
   def __str__(self):
        return self.name
class Followupstatu(models.Model):
   YES_NO_CHOICES = [
       ('yes', 'Yes'),
       ('no', 'No'),
   ]
   Name_Of_The_Follower = models.CharField(max_length=200)
   followup_statu = models.CharField(max_length=3, choices=YES_NO_CHOICES, default='no')
   def __str__(self):
             return self.Name_Of_The_Follower
   
class Qualification(models.Model):
      name = models.CharField(max_length=200)

      def __str__(self):
         return self.name
      


class Course(models.Model):
   course = models.CharField(max_length=200)
   active = models.BooleanField(default=True)

   def __str__(self):
       return self.course

    
 
class syllabus(models.Model):
       name=models.CharField(max_length=300)
      
       def __str__(self):
             return self.name


class Batches(models.Model):
    branch_name = models.ForeignKey(Branches, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    start_date = models.DateField()
    start_time = models.TimeField()
    end_date = models.DateField()
    end_time = models.TimeField()
    trainer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=False, related_name="trainer", limit_choices_to={"groups__name": 'Trainer'})
    
    def __str__(self):
    

   
        return f"{self.branch_name} {self.start_date} {self.start_time} {self.course} {self.trainer.username} - {self.trainer.groups.first()}"
